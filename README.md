# Blockchain Development · Python

A Python and Flask learning project exploring linked blocks, hashing, proof of work and chain inspection.

**PYTHON · FLASK · BLOCKCHAIN**

## What is included

The implementation is in [blockchain.py](Module%201-Create%20Blockchain/blockchain.py). It defines an in-memory chain, block hashes, a proof-of-work routine, chain validation logic and Flask routes.

| Route | Purpose |
| --- | --- |
| `GET /get_chain` | Inspect the current in-memory chain |
| `GET /mine_block` | Invoke the proof-of-work routine |

## Getting started

Read the single-file implementation with Python and Flask in an isolated development environment. Historical dependency guidance is embedded in the file; no locked environment is included.

## Project status

Educational prototype. The mining check compares a three-character slice to a four-character target, so mining currently cannot complete. The chain is in memory; there is no distributed network, wallet or deployable cryptocurrency.

Setup commands are documented from the repository structure; execution has not been revalidated as part of this presentation update.

---

Part of [Datta Dhebe's engineering portfolio](https://github.com/DattaDhebe).
