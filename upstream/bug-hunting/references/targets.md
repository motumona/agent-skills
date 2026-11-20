# Bug bounty targets (verified 12 Nov 2026 from the official program pages)

Full research file: `~/workspace/bug-bounty/bug-bounty-research-2026-11-12.md`. Re-check each live scope page before a hunt, because scope changes.

## Priority 1: Ethereum Foundation — up to $1,000,000 — OPEN

- Page: https://ethereum.org/bug-bounty/
- Status: open for submissions, ongoing program, no closing date.
- Submit: form at https://bbp-form.ethereum.org (all reports must go through this form).
- A proof of concept is mandatory. Duplicate or already-known reports are not eligible. Public disclosure without agreement makes a report ineligible.
- Identity proof (KYC) is required. No payouts to people or countries on sanctions lists. Testing only on local testnets, never break the law or compromise other people's data.
- EF employees, contractors, grantees and in-scope client team members get points only, no money, during the relationship and for 90 days after it.

### In scope
- Protocol specifications (consensus, wire and p2p protocols, proof of stake).
- Execution layer clients: Besu, Erigon, Ethrex, Geth, Nethermind, Reth.
- Consensus layer clients: Grandine, Lighthouse, Lodestar, Nimbus, Prysm, Teku.
- Solidity and Vyper compilers.
- Beacon Chain Deposit Contract.
- Dependencies: C-KZG-4844 and Go-ETH-KZG.
- Glamsterdam upgrade: specs and EIPs already in scope with a 0.5x multiplier now, 2.0x from 24 hours after the Sepolia upgrade epoch finalizes until the Hoodi upgrade, 1.5x from Hoodi until one week before the mainnet upgrade. The multiplier is set by the submission date, not the discovery date. Low Glamsterdam findings are not paid during the 0.5x window.

### Out of scope
- Infrastructure bugs (webpages, DNS, email).
- ERC-20 contract bugs.
- ENS bugs.
- Vulnerabilities that need a publicly exposed API (JSON-RPC, Beacon API). EngineAPI is trusted.
- Typos, tests, high-effort single-peer DoS, publicly known issues, anything with no direct impact on Ethereum mainnet.

### Payouts by severity
- Low up to $2,000: slash more than 0.01 percent of validators, split more than 0.01 percent of the network, or bring down more than 0.01 percent of the network with one packet or onchain transaction.
- Medium up to $10,000: slash more than 1 percent, split more than 5 percent, or bring down more than 5 percent.
- High up to $50,000: slash more than 33 percent, split more than 33 percent, or bring down more than 33 percent with one onchain transaction.
- Critical up to $1,000,000: slash more than 50 percent, mint unlimited finalized ETH, steal ETH from all EOAs, burn ETH from all EOAs, or take down the whole network with one transaction that crashes all clients.

### Repos to audit (verified)
- Geth: https://github.com/ethereum/go-ethereum (Go)
- Reth: https://github.com/paradigmxyz/reth (Rust)
- Nethermind: https://github.com/NethermindEth/nethermind (C#/.NET)
- Besu: https://github.com/hyperledger/besu (Java)
- Lighthouse: https://github.com/sigp/lighthouse (Rust)
- Prysm: https://github.com/OffchainLabs/prysm (Go)
- Lodestar: https://github.com/ChainSafe/lodestar (TypeScript)
- Nimbus: https://github.com/status-im/nimbus-eth2 (Nim)
- Teku: https://github.com/ConsenSys/teku (Java)
- Erigon (Go), Ethrex (Rust), Grandine (Rust) — also in scope.
- Specs: https://github.com/ethereum/consensus-specs and https://github.com/ethereum/execution-specs
- Compilers: https://github.com/ethereum/solidity (C++), https://github.com/vyper-ethereum/vyper (Python)

### Where to start
- One client in a language you know well (Reth in Rust, or Geth in Go), or the fresh Glamsterdam specs and EIPs.

## Priority 2: HyperLiquid — up to $1,000,000 — OPEN

- Page: https://hyperliquid.gitbook.io/hyperliquid-docs/bug-bounty-program
- Status: open, ongoing program, no closing date on the official page.
- Submit: email bugbounty@hyperfoundation.org with the report, detailed reproduction steps and a proof of concept. First report wins. Rewards are paid in USDC on Hyperliquid.
- Requires KYC/KYB compliance and the ability to receive USDC on Hyperliquid. Keep findings confidential until authorized for disclosure. Contributors to the tested code are not eligible.

### In scope
- On mainnet, any bug that would cause an outage or logical error on nodes or API servers.
- Experimental features on testnet are not in scope unless announced in Discord or Telegram.

