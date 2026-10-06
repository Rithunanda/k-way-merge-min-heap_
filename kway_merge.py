from min_heap import MinHeap


def kway_merge(lists, verbose=True):
    """K-way merge of sorted lists using a Min Heap.
    Returns (merged_list, comparisons, max_heap_size)."""
    heap = MinHeap()
    out = []
    max_size = 0

    # Step 1: insert the first element of every list
    for i, lst in enumerate(lists):
        if lst:
            heap.push((lst[0], i, 0))
    max_size = len(heap)
    if verbose:
        print(f"Initial heap : {heap.values()}  (size={len(heap)}, comps={heap.comparisons})")

    # Step 2: extract min, push the next element of the same list
    step = 0
    while len(heap):
        val, i, j = heap.pop()
        out.append(val)
        step += 1
        if j + 1 < len(lists[i]):
            heap.push((lists[i][j + 1], i, j + 1))
        max_size = max(max_size, len(heap))
        if verbose:
            print(f"Step {step:2d}: extracted {val:3d} (L{i+1}) -> heap {heap.values()}  "
                  f"(size={len(heap)}, comps so far={heap.comparisons})")

    return out, heap.comparisons, max_size


if __name__ == "__main__":
    L1 = [10, 30, 50, 70]
    L2 = [20, 40, 60, 80]
    L3 = [15, 35, 55, 75]
    result, comps, max_size = kway_merge([L1, L2, L3])
    print("\nMerged output   :", result)
    print("Comparisons     :", comps)
    print("Max heap size   :", max_size)
