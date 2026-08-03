#!/usr/bin/env python3
"""Verify the public CCT shelf and repository interpretation surfaces."""

from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "CCT" / "v1.1a"
MANIFEST = RELEASE / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in (ROOT / "README.md", ROOT / "DISCLAIMER.md", ROOT / "ARCHIVE_STATUS.md"):
        if not path.is_file():
            fail(f"missing interpretation surface: {path.relative_to(ROOT)}")

    disclaimer = (ROOT / "DISCLAIMER.md").read_text(encoding="utf-8").lower()
    if "speculative conceptual framework" not in disclaimer:
        fail("repository-wide disclaimer does not state speculative status")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for entry in manifest["outputs"].values():
        path = RELEASE / entry["name"]
        if not path.is_file():
            fail(f"missing release file: {path.name}")
        if path.stat().st_size != entry["bytes"]:
            fail(f"size mismatch: {path.name}")
        if sha256(path) != entry["sha256"]:
            fail(f"SHA-256 mismatch: {path.name}")

    forbidden_images = [
        path
        for path in RELEASE.rglob("*")
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}
    ]
    if forbidden_images:
        fail("illustrations found in image-free release: " + ", ".join(map(str, forbidden_images)))

    docx = RELEASE / manifest["outputs"]["docx"]["name"]
    with zipfile.ZipFile(docx) as archive:
        bad_members = [name for name in archive.namelist() if name.startswith("word/media/")]
        broken = archive.testzip()
    if bad_members:
        fail("embedded DOCX media remain: " + ", ".join(bad_members))
    if broken:
        fail(f"broken DOCX member: {broken}")

    print("OK: disclaimer, archive map, hashes, image-free release, and DOCX package")


if __name__ == "__main__":
    main()
