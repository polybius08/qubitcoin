#!/bin/sh
set -e
cd "$(dirname "$0")/.."
cat parts/part0.txt parts/part1.txt parts/part2.txt parts/part3.txt > qubitcoin.py
echo "Wrote qubitcoin.py ($(wc -c < qubitcoin.py) bytes)"
