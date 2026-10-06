def merge_two(a, b):
    """Standard two-way merge. Returns (merged, comparisons, moves)."""
    i = j = comps = moves = 0
    out = []
    while i < len(a) and j < len(b):
        comps += 1
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
        moves += 1
    rest = a[i:] + b[j:]
    out += rest
    moves += len(rest)
    return out, comps, moves


def pairwise_merge(lists, verbose=True):
    """Merge ((L1 + L2) + L3) + ... one list at a time.
    Returns (merged, total_comparisons, total_moves, max_temp_size)."""
    merged = lists[0]
    total_c = total_m = 0
    max_temp = len(merged)
    for k in range(1, len(lists)):
        merged, c, m = merge_two(merged, lists[k])
        total_c += c
        total_m += m
        max_temp = max(max_temp, len(merged))
        if verbose:
            print(f"Merge {k}: comparisons={c}, moves={m}, result={merged}")
    return merged, total_c, total_m, max_temp


if __name__ == "__main__":
    L1 = [10, 30, 50, 70]
    L2 = [20, 40, 60, 80]
    L3 = [15, 35, 55, 75]
    result, c, m, t = pairwise_merge([L1, L2, L3])
    print("\nMerged output :", result)
    print("Comparisons   :", c)
    print("Element moves :", m)
