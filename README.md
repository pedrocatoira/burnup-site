# Burn-up for Jira — website

Public site for Burn-up for Jira by Catoira Consulting Inc, served with GitHub Pages. It mirrors the layout, navigation, footer, fonts and colours of `mvp-site`.

- `index.html` is written by hand.
- Inner pages (docs, privacy, terms, security, support) are built from `_src/pages/*.html`:
  `python3 _src/build.py _src .` (run from the repo root), then commit the generated `.html` files.
- `getting-started.html` and `privacy-policy.html` are the site's earlier addresses. The build writes them as redirects to `docs.html` and `privacy.html`, so old links keep working.
- `assets/` holds the stylesheet, the self-hosted Archivo font (SIL Open Font License, see `assets/fonts/OFL.txt`) and icons (from `icons/burn-up-for-jira.png` in the app repo).
- Terms only point to Atlassian's standard end user agreement and state the governing law.

Before launch: replace the Marketplace search link in `index.html` and `_src/build.py` with the real listing URL.
