# Oche Darts

Private Dart-Scoring-App mit Bots, Trainingsspielen, Statistik und Kamera-Erkennung (Testfunktion).

- `app.html`: Quelle der App. Daraus wird auch die Version auf claude.ai veröffentlicht.
- `build.py`: baut daraus `index.html` für GitHub Pages und aktualisiert die Version in `sw.js`.
- `manifest.webmanifest`, `sw.js`, `icon-*.png`: machen die App installierbar und offline nutzbar.

Nach einer Änderung an `app.html`:

```
python build.py
git add -A
git commit -m "Update"
git push
```

Alle Spieldaten (Statistik, Einmessung der Kamera) bleiben nur auf dem jeweiligen Gerät im Browser gespeichert.
