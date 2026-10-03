#!/usr/bin/env python3
"""Export a guide with embedded local CSS, JavaScript and unchanged image bytes.

Canonical guides continue to use shared assets. Download this export and open
it in a web browser. Source-only file viewers will still display HTML as text.
This is not deployment.
"""
import argparse
import base64
from html import escape
from html.parser import HTMLParser
import mimetypes
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://clearwater-bay-shoot-guide.vercel.app/"


class Preview(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.parts = []

    def local_asset(self, url):
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return None
        path = (self.source.parent / unquote(parsed.path)).resolve()
        path.relative_to(ROOT)
        return path

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "link" and attrs.get("rel") == "stylesheet":
            path = self.local_asset(attrs.get("href", ""))
            if path:
                self.parts.append("<style>\n" + path.read_text() + "\n</style>")
                return
        if tag == "script":
            path = self.local_asset(attrs.get("src", ""))
            if path:
                self.parts.append("<script>\n" + path.read_text() + "\n")
                return
        if tag == "img":
            path = self.local_asset(attrs.get("src", ""))
            if path:
                mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
                data = base64.b64encode(path.read_bytes()).decode("ascii")
                attrs["src"] = f"data:{mime};base64,{data}"
        if tag == "a" and self.local_asset(attrs.get("href", "")):
            relative_page = self.source.relative_to(ROOT).as_posix()
            attrs["href"] = urljoin(SITE + relative_page, attrs["href"])
        encoded = "".join(
            " " + name if value is None else f' {name}="{escape(value, quote=True)}"'
            for name, value in attrs.items()
        )
        self.parts.append(f"<{tag}{encoded}>")

    def handle_endtag(self, tag):
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        self.parts.append(data)

    def handle_entityref(self, name):
        self.parts.append(f"&{name};")

    def handle_charref(self, name):
        self.parts.append(f"&#{name};")

    def handle_comment(self, data):
        self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.parts.append(f"<!{decl}>")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("guide", help="Guide folder relative to the repository")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    source = (ROOT / args.guide / "index.html").resolve()
    source.relative_to(ROOT)
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error("Write the temporary preview outside the repository.")
    preview = Preview(source)
    preview.feed(source.read_text())
    preview.close()
    output.write_text("".join(preview.parts))
    print(f"Preview written to {output} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
