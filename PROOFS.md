# A sharp fourteen-ply obstruction to fixed pairing play

Cells have columns 0,…,W−1 and rows 1,…,H, counted from the bottom. Gravity permits only the lowest empty cell of a column. Four consecutive stones horizontally, vertically, or diagonally win. Ply one is the first player's opening at column q. Thereafter the first player follows a fixed perfect matching on the remaining cells, immediately claiming the mate of each second-player move.

**Universal legality** means this reply is legal against every legal sequence of initiating moves, even if play is conceptually continued after a win. No adaptive rematching is permitted.

## Lemma 1 — gravity-chain structure

For an arbitrary disjoint union of chains, a universally legal perfect matching decomposes chains into singleton chains tiled by consecutive pairs, and pairs of chains whose first k cells are matched across at equal ranks, followed by consecutive internal pairs in their remaining tails.

**Proof.** At any completed-round state consider a minimal remaining cell a. Its mate must either be the next cell of its chain or a minimal cell of another chain: these are exactly the cells made legal or already legal after a. If it is the next cell, that two-cell round can be performed and removed. If minimal cells a,b in distinct chains are matched across, they can be removed together. An internal pair can never be followed by a cross-pair: advance the internally paired chain in complete rounds while leaving the other chain at its earlier front; at the first subsequent cross-pair, the mate is blocked. Similarly, after one cross-pair, a chain cannot switch partners: advance the original two-chain component to the first switch while leaving the new partner behind; either the switched reply or a subsequent reply to the abandoned front is blocked. Equivalently, apply Theorem 1 of Prerequisite Pairings: the external predecessor-block sets at the two endpoints must agree. In a chain those sets are nested prefixes. For a cross-block, equality forces the prefixes to contain exactly the same preceding blocks, so they consist only of earlier cross-blocks between these same chains. An internal block occurring in either prefix has both endpoints in only one chain and cannot appear in the other prefix. Thus every cross-block belongs to a common initial cross-prefix, before any internal blocks, and every remaining internal block is adjacent. This also proves the claimed decomposition. Conversely each displayed component has immediately legal replies, directly by its fronts. ∎

After an opening on odd W,H, the opening column has even residual length H−1, while all others have odd length H. Thus the opening column is internally tiled, and the other columns pair with odd cross-prefix lengths k; their tails tile internally. Different parity prevents the opening column from having a cross-prefix with any other column.

## Lemma 2 — paired path coloring

For odd N≥5, a distinguished vertex q of a path, and any perfect matching M on the other vertices, there is a red/blue coloring with q red, opposite colors at every M edge, and no monochromatic four consecutive vertices.

**Proof.** Construct a second matching G on the vertices except q. If q is even, pair adjacent vertices separately on either side. If q is odd, pair q−1 with q+1, then pair adjacent vertices in the remaining left and right intervals. Every four-vertex interval contains a whole G edge: away from q this follows from consecutive pairing; an interval crossing q either contains the bridge (in the odd case) or a consecutive pair on one side. The union of two perfect matchings is a disjoint union of alternating even cycles, allowing doubled edges. Two-color each component and color the isolated q red. Every G edge is bichromatic, so every four-vertex interval is bichromatic. ∎

## Theorem 3 — universal fourteen-ply counterattack

For every odd W,H≥5, every universally legal fixed matching response policy for the first player admits a second-player win by ply 14.

**Proof.** Use Lemma 1. If any cross-prefix has k≥3, the second player claims the first four cells of one of its columns. The first three replies lie in the partner column. Before the fourth move the first player has only its opening plus three stones stacked in that partner column, so has no four. The second player wins vertically at ply 8 (the fourth reply is irrelevant).

Otherwise all k=1. Apply Lemma 2 to the bottom-row column matching with opening q red. Choose any interval T of four columns containing q. Activate only the column pairs meeting T\{q}: for each, the second player claims its blue bottom cell and the first player replies at its red mate. Let ℓ be the number of activated pairs; ℓ≤3. Both bottom ownership sets are subsets of the corresponding global color classes, so neither contains four consecutive cells. All bottoms in T are now filled.

The second player next claims row 2 in each of the four columns of T. Every forced reply is row 3 of that same column. Before the last attacking move, the first player has at most three row-3 stones, no row-2 stones, and no stones above row 3. It therefore cannot have a horizontal four in row 3, nor any vertical or diagonal four; the bottom row was already safe. The second player wins horizontally in row 2 on its fourth such move. This occurs at ply 1+2ℓ+7=8+2ℓ≤14. ∎

## Theorem 4 — sharpness

The bound 14 cannot be improved uniformly for this class of policies.

**Proof.** Take W=7 and any odd H≥5. Open at q=3 and pair bottom columns (0,4),(1,5),(2,6). Above the bottom, tile every column with pairs (row 2,row 3),(row 4,row 5), etc. The opening column has the same vertical tiling after its opening. This is universally legal.

The second player never owns any odd row at least 3. Every vertical or diagonal four contains such a row, so any second-player win must be horizontal. Every bottom interval of length four includes the first-player opening at column 3, excluding a bottom win. Every other horizontal winning line must be on an even row. Every four-column interval contains column 3 and three other columns in three distinct bottom matching pairs (the pair endpoints differ by four). Reaching an even row in those three columns requires three separate second-player bottom moves. The horizontal winning line requires another four second-player moves above the bottom. At least seven second-player moves are necessary: the earliest possible win is ply 14. Theorem 3 attains it. ∎

## Computational evidence and limits

`verify.py` checks all 11,460 distinguished-vertex/matching instances of Lemma 2 for N=5,7,9,11. It then performs independent breadth-first grid exploration of all legal second-player choices against the sharpness policy on 7×5, terminating branches when either player wins. The earliest second-player win is ply 14. This finite search checks sharpness for the example, not the universal theorem by itself.

This is an obstruction to a precisely restricted strategy class. It neither solves unrestricted 9×9 Connect Four nor establishes a game-theoretic outcome from its empty board. The alternating-cycle trick and pairing strategies have classical antecedents; priority for this exact bound remains unverified.
