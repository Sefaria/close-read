import socket
import subprocess
import sys
import time
import urllib.request

import pytest

from sheetmodel import ROOT

VIEWPORTS = {
    "desktop": {"width": 1440, "height": 900},
    "mobile": {"width": 390, "height": 844},
}


def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session")
def base_url():
    """Serve the repo root the same way local dev does (python -m http.server)."""
    port = _free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    url = f"http://127.0.0.1:{port}"
    for _ in range(100):
        try:
            urllib.request.urlopen(url + "/index.html", timeout=1)
            break
        except OSError:
            time.sleep(0.05)
    else:
        proc.kill()
        raise RuntimeError("http.server did not start")
    yield url
    proc.terminate()
    proc.wait(timeout=5)


@pytest.fixture(scope="session")
def browser():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        yield b
        b.close()


@pytest.fixture(params=list(VIEWPORTS), ids=list(VIEWPORTS))
def viewport(request):
    return request.param


@pytest.fixture
def page(browser, viewport):
    """A fresh page at the viewport, with console errors, page errors and failed
    requests collected on page.problems."""
    ctx = browser.new_context(
        viewport=VIEWPORTS[viewport],
        reduced_motion="reduce",
        is_mobile=viewport == "mobile",
        has_touch=viewport == "mobile",
        device_scale_factor=2 if viewport == "mobile" else 1,
    )
    pg = ctx.new_page()
    pg.problems = []
    pg.on("console", lambda m: m.type == "error" and pg.problems.append(f"console error: {m.text}"))
    pg.on("pageerror", lambda e: pg.problems.append(f"page error: {e}"))
    pg.on("requestfailed", lambda r: pg.problems.append(f"request failed: {r.url} ({r.failure})"))
    pg.on("response", lambda r: r.status >= 400 and pg.problems.append(f"HTTP {r.status}: {r.url}"))
    yield pg
    ctx.close()
