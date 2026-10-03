#!/usr/bin/env python3
"""Bootstrap: assemble full source from parts if needed, then re-run."""
import runpy
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
marker = root / "parts" / "w0.txt"
assembled = root / ".qubitcoin_assembled"

if marker.exists() and not assembled.exists():
    # First run after clone: expand compressed parts into this file's place
    import base64
    import zlib

    chunks = []
    i = 0
    while True:
        p = root / "parts" / f"w{i}.txt"
        if not p.exists():
            break
        chunks.append(p.read_text().strip())
        i += 1
    if not chunks:
        raise SystemExit("parts/w*.txt missing; cannot assemble")
    body = zlib.decompress(base64.b64decode("".join(chunks)))
    Path(__file__).write_bytes(body)
    assembled.write_text("ok\n")
    print("Assembled full qubitcoin.py; starting node...")
    # Re-exec with same args
    sys.argv[0] = str(Path(__file__))
    runpy.run_path(str(Path(__file__)), run_name="__main__")
    raise SystemExit(0)

raise SystemExit(
    "Full source not assembled. Run: python3 assemble.py\n"
    "Or ensure parts/w0.txt ... w14.txt are present and re-run this file."
)
