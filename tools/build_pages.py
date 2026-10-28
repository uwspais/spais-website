#!/usr/bin/env python3
"""Package the static site and set sharing URLs for its actual Pages address.

Uses only Python's standard library. Run from any working directory.
"""

import argparse
from html import escape
from pathlib import Path
import re
import shutil
from urllib.parse import urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = {"index.html": "assets/team-cover.jpg", "project.html": "assets/farm-2.jpg"}


def normalized_base_url(value):
    parsed = urlsplit(value)
    if (parsed.scheme not in ("http", "https") or not parsed.netloc
            or parsed.query or parsed.fragment or parsed.username or parsed.password):
        raise argparse.ArgumentTypeError("Use an absolute HTTP(S) site URL without credentials, query, or fragment.")
    return value.rstrip("/") + "/"


def with_metadata(document, base_url, filename, image):
    # Remove existing sharing URLs; the deployment determines their final host.
    document = re.sub(r'<link\b[^>]*\brel=[\"\']canonical[\"\'][^>]*>', "", document, flags=re.I)
    document = re.sub(r'<meta\b[^>]*\bproperty=[\"\']og:(?:url|image)[\"\'][^>]*>', "", document, flags=re.I)
    page_url = urljoin(base_url, "" if filename == "index.html" else filename)
    image_url = urljoin(base_url, image)
    metadata = (
        f'\n  <link rel="canonical" href="{escape(page_url, quote=True)}">\n'
        f'  <meta property="og:url" content="{escape(page_url, quote=True)}">\n'
        f'  <meta property="og:image" content="{escape(image_url, quote=True)}">\n'
    )
    if "</head>" not in document:
        raise ValueError(f"Missing </head> in {filename}")
    return document.replace("</head>", metadata + "</head>", 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True, type=normalized_base_url,
                        help="The base_url output of actions/configure-pages.")
    args = parser.parse_args()
    output = ROOT / "_site"
    # _site is generated output only; source files live at the repository root.
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    shutil.copytree(ROOT / "assets", output / "assets")
    shutil.copy2(ROOT / ".nojekyll", output / ".nojekyll")
    for filename, image in PAGES.items():
        document = (ROOT / filename).read_text(encoding="utf-8")
        (output / filename).write_text(
            with_metadata(document, args.base_url, filename, image), encoding="utf-8"
        )
    print(f"Prepared {len(PAGES)} pages in _site for {args.base_url}")


if __name__ == "__main__":
    main()
