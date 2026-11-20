# Web3 smart contract audit checklist

Source: Agentic Bug Hunter repo (`~/workspace/bug-hunter/docs/smart-contract-audit.md` and `bughunter/agents/web3-auditor.md`). Use this for any Solidity or Rust contract audit, including the practice repo Revert v4lend.

## Pre-dive assessment (always first)

```
1. TVL check: under $500K → too low → STOP
2. Audit check: 2+ top-tier audits (Halborn, Trail of Bits, Cyfrin, OpenZeppelin) on a SIMPLE protocol → STOP
3. Size check: under 500 lines, single A to B to C flow → minimal surface → STOP
4. Payout formula: min(10% x TVL, program_cap) → under $10K → STOP
```

Score the target if it passes:
- TVL over $10M: +2
- Immunefi Critical 50K or higher: +2
- No top-tier audit on this version: +2
- Under 30 days since deploy: +1
- Upgradeable proxies: +1
- Protocol you know well: +1
- Proceed at 6 or higher out of 10.

## 10-step audit process

1. Read the documentation. Whitepaper, README, NatSpec comments, design docs. A gap between intent and implementation is a bug.
2. Scope and line count. Clone the repo and count Solidity lines with `cloc src/ --include-lang=Solidity`.
3. Local setup. `forge build` must compile. Run `forge test` and note coverage gaps. Run `forge coverage` to find untested code paths.
4. Static analysis. Slither (93 detectors, fast), Aderyn (Rust-based, Foundry-native), Mythril (symbolic execution, slower and deeper).
5. Architecture visualization. Map contract relationships, value flows and external integrations. List privileged roles (owner, multisig, governance). Note oracle dependencies (Chainlink, Uniswap TWAP, spot price).
6. Grep surface map. Run the grep patterns below, about 15 minutes. Map external calls, access control, oracle usage and unchecked math. Rank red flags by fund proximity.
7. Checklist review. Search Solodit (solodit.cyfrin.io) for findings on similar protocol types. Use the transmissions11 solcurity checklist and the Cyfrin audit checklist.
8. Line-by-line manual review. First pass: read everything, do not investigate leads yet. Second pass: investigate suspicious areas. Focus on external and public functions, state changes, math and access control.
9. Invariant testing. Write Foundry invariants (for example total assets must equal token balance, no user can withdraw more than deposited) and run `forge test --match-test invariant_ -vvv`, or Echidna for property testing.
10. Write a Foundry proof of concept for every confirmed finding.

## Static analysis commands

```bash
# Slither, 93 detectors, fast
slither . --exclude-low --filter-paths "test|lib|node_modules"
slither . --detect reentrancy-eth,unprotected-upgrade,arbitrary-send-eth

# Aderyn, Rust-based, Foundry-native
aderyn . --output report.md

# Mythril, symbolic execution (slower, deeper)
myth analyze src/Contract.sol --max-depth 6
```

## 10 bug classes in frequency order

### Class 1: Accounting Desync (28 percent of Criticals)

Read all functions that modify balance, supply or accounting variables. For each function with an early return, check whether every state variable updated in the normal path is also updated in the early return path. If A is updated but B is not, that is a possible desync.

```bash
grep -rn "totalSupply\|totalShares\|totalAssets\|totalDebt\|cumulativeReward" contracts/
grep -rn "\breturn\b" contracts/ -B5 | grep -B5 "if\b"
```

### Class 2: Access Control (19 percent of Criticals)

The one rule: read ALL sibling functions. If `vote()` has modifiers, check `poke()`, `reset()` and `harvest()` too.

```bash
grep -rn "function vote\|function poke\|function reset\|function update\|function claim\|function harvest" contracts/ -A2
grep -rn "modifier\b" contracts/ -A8 | grep -B3 "if (" | grep -v "require\|revert"
grep -rn "function initialize\b" contracts/ -A3
grep -rn "_disableInitializers()" contracts/
```

### Class 3: Incomplete Code Path (17 percent of Criticals)

For every function pair (deposit and withdraw, place and update, create and cancel), check whether the reverse function handles all the same state changes. Check whether a partial fill refunds both ETH and ERC20.

```bash
grep -rn "safeApprove\b" contracts/
grep -rn "delete\b" contracts/ -B5
grep -rn "function deposit\|function mint\|function withdraw\|function redeem" contracts/ -A10
```

### Class 4: Off-By-One (22 percent of Highs)

Mental test for EVERY `if (A > B)` in the codebase: what happens when A equals B?

```bash
grep -rn "Period\|Epoch\|Deadline\|period\|epoch\|deadline" contracts/ -A3 | grep "[<>][^=]"
grep -rn "\bbreak\b" contracts/ -B10
grep -rn "\.length\s*-\s*1\|i\s*<=\s*.*\.length\b" contracts/
```

