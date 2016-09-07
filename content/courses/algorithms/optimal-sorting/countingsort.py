def empty_array(size, init=None):
    return [init for i in range(size)]

def COUNTING_SORT(A):
    n = len(A)
    k = max(A) + 1
    B = empty_array(size=n)
    C = empty_array(size=k, init=0)

    for a in A:
        C[a] = C[a] + 1

    for i in range(1,k):
        C[i] = C[i] + C[i-1]

    for a in reversed(A):
        B[C[a]-1] = a
        C[a] = C[a] - 1

    return B

if __name__ == '__main__':
    import random
    A = [random.randint(0, 20) for i in range(10)]
    print A
    B = COUNTING_SORT(A)
    print B
