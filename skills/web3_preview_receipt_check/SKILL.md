---
name: web3_preview_receipt_check
description: "Verify a short-lived wallet preview and its on-chain receipt before reporting a Web3 result."
---

# Web3 preview and receipt check

## Treat a preview as a short-lived draft

- Show the preview with its expiry time and exact parameters before asking for approval.

- If the preview expires, discard it and build a new preview and ask for approval of the new preview only.

## Verify the calldata before the preview

- Never type a hex amount by hand. Format every amount with code in zero padded 64 character form.

- Verify every amount field by checking that the integer value of the hex equals the intended amount in raw units before you build a preview.

- Compare the decoded price with the intended price in BNB and in USDT and show both in the preview.

- Check the function selector against the intended function signature before you build a preview.

## Check Element fees before a listing preview

- Before you build an Element sell order preview, run the Element fees read for the collection contract using `~/workspace/custom-connectors/custom.element/bin/element.py fees`.

- Do not rely on an on-chain helper fees check alone, because it does not catch collection royalty.

- Read royalty and protocol fee points and addresses from the fees response and use those values when you build the order.

- Compute net proceeds after royalty and protocol fee and show the net amount in BNB and in USDT in the preview.

- Stop when the fees read fails or royalty is unknown, and never report royalty as zero from a helper sweep alone.

## Verify the collection before you trust a floor price

- Never trust a floor price from a collection page you reached by collection name or slug alone.

- Read the contract address shown on the collection page and compare it character for character with the contract address of the NFT you hold.

- Treat the floor price as unverified when the two addresses differ, and report the collection as having no verified floor instead of reporting the other collection floor price.

- Use a floor price in a listing preview only after the two contract addresses match, and show the matched contract address in the preview.

- When the Element API quota is exhausted, fall back to an on-chain owner check and leave the floor unverified instead of guessing it from a slug page.

## Check a wallet send before you attempt it

- Compute the EIP-55 checksum of the recipient address with code before you attempt a wallet send.

- Never attempt a send to an all-lowercase address, because the wallet rejects it as an invalid address.

- Confirm the recipient is already in the Binance address book before you attempt the send.

- If you cannot confirm address book membership, stop and ask the user to add the address in the Binance app first instead of attempting the send.

- Never retry a send after an invalid address error or an address book error until you have fixed the checksum or the address book step that caused it.

## Name what a number counts before you report it

- Read the label the source gives a number before you report it, and report the number with that label.

- Report a paid count only when the source counts paid items, and report a total count as a total count.

- Report a daily cap as a cap, and report an available balance only after you have read the available balance field itself.

- When the label is unclear, verify the figure from a live source or on-chain state before you report it as verified.

- Report a figure as unverified when you cannot confirm what it counts, instead of presenting it as a confirmed balance or count.

## Verify the receipt, not the simulation

- Treat every simulated result as an estimate, including any simulated token identifier.

- After execution, read the transaction receipt and its transfer logs before reporting ownership or a result.

## Report only the step the receipt proves

- Report a mint only after receipt status shows success and the transfer log names the token.

- Use VERIFIED only for a step with receipt evidence, PENDING for a submitted but unconfirmed step, and BLOCKED for a step that cannot proceed.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Build the preview only when the user is ready to approve it.