### Class 5: Oracle and Price Manipulation

```bash
grep -rn "latestRoundData" contracts/ -A5 | grep -v "updatedAt\|timestamp"
grep -rn "getPriceUnsafe\|getPrice\b" contracts/ -A8 | grep -v "conf\|confidence"
grep -rn "getReserves\|getAmountsOut\|slot0\b" contracts/ -A5
```

### Class 6: ERC4626 Vaults

```bash
grep -rn "function deposit\|function mint\|function withdraw\|function redeem" contracts/ -A10
grep -rn "_decimalsOffset\|_convertToShares\|_convertToAssets" contracts/
```

### Class 7: Reentrancy

```bash
grep -rn "\.call{value\|safeTransfer\|transfer(" contracts/ -B10
grep -rn "function withdraw\|function redeem\|function claim" contracts/ -A2 | grep -v "nonReentrant"
```

### Class 8: Flash Loan

Look for spot price readings that a flash loan can move.

```bash
grep -rn "getReserves\|slot0\b\|getAmountsOut" contracts/
```

### Class 9: Signature Replay

```bash
grep -rn "ecrecover\|ECDSA\.recover" contracts/ -B20
grep -rn "nonce\|_nonces" contracts/
```

### Class 10: Proxy and Upgrade

```bash
grep -rn "function initialize\b\|_disableInitializers" contracts/
grep -rn "delegatecall\b" contracts/ -B3
```

## High-value bug classes from 2024 to 2025

- ERC4626 near-empty vault manipulation (first depositor inflation, donation attack).
- EIP-2612 permit frontrun denial of service.
- Signature replay across chains (ecrecover present but no chainId is a red flag).
- ZK proof verifier bypass (unsound constraints, unconstrained witness variables, missing range checks).
- Wrong access control modifier (an `if` with no else revert instead of `require`).
- Donation attack on share price.
- Deploy script and initializer bugs.

## Attack surface mindmap by protocol type

- DEX and AMM: oracle manipulation, rounding in pool math, sandwich and frontrun, fee accounting, LP share inflation.
- Lending and borrowing: collateral valuation, liquidation logic, interest accrual rounding, flash loan to inflate collateral then borrow, ERC4626 vault share manipulation.
- Bridge and cross-chain: message replay (missing nonce or nullifier), validator or guardian set manipulation, uninitialized proxy after upgrade, cross-chain signature replay, destination execution reentrancy.
- Vault and yield: share price manipulation, ERC4626 first depositor inflation, reward accounting, withdrawal queue manipulation.
- Stablecoin: collateral depeg cascading liquidations, oracle dependence, liquidation engine rounding.
- Governance and DAO: flash loan voting, quorum manipulation, timelock bypass, token snapshot timing attack.
- ZK rollup and circuit: unsound proof constraints, unconstrained witness variables, missing range checks, exodus mode bypassing verification.

## Audit checklist (quick pass)

- Access control: every privileged function has the right modifier, initialize can run once, no missing modifier on a sibling function.
- Math and logic: rounding favors the protocol or is neutral, no unchecked arithmetic on user funds, no off-by-one on periods and deadlines.
- Reentrancy: checks-effects-interactions order everywhere, nonReentrant on withdraw, claim and redeem, no external call before state update.
- Oracle and price: no spot price as the only price source, Chainlink staleness checked, TWAP window sane, no flash-loan-movable price in a critical path.
- Token handling: fee-on-transfer tokens handled, no unsafe approve, no missing return-value check on non-standard ERC20.
- Proxy and upgrades: initializer protected, storage layout safe across upgrades, no delegatecall to an untrusted address.
- Governance: no flash loan voting, quorum reachable but not trivially manipulable, timelock enforced.

## Kill a finding when

- Defense in depth prevents the path.
- The same bug was reported in a recent audit and the fix is confirmed.
- The state update is atomic (no intermediate state is visible).
- The checks-effects-interactions order is correct everywhere reentrancy was attempted.

## Reporting format for each confirmed finding

```
CLASS: [bug class]
FUNCTION: [FunctionName() in ContractName.sol]
SEVERITY: [Critical / High / Medium]
ROOT CAUSE: [one sentence]

VULNERABLE CODE:
[exact code snippet]

IMPACT: [economic impact in $]

FIX: [exact code change]

FOUNDRY POC:
[test function stub]
```

## Decision output

```
FINDING: [class] in [function] — [severity]
CONFIDENCE: [HIGH / MEDIUM / LOW] — [reason]
RECOMMENDATION: [write Foundry PoC / investigate further / dismiss]
```
