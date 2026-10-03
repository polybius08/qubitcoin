#!/usr/bin/env python3
"""Reassemble qubitcoin.py from compressed parts."""
import base64
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
parts_dir = root / "parts"
chunks = []
i = 0
while True:
    p = parts_dir / f"w{i}.txt"
    if not p.exists():
        break
    chunks.append(p.read_text().strip())
    i += 1
if not chunks:
    raise SystemExit("no parts/w*.txt found")
b64 = "".join(chunks)
out = root / "qubitcoin.py"
out.write_bytes(zlib.decompress(base64.b64decode(b64)))
print(f"wrote {out} ({out.stat().st_size} bytes)")
