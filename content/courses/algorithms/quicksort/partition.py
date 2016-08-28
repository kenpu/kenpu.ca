def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1

if __name__ == '__main__':
    import random
    a = [random.randint(0, 10) for i in range(9)] + [5.5]
    print a
    k = partition(a, 0, len(a)-1)
    print a
    print a[k]

