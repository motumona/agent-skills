---
name: device_browser_first
description: "Start logged-in browser work on the user's own device browser, where the session already lives. Fall back to the cloud browser only when the device is unreachable."
---

# Use the logged-in browser first

## Start where the session already lives

- Start a task that needs a login on the browser on the user's own device when that browser is reachable from your current session.

- Check reachability before you start and name the browser you will use in your working notes.

- Use the cloud browser only as a fallback when the device browser is not reachable.

## Switch after one login failure

- Switch to the device browser after one login, session, or rate limit failure in the cloud browser instead of retrying the cloud browser.

- Restart the device browser when it is slow or stuck by closing every window and opening a fresh window before you retry the same step.

- Keep the work you already completed and rebuild only the step that failed.

## Say plainly when the device is unreachable

- Say plainly when the device browser is not reachable from your current channel and name what the user must do instead.

- Never claim that a login failed on the device browser when you never tried it there.

- Close a finished device browser window in the same turn and verify that it closed before you report the result.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Use a public read without a login when the task only needs public information.

- Ask the user to open the step on their own device when the device browser is unreachable and the step needs their login.
