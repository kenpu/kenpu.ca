from merge import merge

def mergesort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        return merge(mergesort(L[:n/2]), mergesort(L[n/2:]))

if __name__ == '__main__':
    import random
    a = [random.randint(0, 100) for i in range(10)]
    print a
    print mergesort(a)
