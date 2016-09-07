def radix2(num):
    return "{0:b}".format(num)

# Get the i-th digit of binary string x
def digit(num, i):
    x = radix2(num)
    if i >= len(x):
        return 0
    else:
        d = x[-(i+1)]
        return 0 if d == '0' else 1

# create an empty array
def empty_array(size, init=None):
    return [init for i in range(size)]

# Sort A using binary digit i
def COUNTING_SORT(A, i):
    n = len(A)
    k = 2
    B = empty_array(size=n)
    C = empty_array(size=k, init=0)

    for a in A:
        d = digit(a, i)
        C[d] = C[d] + 1

    for j in range(1,k):
        C[j] = C[j] + C[j-1]

    for a in reversed(A):
        d = digit(a, i)
        B[C[d]-1] = a
        C[d] = C[d] - 1

    return B



def RADIX_SORT(A):
    n = max(len(radix2(x)) for x in A)
    for i in range(n):
        A = COUNTING_SORT(A, i)
    return A

if __name__ == '__main__':
    import random
    A = [random.randint(0, 200000) for i in range(10)]
    A = [129078, 127686, 164991, 150073, 49750, 136041, 55871, 50194, 43965, 119140]
    print A
    A = RADIX_SORT(A)
    print A
