class MinHeap:
    """Array-based min heap of (value, list_id, index) nodes.
    Counts every key comparison in self.comparisons."""

    def __init__(self):
        self.a = []
        self.comparisons = 0

    def __len__(self):
        return len(self.a)

    def _less(self, i, j):
        self.comparisons += 1
        return self.a[i][0] < self.a[j][0]

    def push(self, node):
        self.a.append(node)
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._less(i, p):
                self.a[i], self.a[p] = self.a[p], self.a[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.a)
        while True:
            l, r, s = 2 * i + 1, 2 * i + 2, i
            if l < n and self._less(l, s):
                s = l
            if r < n and self._less(r, s):
                s = r
            if s == i:
                break
            self.a[i], self.a[s] = self.a[s], self.a[i]
            i = s

    def pop(self):
        top = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            self._sift_down(0)
        return top

    def values(self):
        return [x[0] for x in self.a]
