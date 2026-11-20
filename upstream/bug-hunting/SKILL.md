---
name: bug-hunting
description: "Hunt for bugs in official bug bounty programs - recon, triage, PoC, and report drafting. Authorized targets only."
---

# Bug hunting

## Set up the hunter

- Work from the cloned repo at `~/workspace/bug-hunter/` and run the CLI as `python3 -m bughunter` from that directory.

- Verify the CLI before a hunt with `python3 -m bughunter --help` and `python3 -m bughunter status`.

- Run the hunt without a configured AI provider when you only need the mechanical workflow, because the methodology, checklists, gate and report templates work with your own reasoning.

- Configure a provider only after the user approves it, because Ollama needs a local model download of about 9 GB and Groq and DeepSeek need an API key signup.

- Use the free provider order the repo documents, which is Ollama first, then Groq, then DeepSeek, then the paid providers.

- Treat the external recon tools as optional, because the CLI skips a missing tool instead of failing, and install them only when a hunt needs them.

## Pick a target and read the scope first

- Read the full program scope before you touch any asset, because one request outside scope can get the account banned.

- Start with the Ethereum Foundation program, because it is open, it has the widest scope, its code is fully open source and active, and even a Low finding pays up to 2,000 dollars.

- Hunt HyperLiquid second, because it is open and pays up to 1,000,000 dollars, but its scope is narrower, its bar is higher, and its API server is closed source.

- Do not chase the Revert v4lend prize, because that competition closed on 3 November 2026, and use its repo only as practice material for the Web3 audit workflow.

- Score a new target with the evaluation scorecard in `references/targets.md` and proceed only at 6 or higher out of 10.

- Stop at a hard kill signal, which is TVL under 500K, two or more top-tier audits on a simple protocol, a protocol under 500 lines with a single flow, or a realistic max payout under 10K.

- Never test HyperLiquid on mainnet code, because the program requires testnet or local forks for testing.

- Re-check the live scope page before each hunt, because scope changes and a closed program stays closed.

## Run the hunt

- Follow the loop of scope, recon, hunt, validate and report, and keep a lead board so no lead is lost.

- Run recon before hunting, which means subdomain enumeration, live host probing, URL crawling and a nuclei sweep, then rank the surface by value.

- Keep notes in the target session file with interesting leads, dead ends, anomalies, time-boxed rabbit holes and confirmed bugs, because memory carries patterns to the next target.

- Apply the 5-minute rule and move on when a lead shows no progress after 5 minutes.

- For a smart contract target, follow the 10-step audit process in `references/web3-audit-checklist.md`, which is read the docs, scope and count lines, build and test locally, run static analysis, map the architecture, grep the surface, review the checklist, read line by line, test invariants and write a Foundry proof of concept.

- Hunt the 10 Web3 bug classes in frequency order, which is accounting desync, access control, incomplete code path, off-by-one, oracle manipulation, ERC4626 share inflation, reentrancy, flash loan attack, signature replay and proxy or upgrade issues.

- Ask whether an attacker can do this right now, because a theoretical bug with no working proof of concept is wasted time.

## Validate before you report

- Run the 7-Question Gate on every finding before you write a report, and kill the finding at the first question that answers no.

- Ask the seven questions in order, which are can an attacker do this right now with a real request, is the impact type accepted by the program, is the asset in scope and owned by the target, does it work without privileged access, is it not already known or documented, can the impact be proved beyond technically possible, and is it not on the never-submit list.

- Kill a finding on the never-submit list unless you can chain it into a real impact, because a weak report hurts the validity ratio.

- Run the 4 gates after the seven questions pass, which are a 30 second confirmation check, a 2 minute impact check, a 5 minute duplicate search and a 10 minute report readiness check.

- Downgrade the severity when the impact is real but smaller than claimed, instead of killing a valid bug.

## Write the report

- Write the report only after validation passes, and use the title formula of bug class plus endpoint or function plus impact.

- Calculate the CVSS score and include the exact reproduction steps, the expected versus actual behavior, the impact in money or users affected, and the recommended fix.

- Use the platform format the program wants, which is HackerOne or Bugcrowd for web targets, Immunefi for smart contracts and the Cantina format with a coded proof of concept for a competition.

- Submit only after the user approves the exact report text, because a submission is an external action that cannot be undone.

- Send a HyperLiquid report to bugbounty@hyperfoundation.org, and send an Ethereum Foundation report through the submission form at bbp-form.ethereum.org.

## Use the background assistants as reviewers

- Hand a finding or a code snippet to the background assistants for a second opinion, because a fresh read catches a wrong assumption.

- Route honesty-sensitive checks through Qwen or DeepSeek on APInex, because Gemini once invented a fact in a test and must not be the only reviewer for a claim.

- Keep assistant answers as unverified drafts and check them yourself before you use them in a report.

- Never send a secret, a wallet key, a seed phrase or personal data through any assistant gateway.

## Hard limits

- Test only inside an approved bug bounty scope, and stop the moment a target is out of scope.

- Never submit a bug, register for a program or pay for a tool or key without the user approving that exact step first.

- Never put a secret, a key, a token or a password into the skill, a report or a command.

- Never use a finding for personal gain outside the bounty program, and never disclose a bug publicly before it is fixed and paid.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for reading a target repository, its issues and its pull requests when you check for known bugs and prior audits.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Agentic Bug Hunter](https://github.com/awarexone/Agentic-Bug-Hunter) for the repo, the CLI, the agents and the docs. Clone it to `~/workspace/bug-hunter/` and read its README and SKILL.md before a hunt.

- [Ethereum Foundation bug bounty](https://ethereum.org/bug-bounty/) for the in-scope clients, compilers and specs and the submission form. Carry the out-of-scope list into the hunt and verify it on the live page.

- [HyperLiquid bug bounty](https://hyperliquid.gitbook.io/hyperliquid-docs/bug-bounty-program) for the scope, the submission email and the severity payouts. Carry the scope rules into the hunt and verify them on the live page.

- [Revert v4lend competition](https://cantina.xyz/competitions/e275368c-547d-4d91-a418-053ad31082a8) for the practice scope files and the commit hash. The competition is closed, so use it for training only.

## Alternatives for better results

- Start with one Ethereum client in a language you know well, such as Reth in Rust or Geth in Go, or start with the fresh Glamsterdam specifications, because a narrow start beats a shallow scan of the whole scope.

- Chain a weak finding into a stronger one before you submit it, because a chained impact often moves a finding from the never-submit list to a paid severity.

- Search disclosed reports for the same protocol type before you hunt, because a known pattern in a new codebase is the fastest way to a valid finding.

- Practice the full Web3 audit workflow on the closed Revert v4lend repo first, because its scope is small and clear and a first review means no prior audit to compete with.
