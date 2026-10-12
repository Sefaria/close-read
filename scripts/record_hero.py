"""Record the homepage hero walkthrough from the live Bereshit sheet.

Walks a real reader's path: the opening, the first decision (choose a passage),
the second (choose a year), a verse with its words lit, then the two Leningrad
Codex pages with the scribe's breaks highlighted. Re-run whenever the Bereshit
sheet or the engine changes so the video never shows a stale build.

    python3 scripts/record_hero.py        # writes assets/hero/bereshit-walkthrough.{mp4,webm,jpg}

Needs playwright (requirements-dev.txt) and ffmpeg on PATH.
"""

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

# A visible pointer: Playwright's recorder doesn't draw the mouse, and the
# decision clicks are the point of the first half.
CURSOR_JS = """
(() => {
  const c = document.createElement('div');
  c.id = '__cursor';
  c.style.cssText = 'position:fixed;left:0;top:0;width:22px;height:22px;margin:-11px 0 0 -11px;' +
    'border-radius:50%;background:rgba(139,94,60,.35);border:2px solid #8b5e3c;z-index:99999;' +
    'pointer-events:none;transition:transform .15s ease;opacity:0';
  document.body.appendChild(c);
  window.__moveCursor = (x, y, ms) => new Promise(res => {
    c.style.opacity = 1;
    const r = c.getBoundingClientRect();
    const x0 = r.left + 11, y0 = r.top + 11, t0 = performance.now();
    const ease = t => t < .5 ? 2*t*t : 1 - Math.pow(-2*t + 2, 2) / 2;
    (function step(now) {
      const t = Math.min(1, (now - t0) / ms), e = ease(t);
      c.style.left = (x0 + (x - x0) * e) + 'px';
      c.style.top = (y0 + (y - y0) * e) + 'px';
      t < 1 ? requestAnimationFrame(step) : res();
    })(t0);
  });
  window.__press = () => { c.style.transform = 'scale(.7)'; setTimeout(() => c.style.transform = '', 180); };
  window.__hideCursor = () => { c.style.opacity = 0; };
})();
"""

GLIDE_JS = """
([y, ms]) => new Promise(res => {
  const y0 = window.scrollY, t0 = performance.now();
  const ease = t => t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3) / 2;
  (function step(now) {
    const t = Math.min(1, (now - t0) / ms);
    window.scrollTo(0, y0 + (y - y0) * ease(t));
    t < 1 ? requestAnimationFrame(step) : res();
  })(t0);
})
"""


def glide_to(page, selector, ms, at=0.42):
    """Smooth-scroll so the element's top sits at `at` of the viewport height."""
    y = page.evaluate(
        "([s, at]) => { const e = document.querySelector(s); return e.getBoundingClientRect().top + scrollY - innerHeight * at; }",
        [selector, at])
    page.evaluate(GLIDE_JS, [max(0, y), ms])


def card(step_id):
    return f'.step-card[data-step-id="{step_id}"]'


def choose(page, decision, branch):
    btn = f'#{decision} .decision-branch-button[data-branch="{branch}"]'
    glide_to(page, f"#{decision}", 1400, at=0.12)
    page.wait_for_timeout(900)
    box = page.locator(btn).bounding_box()
    page.evaluate("([x, y]) => __moveCursor(x, y, 900)", [box["x"] + box["width"] / 2, box["y"] + box["height"] / 2])
    page.wait_for_timeout(450)
    page.evaluate("__press()")
    page.locator(btn).click()
    page.wait_for_timeout(300)
    page.evaluate("__hideCursor()")
    page.wait_for_timeout(1600)  # the engine's own smooth scroll to the branch


def record(base_url, video_dir):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport=SIZE, record_video_dir=str(video_dir), record_video_size=SIZE)
        page = ctx.new_page()
        start = time.monotonic()
        page.goto(f"{base_url}/index.html?sheet=bereshit")
        page.wait_for_function("() => window.ScrollTrigger && ScrollTrigger.getAll().length > 0")
        page.evaluate("document.fonts.ready")
        page.evaluate(CURSOR_JS)
        # Let the manuscript pages load before they're needed.
        page.evaluate("""() => Promise.all([...document.querySelectorAll('img')].map(i =>
            i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })))""")
        page.wait_for_timeout(1200)
        lead_in = time.monotonic() - start

        page.wait_for_timeout(1800)                       # title screen
        choose(page, "root-fork", "creation")              # decision 1: a passage
        choose(page, "creation-fork", "cr-1963")           # decision 2: a year
        page.wait_for_timeout(600)
        glide_to(page, card("cr-1963-codex"), 2200)        # into the manuscript
        page.wait_for_timeout(2200)
        glide_to(page, card("cr-1963-days"), 1600)         # the scribe's day breaks
        page.wait_for_timeout(2000)
        poster_at = time.monotonic() - start - lead_in  # poster: day breaks lit on folio 1v
        page.wait_for_timeout(1400)
        glide_to(page, card("cr-1963-day-6"), 1800)        # folio 2r
        page.wait_for_timeout(2400)
        glide_to(page, card("cr-1963-seventh"), 1600)      # Va-yekhullu: chapter 2
        page.wait_for_timeout(3800)

        video = page.video.path()
        ctx.close()
        browser.close()
        return Path(video), lead_in, poster_at


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
            raw, lead_in, poster_at = record(base, Path(tmp))
            OUT.mkdir(parents=True, exist_ok=True)
            trim = ["-ss", f"{lead_in:.2f}", "-i", str(raw), "-an"]
            subprocess.run(["ffmpeg", "-y", *trim, "-vf", "fps=30,scale=1280:-2", "-c:v", "libx264",
                            "-pix_fmt", "yuv420p", "-crf", "28", "-preset", "slow", "-movflags", "+faststart",
                            str(OUT / "bereshit-walkthrough.mp4")], check=True, capture_output=True)
            subprocess.run(["ffmpeg", "-y", *trim, "-vf", "fps=30", "-c:v", "libvpx-vp9", "-b:v", "0",
                            "-crf", "40", str(OUT / "bereshit-walkthrough.webm")], check=True, capture_output=True)
    finally:
        server.terminate()
    # Poster: the highlighted manuscript, the frame that sells it.
    mp4 = OUT / "bereshit-walkthrough.mp4"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
                               capture_output=True, text=True, check=True).stdout)
    subprocess.run(["ffmpeg", "-y", "-ss", f"{poster_at:.2f}", "-i", str(mp4), "-frames:v", "1", "-q:v", "4",
                    str(OUT / "bereshit-walkthrough.jpg")], check=True, capture_output=True)
    for f in sorted(OUT.iterdir()):
        print(f"{f.relative_to(ROOT)}  {f.stat().st_size / 1e6:.2f} MB")
    print(f"duration {dur:.1f}s")


if __name__ == "__main__":
    main()
