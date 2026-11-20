---
name: remotion-skills
description: Create, edit, and render animated videos with Remotion (React-based programmatic video). Use whenever the user asks to make an animated video, a promo/intro/title card, captions/subtitles on video, a map animation, or to render/export a video from code. This is a local hub for the official Remotion Agent Skills (github.com/remotion-dev/skills, installed verbatim, version 4.0.543) — read the matching sub-skill below before doing the work.
---

# Remotion Skills (hub)

Local hub for the **official Remotion Agent Skills** by the Remotion team.
Source: https://github.com/remotion-dev/skills — installed verbatim via `git clone --depth 1` into this folder on 2026-11-16. The 13 real skills live in `skills/<name>/SKILL.md` with their own `agents/` and `assets/` folders. Do not edit the vendored files; this hub file is the only local addition.

## How to use

1. Pick the sub-skill that matches the task from the list below.
2. Read that sub-skill's `SKILL.md` first, then follow it. It contains the real instructions.
3. If unsure which one fits, start with `remotion-best-practices` — it is the router for all the others.
4. Commands in the sub-skills (e.g. `npx remotion studio`, `npx remotion render`, `npx create-video@latest`) are only run when the user actually asks to build/preview/render a video. Never run them speculatively.

## Sub-skills

| Skill | When to use |
|---|---|
| `skills/remotion-best-practices/SKILL.md` | Router for all Remotion skills; use when unsure which specific skill fits. |
| `skills/remotion-create/SKILL.md` | Create a new Remotion project or composition from scratch. |
| `skills/remotion-markup/SKILL.md` | Writing Remotion React markup: compositions, animations, layout, typography, media, effects, audio, fonts, timing. |
| `skills/remotion-studio/SKILL.md` | Launch the Studio to preview a video. |
| `skills/remotion-render/SKILL.md` | Render a composition into a video file or a still image. |
| `skills/remotion-maps/SKILL.md` | Map animations: static maps, animated routes and markers, geographic explainers, Mapbox/MapLibre/MapTiler/GeoJSON, 3D flyovers with CesiumJS. |
| `skills/remotion-captions/SKILL.md` | Captions and subtitles (including transcription and SRT import). |
| `skills/remotion-saas/SKILL.md` | Architecture for Remotion-powered apps and product integrations. |
| `skills/remotion-interactivity/SKILL.md` | Making Remotion code editable/selectable in the Studio. |
| `skills/remotion-docs/SKILL.md` | Search the Remotion docs and fetch any page as Markdown for current API references. |
| `skills/remotion-license/SKILL.md` | Remotion license information, FAQs, terms, where to buy. |
| `skills/remotion-upgrade/SKILL.md` | Upgrade Remotion, related packages, and these installed skills. |
| `skills/remotion-multimedia/SKILL.md` | Browser-based multimedia handling with Mediabunny (audio/video durations and dimensions). |

## Notes and limits

- Remotion renders with a bundled headless browser; rendering needs a project scaffolded first (`remotion-create`) and can take a while on this VM (1.5 shared CPUs).
- The Studio is a local web UI for previewing — it is not a video editor with a timeline GUI.
- This hub covers programmatic video only. The other 17 items from the same X post are plain libraries/tools, not Agent Skills, and were deliberately NOT installed as fake skills (see the install report for the full list).
