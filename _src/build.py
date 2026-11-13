#!/usr/bin/env python3
"""Builds the inner pages of the Burn-up for Jira site from content fragments.

Usage: python3 build.py <src_dir> <site_dir>
Each fragment file in <src_dir>/pages/*.html starts with three header lines:
  title: Page title
  description: Meta description
  lede: One-line intro under the page heading
followed by a blank line and the article HTML.
"""
import pathlib
import sys

MARKETPLACE_URL = "https://marketplace.atlassian.com/search?query=Burn-up%20for%20Jira"  # replace once listed

NAV = [("docs.html", "Docs"), ("index.html#pricing", "Pricing"), ("security.html", "Security"), ("support.html", "Support")]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Burn-up for Jira</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="./"><img src="assets/icon.png" alt="" width="36" height="36">Burn-up for Jira</a>
    <nav class="site-nav" aria-label="Main">
{nav}
      <!-- MARKETPLACE_URL: replace with the listing URL once it exists -->
      <a class="btn btn-blue" href="{marketplace}">Get it on the Marketplace</a>
    </nav>
  </div>
</header>
<main id="main">
  <div class="page-head"><div class="wrap"><h1>{title}</h1><p>{lede}</p></div></div>
  <div class="prose"><div class="wrap"><article>
{body}
  </article></div></div>
</main>
<footer class="site-foot">
  <div class="wrap">
    <div>
      <p>© 2026 Catoira Consulting Inc.</p>
      <p>Jira and Atlassian are trademarks of Atlassian Pty Ltd. Burn-up for Jira is not made or endorsed by Atlassian.</p>
    </div>
    <nav aria-label="Footer">
      <a href="docs.html">Docs</a>
      <a href="support.html">Support</a>
      <a href="security.html">Security</a>
      <a href="privacy.html">Privacy</a>
      <a href="terms.html">Terms</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""


# Earlier addresses of this site, kept alive as redirects to the page that replaced them.
REDIRECTS = {"getting-started.html": "docs.html", "privacy-policy.html": "privacy.html"}

REDIRECT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved | Burn-up for Jira</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<p>This page has moved to <a href="{target}">{target}</a>.</p>
</body>
</html>
"""


def build(src: pathlib.Path, out: pathlib.Path) -> None:
    for frag in sorted((src / "pages").glob("*.html")):
        text = frag.read_text(encoding="utf-8")
        head, body = text.split("\n\n", 1)
        meta = dict(line.split(": ", 1) for line in head.splitlines())
        current = ' aria-current="page"'
        nav = "\n".join(
            f'      <a href="{href}"{current if href == frag.name else ""}>{label}</a>'
            for href, label in NAV
        )
        html = TEMPLATE.format(
            title=meta["title"], description=meta["description"], lede=meta["lede"],
            nav=nav, marketplace=MARKETPLACE_URL, body=body.rstrip(),
        )
        (out / frag.name).write_text(html, encoding="utf-8")
        print("built", frag.name)
    for old, target in REDIRECTS.items():
        (out / old).write_text(REDIRECT.format(target=target), encoding="utf-8")
        print("redirect", old, "->", target)


if __name__ == "__main__":
    build(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
