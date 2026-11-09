# Fourteen

**[Download & run locally](LOCAL.md)** — a short guide and ready-to-run ZIP.

**A sharp fourteen-ply obstruction to fixed pairing strategies in odd-board Connect Four.**

For every odd width and height at least five, any universally legal fixed first-player matching response policy can be defeated by the second player by **ply 14**. A 7×5 example proves the uniform bound is sharp.

The proof combines a gravity-chain classification with an alternating-cycle coloring construction. It improves the earlier width-nine 16-ply obstruction and extends the result to arbitrary odd widths.

- [Definitions and complete proofs](PROOFS.md)
- [Independent shortest-win search results](evidence/verification.json)
- [Related work](REFERENCES.md) · [Research provenance](PROVENANCE.md)

## Reproduce

Python 3.10+, standard library only:

```sh
python3 verify.py
python3 attack.py
```

Also replays 2,750 constructed attacks, including 500 random all-one-prefix policies, plus the sharpness construction. Checks all **11,460** small paired-path coloring instances, then independently searches the 7×5 sharpness example using legal gravity moves and immediate win detection. The earliest second-player win is move seven, or ply fourteen. Columns in the output witness are zero-based.

## Exact scope

The first player opens, then always takes the fixed mate of the second player's move. The matching must remain legal against every legal initiating sequence, even when terminal wins are ignored for that legality definition. Adaptive policies and other strategies are outside the theorem. Unrestricted 9×9 Connect Four remains unsolved by this work.

Companion: [Prerequisite Pairings](https://github.com/rishitpradhan-gif/prerequisite-pairings), a general legality characterization for prerequisite posets.

Research direction by Rishit Pradhan; proof development and implementation were AI-assisted. Worldwide priority for the precise theorem is unverified.
