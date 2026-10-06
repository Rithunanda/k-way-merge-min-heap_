import random
from kway_merge import kway_merge
from pairwise_merge import pairwise_merge

L1 = [10, 30, 50, 70]
L2 = [20, 40, 60, 80]
L3 = [15, 35, 55, 75]

print("=== Given example (k=3, N=12) ===")
h_out, h_c, h_size = kway_merge([L1, L2, L3], verbose=False)
p_out, p_c, p_m, p_tmp = pairwise_merge([L1, L2, L3], verbose=False)
assert h_out == p_out == sorted(L1 + L2 + L3)
print(f"{'':22}{'Min Heap':>10}{'Pairwise':>10}")
print(f"{'Comparisons':22}{h_c:>10}{p_c:>10}")
print(f"{'Element moves':22}{12:>10}{p_m:>10}")
print(f"{'Max heap size':22}{h_size:>10}{'-':>10}")
print(f"{'Max temp array size':22}{'-':>10}{p_tmp:>10}")

print("\n=== Scaling with k (each list has 100 sorted elements) ===")
print(f"{'k':>6}{'N':>8}{'Heap comps':>14}{'Pairwise comps':>16}{'Pairwise moves':>16}")
random.seed(1)
for k in [3, 10, 50, 200]:
    lists = [sorted(random.sample(range(10**6), 100)) for _ in range(k)]
    _, hc, _ = kway_merge(lists, verbose=False)
    _, pc, pm, _ = pairwise_merge(lists, verbose=False)
    print(f"{k:>6}{k*100:>8}{hc:>14}{pc:>16}{pm:>16}")