### Prohibited
- Testing on mainnet code. All testing must be on testnet or local forks.
- Phishing or social engineering, extended large-scale DDoS, testing third-party systems, ransom demands, public disclosure before fix and payment, doxxing, exploiting a bug for personal gain beyond the reward.

### Payouts by severity
- Critical under $1,000,000: significant loss of user funds, violation of L1 execution invariants.
- High under $50,000: network downtime that does not lead to incorrect state.
- Medium under $10,000: API server performance issues.
- No Low tier is listed.

### Not eligible
- Reports without enough detail, proof of concept or reproduction steps.
- Bugs that need highly unlikely user behavior, outdated software, root access or jailbreaking, third-party library issues with no direct HyperLiquid vulnerability, non-security bugs, or extreme unrealistic market conditions.

### Repos to audit
- Node: https://github.com/hyperliquid-dex/node — Rust (HyperCore/RustVM). Public repo is a snapshot (last change 10 Aug 2026 per the 11 Nov 2026 research note).
- SDKs: hyperliquid-python-sdk (Python), hyperliquid-rust-sdk (Rust) — MIT.
- The API server and frontend are closed source. Only the node and the SDKs can be audited publicly.

## CLOSED: Revert v4lend (Cantina) — $50,000 USDC — DO NOT CHASE

- Page: https://cantina.xyz/competitions/e275368c-547d-4d91-a418-053ad31082a8
- Status: finished. Competition ran 6 Oct to 3 Nov 2026, ended 3 Nov 2026 18:30 UTC. No submissions are possible anymore.
- Use the repo ONLY as practice material for the Web3 audit workflow. Watch Cantina for the next competition.

### Scope (practice only)
- Repo: https://github.com/revert-finance/v4lend, commit f6d0fb41b7487f60ce64e011312a956e184e2a75 — Solidity + Foundry.
- v4lend is a Uniswap v4-native lending and automation codebase: a lending vault that takes Uniswap v4 LP NFTs as collateral, a two-source oracle (Chainlink-compatible feeds with Uniswap v3 TWAP verification), a Uniswap v4 hook for on-swap automation (auto exit, auto range, auto collect, auto lend, auto leverage), standalone operator automators, vault transformers, liquidation helpers and shared swap utilities.
- In-scope files: `src/vault/V4Vault.sol`, `src/oracle/V4Oracle.sol`, `src/RevertHook.sol` and `src/hook/**`, `src/automators/**`, `src/vault/transformers/**`, `src/shared/**`.
- Out of scope: `test/`, `script/`, `docs/`; documented accepted design behaviors (whole-balance sweep accounting, AutoLend holding ERC4626 vault shares while lent, hook swaps with no default amountOutMin floor, direct non-vault range change leaving the replacement position without automation config); centralization and trusted-role assumptions; MEV, gas griefing, frontrunning; frontend and off-chain components.
- This was v4lend's first external security review, with no prior audit reports.

### Prize rules (no longer in effect)
- Total pool $50,000 USDC. Only High and Medium findings were rewarded.
- High is 10 points, Medium is 3 points, pool split proportionally by points. Duplicates shrink: each reporter gets `10 x 0.9^(n-1) / n` points.
- Mandatory proof of concept rule: every Critical, High and Medium finding needed a valid coded PoC before the competition ended.

## Target evaluation scorecard (from the repo)

Score 6 or higher out of 10 to proceed. Under 4 means skip.

| Criterion | Points | How to check |
|---|---:|---|
| Max bounty 50K or higher | 2 | Program page |
| TVL over $1M | 2 | DeFiLlama |
| Program launched under 30 days ago | 2 | Immunefi new filter |
| Custom math (AMM, vault, lending) | 1 | Read scope contracts |
| Recent code changes | 1 | `git log --oneline -20` |
| Prior audits available to read | 1 | Program page or GitHub |
| Scope includes smart contracts plus web or app | 1 | Program scope section |
| Few prior reports | 1 | Program stats |
| Protocol type you know well | 1 | Your specialization |
| Source code is public and readable | 1 | GitHub or Etherscan |

Score 6 to 8 means a good target, spend 1 to 2 days. Score 9 to 10 means excellent, spend up to 1 week.

## Hard kill signals (check first, 10 minutes)

- TVL under $500K. Even a Critical pays at most 10 percent of TVL, so the expected payout is under $50K.
- Two or more top-tier audits (Trail of Bits, Halborn, Cyfrin, OpenZeppelin) on a simple protocol. Exception: audits over 1 year old plus major code changes are still huntable.
- Protocol is simple (under 500 lines, single function flow). A simple A to B to C flow with no composability has minimal attack surface.
- Max realistic payout under $10K, calculated as min(10 percent of TVL, program cap), unless the program is brand new.
