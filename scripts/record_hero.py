"""Record the homepage hero walkthrough from the live Bereshit sheet.

Walks a real reader's path: the opening, the first decision (choose a passage),
the second (choose a year), a verse with its words lit, then the two Leningrad
Codex pages with the scribe's breaks highlighted. Re-run whenever the Bereshit
sheet or the engine changes so the video never shows a stale build.

    python3 scripts/record_hero.py        # writes assets/hero/bereshit-walkthrough.{mp4,webm,jpg}

Needs playwright (requirements-dev.txt) and ffmpeg on PATH.

The video is rendered frame by frame rather than screen-recorded: real-time
capture in headless Chromium drops frames, which made the scrolling judder.
For each frame we set the scroll position (a steady, wheel-like glide) and
take a screenshot. Screenshots are slower than real time, so the page's own
animations (CSS transitions and animations, GSAP tweens) are slowed by SLOWDOWN and each
frame is captured on a fixed real-time schedule; in the video they play at
normal speed.
"""

import base64
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "hero"
SIZE = {"width": 1280, "height": 800}
FPS = 30
SLOWDOWN = 5          # real seconds per video second while capturing
SPEED = 520           # glide speed, px per video second, like steady wheel scrolling
RAMP = 0.35           # seconds to ease into and out of each glide

# A visible pointer for the decision clicks (the recorder draws no mouse).
SETUP_JS = """
(slow) => {
  document.documentElement.style.scrollBehavior = 'auto';
  // The engine smooth-scrolls to a branch after a click; the recorder glides there itself.
  Element.prototype.scrollIntoView = function () {};
  if (window.gsap) gsap.globalTimeline.timeScale(1 / slow);
  // Slow every CSS transition/animation the frame it starts (CDP's
  // Animation.setPlaybackRate misses compositor transitions like the zoom).
  const seen = new WeakSet();
  (function tick() {
    for (const a of document.getAnimations()) {
      if (!seen.has(a)) { seen.add(a); a.playbackRate = a.playbackRate / slow; }
    }
    requestAnimationFrame(tick);
  })();
  const c = document.createElement('div');
  c.id = '__cursor';
  c.style.cssText = 'position:fixed;left:0;top:0;width:22px;height:22px;margin:-11px 0 0 -11px;' +
    'border-radius:50%;background:rgba(139,94,60,.35);border:2px solid #8b5e3c;z-index:99999;' +
    'pointer-events:none;opacity:0';
  document.body.appendChild(c);
}
"""


class Recorder:
    def __init__(self, page, cdp, frames_dir):
        self.page, self.cdp, self.dir = page, cdp, frames_dir
        self.n = 0
        self.t0 = None
        self.cursor = None  # (x, y) in viewport px, or None when hidden

    def snap(self):
        """Capture one frame on schedule: frame n is taken at n/FPS * SLOWDOWN real seconds."""
        if self.t0 is None:
            self.t0 = time.monotonic()
        due = self.t0 + self.n / FPS * SLOWDOWN
        wait = due - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        shot = self.cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 92})
        (self.dir / f"{self.n:05d}.jpg").write_bytes(base64.b64decode(shot["data"]))
        self.n += 1

    @property
    def video_time(self):
        return self.n / FPS

    def hold(self, seconds):
        for _ in range(round(seconds * FPS)):
            self.snap()

    def scroll_y(self):
        return self.page.evaluate("scrollY")

    def target_y(self, selector, at):
        return self.page.evaluate(
            "([s, at]) => { const e = document.querySelector(s);"
            " const y = e.getBoundingClientRect().top + scrollY - innerHeight * at;"
            " return Math.max(0, Math.min(y, document.documentElement.scrollHeight - innerHeight)); }",
            [selector, at])

    def glide_to(self, selector, at=0.42):
        """Scroll at a steady speed, easing in and out, like a reader rolling the wheel."""
        y0, y1 = self.scroll_y(), self.target_y(selector, at)
        dist = abs(y1 - y0)
        if dist < 1:
            return
        cruise = max(0.0, dist / SPEED - RAMP)  # ramps cover half their length at cruise speed
        total = cruise + 2 * RAMP
        frames = max(2, round(total * FPS))
        for i in range(1, frames + 1):
            t = i / frames * total
            # Distance covered under a trapezoid velocity profile, normalised to 1.
            if t < RAMP:
                d = t * t / (2 * RAMP)
            elif t < RAMP + cruise:
                d = RAMP / 2 + (t - RAMP)
            else:
                u = total - t
                d = (RAMP + cruise) - u * u / (2 * RAMP)
            frac = d / (RAMP + cruise)
            self.page.evaluate("y => window.scrollTo(0, y)", y0 + (y1 - y0) * frac)
            self.snap()

    def move_cursor(self, x, y, seconds):
        x0, y0 = self.cursor or (x - 140, y + 90)
        frames = round(seconds * FPS)
        for i in range(1, frames + 1):
            t = i / frames
            e = 2 * t * t if t < .5 else 1 - (-2 * t + 2) ** 2 / 2
            self.set_cursor(x0 + (x - x0) * e, y0 + (y - y0) * e)
            self.snap()

    def set_cursor(self, x, y, scale=1, opacity=1):
        self.cursor = (x, y)
        self.page.evaluate(
            "([x, y, s, o]) => { const c = document.getElementById('__cursor');"
            " c.style.left = x + 'px'; c.style.top = y + 'px'; c.style.transform = `scale(${s})`; c.style.opacity = o; }",
            [x, y, scale, opacity])

    def choose(self, decision, branch):
        btn = f'#{decision} .decision-branch-button[data-branch="{branch}"]'
        self.glide_to(f"#{decision}", at=0.12)
        self.hold(0.7)
        box = self.page.locator(btn).bounding_box()
        x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
        self.move_cursor(x, y, 0.9)
        self.hold(0.25)
        self.set_cursor(x, y, scale=0.7)
        self.page.evaluate("s => document.querySelector(s).click()", btn)
        self.hold(0.2)
        self.set_cursor(x, y)
        self.hold(0.5)
        self.set_cursor(x, y, opacity=0)
        self.cursor = None


