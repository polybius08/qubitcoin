# Qubitcoin

An unofficial peer-to-peer cryptocurrency. Not Bitcoin. Not the 2024 Qubitcoin (QTC) quantum-proof-of-work network. Not the Dilithium QubitCoin fork. No premine, no sale, no admin key.

**Ticker QBIT** (not QTC). Network magic `QBIT`. Cap 21,000,000. Opening subsidy 50. Halving every 210,000 blocks. SHA-256d proof of work. secp256k1 signatures. Two-minute target.

Educational node software. Demo difficulty is easy. Do not store value.

## Get the full client

The source is stored as compressed parts (GitHub upload size limits). Assemble it once:

```bash
python3 assemble.py
```

That writes `qubitcoin.py` (~29 KB).

## Run

```bash
pip install cryptography
python3 assemble.py
python3 qubitcoin.py run --datadir node-a --port 19100 --mine
python3 qubitcoin.py run --datadir node-b --port 19101 --peer 127.0.0.1:19100
python3 qubitcoin.py status --datadir node-a
python3 qubitcoin.py upgrades
```

## Upgrades (Bitcoin 2 style)

- Relay policy: data over 80 bytes and dust rejected
- Timewarp guard from height 51
- BIP 110 reduced-data window from height 52 for 52,416 blocks
- DATUM-style pool split (pool cannot supply a template)
- Package relay, silent payments, vault clawback

## Safety

Wallet private keys (`wallet.json`) are never published. Anyone with a wallet file can spend that node's coins.
