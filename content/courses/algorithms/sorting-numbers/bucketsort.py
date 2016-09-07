import math

def bucketsort(A, n):
    buckets = [[] for i in range(n)]
    for a in A:
        i = int(math.floor(a * n))
        buckets[i].append(a)
    for bucket in buckets:
        bucket.sort()
    i = 0
    for bucket in buckets:
        for a in bucket:
            A[i] = a
            i += 1

if __name__ == '__main__':
    import random
    A = [random.random() for i in range(10)]
    print ["%.2f" % x for x in A]
    bucketsort(A, 100)
    print ["%.2f" % x for x in A]
