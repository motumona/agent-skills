---
name: verify_before_reporting
description: "Re-check delegated, browser and scheduled-job results from a live source before reporting them, and label anything unrechecked as unverified."
---

# Verify worker results before reporting them

## Re-check the key figures yourself

- Open the live source yourself before you report a figure that came from a delegated agent, a browser task, a scheduled job or a cron worker.

- Compare each key figure against the live source, and use the live figure when the two differ.

- Treat a worker report as a lead to check, and never present its figures as verified facts on the strength of the report alone.

- Re-check balances, counts, scores and completion states, and re-check any figure the user will act on first.

## Say plainly when you have not verified a figure

- Label a figure belum terverifikasi when you could not re-check it, and keep that label attached to the figure in the report.

- Say what you still need to check when a figure is unverified, and check it before you repeat the figure as fact.

- Never soften the label by presenting an unverified figure beside verified ones without marking which is which.

## Keep the check proportional to the risk

- Spend the most effort on figures that change a decision, a balance or a claim of success.

- Accept a single live re-check as enough when it confirms the key figures, and do not repeat the whole worker run to confirm a low-stakes detail.

- Record the live source and the time of your re-check when the report may be read later.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the worker to include the live source and the exact figure it read, so your re-check starts from the same place.

- Report a partial result with its verified figures and its unverified figures marked, instead of waiting for a full re-check when the user needs the verified part now.
