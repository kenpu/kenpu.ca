def inc(cnt, key):
    if key in cnt:
        cnt[key] += 1
    else:
        cnt[key] = 1
    return cnt

def repeat(n, x):
    return [x for i in range(n)]

def count_seq0(seq):
    if len(seq) == 0:
        return dict()
    else:
        head = seq[0]
        tail = seq[1:]
        return inc(count_seq0(tail), head)

def count_seq(seq, cnt):
    if len(seq) == 0:
        return cnt
    else:
        head = seq[0]
        tail = seq[1:]
        return count_seq(tail, inc(cnt, head))

N = 997
try:
    print count_seq0(repeat(N, "a"))
except:
    print "count_seq0 failed"

try:
    print count_seq(repeat(N, "b"), {})
except:
    print "count_seq failed"
