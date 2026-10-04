# Qubitcoin

**Client v1.0.0.** Unofficial peer-to-peer cryptocurrency. Not Bitcoin. Not the 2024 Qubitcoin (QTC) network. No premine, no sale, no admin key.

Ticker **QBIT**. Magic `QBIT`. Cap 21,000,000. Subsidy 50. Halving every 210,000 blocks. SHA-256d. secp256k1. 120s target spacing.

## Genesis work (v1.0.0)

Demo difficulty is **retired**.

| Constant | Value |
|----------|--------|
| `GENESIS_BITS` | `0x1E00FFFF` |
| Expected hashes / block | ~1.7×10⁷ |
| ~0.2 MH/s Python SHA-256d | on the order of **1 minute** per block |

Rewriting a long chain costs real time on ordinary hardware. Still far below Bitcoin mainnet; this is a public-test floor, not instant mine.

**Wipe pre-v1.0 datadirs** — they are a different chain.

```bash
python3 qubitcoin.py info
```

## Run

```bash
pip install cryptography
python3 assemble.py    # if you only have compressed parts/

python3 qubitcoin.py run --datadir node-a --port 19100 --mine
python3 qubitcoin.py run --datadir node-b --port 19101 --seed 127.0.0.1:19100
python3 qubitcoin.py status --datadir node-a
```

`--seed` / `--peer` take `host:port` (repeatable). `DEFAULT_SEEDS` is empty by default.

Mining prints progress every 1M hashes. First genesis often takes ~1 minute.

## What v1.0.0 changed

- Harder genesis (`0x1E00FFFF`)
- Unlimited nonce search + progress logs
- `--seed` bootstrap flag
- `info` command (expected work, seeds)
- Client version banner `1.0.0`

## Safety

Do not store meaningful value. Keep `wallet.json` private.
