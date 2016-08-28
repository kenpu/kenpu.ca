from partition import partition

def quicksort(L, p, r):
    if p < r:
        k = partition(L, p, r)
        quicksort(L, p, k-1)
        quicksort(L, k+1, r)

if __name__ == '__main__':
    import random
    a = [random.randint(0, 100) for i in range(10)]
    print a
    quicksort(a, 0, len(a)-1)
    print a
    print sorted(a)

