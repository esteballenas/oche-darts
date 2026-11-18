"""Baut aus app.html (Quelle, auch für das claude.ai-Artifact) die installierbare index.html für GitHub Pages.

Aufruf im Ordner Dart-App:  python build.py
"""
import hashlib
import io
import pathlib
import re

here = pathlib.Path(__file__).parent
src = (here / "app.html").read_text(encoding="utf-8")

head = (
    '<!doctype html><html lang="de"><head>'
    '<link rel="manifest" href="manifest.webmanifest">'
    '<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">'
    '<link rel="apple-touch-icon" href="icon-192.png">'
    '<meta name="mobile-web-app-capable" content="yes">'
    '<meta name="apple-mobile-web-app-capable" content="yes">'
    '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
    "</head><body>"
)
html = head + src + "</body></html>"
(here / "index.html").write_text(html, encoding="utf-8", newline="\n")

# Service-Worker-Version an den Inhalt koppeln, damit Handys Updates sicher bekommen
digest = hashlib.sha1(html.encode("utf-8")).hexdigest()[:10]
sw_path = here / "sw.js"
sw = sw_path.read_text(encoding="utf-8")
sw = re.sub(r"const VERSION = '[^']*';", f"const VERSION = 'oche-{digest}';", sw)
sw_path.write_text(sw, encoding="utf-8", newline="\n")

print(f"index.html gebaut ({len(html) // 1024} KB), Version oche-{digest}")