def card(step_id):
    return f'.step-card[data-step-id="{step_id}"]'


def record(base_url, frames_dir):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=SIZE)
        page.goto(f"{base_url}/index.html?sheet=bereshit")
        page.wait_for_function("() => window.ScrollTrigger && ScrollTrigger.getAll().length > 0")
        page.evaluate("document.fonts.ready")
        # Let the manuscript pages load before they're needed.
        page.evaluate("""() => Promise.all([...document.querySelectorAll('img')].map(i =>
            i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })))""")
        page.wait_for_timeout(1500)
        cdp = page.context.new_cdp_session(page)
        page.evaluate(SETUP_JS, SLOWDOWN)

        r = Recorder(page, cdp, frames_dir)
        r.hold(1.6)                                    # title screen
        r.choose("root-fork", "creation")               # decision 1: a passage
        r.glide_to("#creation-fork", at=0.12)           # past "The Days of Creation"
        r.choose("creation-fork", "cr-1963")            # decision 2: a year
        steps = page.evaluate(
            "() => [...document.querySelectorAll('.step-card[data-section-id=\"cr-1963\"]')].map(c => c.dataset.stepId)")
        for sid in steps:                               # the verse, words lit
            r.glide_to(card(sid))
            r.hold(2.0)
        r.glide_to(card("cr-1963-codex"))               # into the manuscript
        r.hold(2.0)
        r.glide_to(card("cr-1963-days"))                # the scribe's day breaks
        r.hold(1.8)
        poster_frame = r.n                              # poster: day breaks lit on folio 1v
        r.hold(1.6)
        r.glide_to(card("cr-1963-day-6"))               # folio 2r
        r.hold(2.2)
        r.glide_to(card("cr-1963-seventh"))             # Va-yekhullu: chapter 2
        r.hold(3.8)
        browser.close()
        return poster_frame, r.video_time


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found on PATH")
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    server = subprocess.Popen([sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
                              cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    base = f"http://127.0.0.1:{port}"
    time.sleep(0.8)
    try:
        with tempfile.TemporaryDirectory() as tmp:
            frames = Path(tmp)
            poster_frame, dur = record(base, frames)
            OUT.mkdir(parents=True, exist_ok=True)
            src = ["-framerate", str(FPS), "-i", str(frames / "%05d.jpg")]
            subprocess.run(["ffmpeg", "-y", *src, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "26",
                            "-preset", "slow", "-movflags", "+faststart",
                            str(OUT / "bereshit-walkthrough.mp4")], check=True, capture_output=True)
            subprocess.run(["ffmpeg", "-y", *src, "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "38",
                            "-row-mt", "1", str(OUT / "bereshit-walkthrough.webm")], check=True, capture_output=True)
            shutil.copy(frames / f"{poster_frame:05d}.jpg", OUT / "bereshit-walkthrough.jpg")
    finally:
        server.terminate()
    for f in sorted(OUT.iterdir()):
        print(f"{f.relative_to(ROOT)}  {f.stat().st_size / 1e6:.2f} MB")
    print(f"duration {dur:.1f}s")


if __name__ == "__main__":
    main()
