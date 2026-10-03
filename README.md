# Qubitcoin

An unofficial peer-to-peer cryptocurrency. Not Bitcoin. Not the 2024 Qubitcoin (QTC) quantum-proof-of-work network. Not the Dilithium QubitCoin fork. No premine, no sale, no admin key.

Ticker QBIT, so it is not QTC. Network magic `QBIT`. Cap 21,000,000. Opening subsidy 50. Halving every 210,000 blocks. SHA-256d proof of work. secp256k1 signatures. Two-minute target.

## Run

```bash
python3 qubitcoin.py run --datadir node-a --port 19100 --mine
python3 qubitcoin.py run --datadir node-b --port 19101 --peer 127.0.0.1:19100
python3 qubitcoin.py status --datadir node-a
```

The node also carries the Bitcoin 2 upgrades. Relay policy drops data over 80 bytes and dust. From height 51 a retarget cannot timewarp. From height 52 the BIP 110 reduced-data window runs for 52,416 blocks; earlier coins stay spendable. A DATUM pool can split a reward and cannot supply a template. Package relay, silent payments, and vault clawback are in the client.

```bash
python3 qubitcoin.py upgrades
```
