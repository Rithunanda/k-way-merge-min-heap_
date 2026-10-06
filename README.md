# K-Way Merge using Min Heap vs Pairwise Merge

Merging already-sorted transaction lists in a financial system.

```
L1 = 10, 30, 50, 70
L2 = 20, 40, 60, 80
L3 = 15, 35, 55, 75
```

## Files

| File | Purpose |
|---|---|
| `min_heap.py` | Array-based Min Heap that counts comparisons |
| `kway_merge.py` | (a) K-way merge using the Min Heap, prints heap state at every step |
| `pairwise_merge.py` | (b) Pairwise merge: (L1+L2) then (result+L3) |
| `compare.py` | (c) Runs both approaches, compares counts, and tests scaling with k |
| `output_*.txt` | Saved program output |

## How to run

```bash
python3 kway_merge.py
python3 pairwise_merge.py
python3 compare.py
```
Requires Python 3 only (no external libraries).

## (a) K-way merge with Min Heap
Each list is a Python list. The heap stores `(value, list_id, index)` and holds at most one element per list, so its size is at most k.
1. Insert the first element of every list.
2. Extract the minimum, append to output, push the next element from the same list.
3. Repeat until the heap is empty.

Output: `10, 15, 20, 30, 35, 40, 50, 55, 60, 70, 75, 80`

Initial heap `[10, 20, 15]`, then `[15, 20, 30]`, `[20, 30, 35]`, `[30, 35, 40]`, ... (full trace in `output_kway.txt`).

## (b) Pairwise merge
Merge L1 and L2 (7 comparisons, 8 moves), then merge the result with L3 (11 comparisons, 12 moves).

## Results for the given input (k = 3, N = 12)

| Metric | Min Heap k-way | Pairwise |
|---|---|---|
| Comparisons | 21 | 18 |
| Element moves | 12 | 20 |
| Max heap size | 3 (= k) | no heap |
| Max temporary array | none | 12 |

For such a small k, pairwise needs slightly fewer comparisons. The heap writes each element only once.

## (c) Analysis

| Criterion | Min Heap | Pairwise (sequential) |
|---|---|---|
| Heap size | at most k | n/a |
| Comparisons | about 2 N log k (about log k per element for a binary heap) | about N k / 2 |
| Time complexity | **O(N log k)** | **O(N k)** |
| Extra space | **O(k)** plus output | **O(N)** intermediate arrays |

Measured scaling (100 elements per list, from `compare.py`):

| k | Heap comparisons | Pairwise comparisons |
|---|---|---|
| 3 | 597 | 497 |
| 10 | 6,166 | 5,341 |
| 50 | 53,431 | 126,258 |
| 200 | 291,812 | 1,989,902 |

## Conclusion
For small k (like 3), both are similar. As the number of sorted files grows, the **Min Heap k-way merge is far more suitable**: O(N log k) time versus O(N k), only O(k) extra memory, and it can stream output without loading everything. The crossover in the measurements happens between k = 10 and k = 50.
