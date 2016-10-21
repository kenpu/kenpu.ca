import math
from collections import defaultdict

def h_mul(key, m, A=0.5*(math.sqrt(5)-1)):
    p = A * key
    fr = p - math.floor(p)
    hashvalue = math.floor(fr * m)
    return int(hashvalue)

def test(N, h):
    counts = defaultdict(int)
    for i in range(N):
        hv = h(i)
        counts[hv] += 1
    print sorted(counts.values(), reverse=1)[:100]

test(100000, lambda i: h_mul(i, 10000, A=math.pi))
