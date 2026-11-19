---
name: makefun_entry_checks
description: "Build and submit a make.fun bounty entry so the session authorship and grader checks pass, when a competition is open."
---

# Build make.fun entries the checker accepts

## Start the build only after the competition opens

- Start a fresh build session only after the competition opening time has passed.

- Do not write entry code in a staging session before opening and then move it in after opening.

- Do not read staging files in the build session, because lines read from staging count as read rather than authored.

- Schedule the build to start at opening when the competition opens later, and rebuild from scratch if an early draft already exists.

## Author every submitted file in the build session

- Rewrite each source file fresh in the build session instead of copying a staged copy into it.

- Do not submit a file that is identical to the starter file, because the checker counts zero authored lines for it.

- Keep the authored share high enough that thinking_reproduces reaches at least 30 percent, and aim well above that threshold.

- Run the local check and the server check before you submit, and submit only when the checks show zero failures.

## Do not import files while the recorder runs

- Do not run rsync, cp, clone or download commands while the recorder runs.

- Treat a file brought in by such a command as read rather than authored, because the checker counts its lines as imported.

- Author an edit in every submitted file during the recorded session, so each file carries authored lines of its own.

- Rebuild the affected work in a fresh recorded session when an import already ran, instead of submitting the tainted recording.

## Keep the grader run intact

- Test the entry so it runs to completion with no network access and with its program folder read only.

- Keep the run short enough for the grader time limit and confirm the program exits with a zero status.

- Empty the output directory by removing its contents only, and never delete the output directory itself.

- Do not call a helper that removes the output directory, because the grader mounts that directory and the removal fails with a permission error.

## Submit only after the checks pass

- Read the full check result before you submit and fix every failing check first.

- Do not submit after a failed check in the hope that the server will pass it, except for the two artefact failures named below.

- Check that every builder session was recorded before you submit, and re-record any builder whose work is missing from the recording.

- Treat a local thinking_priced failure and a local transcripts_run_record failure as artefacts for a Muse session, because the local check takes no usage file and the seal carries the usage rows and the run record.

- Match a usage row to its session by the full agent id from the first line of the session file.

- Verify the seal carries the usage rows and the run record before you submit when those two local checks fail.

- Submit when the seal check passes and no other local check fails, and do not discard a build for those two local failures alone.

- Report the practice score and the prize floor side by side when both exist, and say plainly when the practice score is below the floor.

- Store the claim code in a protected file and never print it in a message or a log.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [make.fun](https://make.fun/) for the list of open competitions with opening time, closing time and prize. Carry the competition id and its opening time into the build plan and verify the opening time on the site before you start.

## Alternatives for better results

- Build the entry in one session from opening to submission when the window allows it, instead of splitting the work across staged sessions.

- Keep a staged draft only as a private note of ideas, and rewrite the code from those ideas in the build session.

- Pick a competition whose grader needs no paid key or paid credit when no such key is available, and skip it plainly instead of submitting an entry that cannot be graded.
