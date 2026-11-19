---
name: single_coin_analysis
description: "Give one integrated analysis for a single coin the user names, ending in a firm verdict with entry, stop, targets and a 15 minute execution plan."
---

# Single coin analysis

## Build the technical picture

- Analyse the coin on Gate spot and futures across four timeframes in one pass.

- Read the 1D chart for trend direction first and state the trend in one sentence.

- Read the 4H chart for market structure and mark the levels that decide the bias.

- Read the 1H chart to refine the entry zone and the stop placement.

- Use the 15m chart only to time execution once the higher timeframes agree.

- Confirm the coin identity on CoinGecko before you analyse it when two coins share a ticker.

## Check derivatives and whale flow

- Read CoinGlass for total open interest and open interest per exchange.

- Read CoinGlass for funding, 24 hour liquidations and the long short ratio for takers, accounts and top traders.

- Check whale wallets through the Hyperliquid Whale Tracker and Glint and report what the wallets actually show.

- Say plainly when no whale wallet data exists and use CoinGlass position data and the Gate long short ratio as the substitute instead of inventing wallet activity.

- Never invent a whale purchase, a wallet address or a trade size.

## Check the exchange and token facts

- Read the Gate spot and futures pages for the live price and the available market.

- Read CoinGecko for market cap, fully diluted valuation, circulating supply, volume and the all time high and low.

- Compare the technical read with the derivatives read and the token facts and name any disagreement before you give a verdict.

- Check every price, level and figure against a second source when the first source looks stale or inconsistent.

## Give a firm verdict and execution plan

- Give a firm verdict of YA or TIDAK with one entry zone, one stop and at least one target.

- Give a 15 minute execution plan with a clear trigger for a pullback entry and a clear trigger for a breakout entry.

- State the condition that cancels the plan in one sentence.

- Declare a setup void when price runs through a target without touching the entry and build a fresh plan instead of defending the old entry.

- Leave execution to the user and never place an order in Gate or any other exchange.

- Never discuss open trading positions and never initiate talk about positions.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Gate](https://www.gate.io/) for spot and futures prices and the multi timeframe charts. Carry the exact coin symbol and the timeframe levels into `browser.browse` and verify the price and the levels there.

- [CoinGlass](https://www.coinglass.com/) for open interest, funding, liquidations and long short ratios. Carry the coin name and verify the totals against the per exchange breakdown.

- [CoinGecko](https://www.coingecko.com/) for market cap, fully diluted valuation, circulating supply, volume and the all time high and low. Carry the CoinGecko coin id and verify the ticker identity before you use the figures.

## Alternatives for better results

- Wait for the stated trigger instead of chasing price after it has already moved through the entry.

- Ask the user which timeframe matters most when the 1D trend and the 4H structure disagree.

- Rebuild the plan from fresh prices when the analysis is more than a few hours old.
