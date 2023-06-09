from typing import List
from math import floor

# check if there exists some item that have not been discarded
def exist_k(ranges: List[int], N : int) :
    oPar = 0
    for k in range(0, N + 1):
        par = ranges[k]
        oPar += par
        if oPar == 0 and k > N//2:
            return k
    return -1

def solve(a: List[int]):
    N = len(a)

    if a[N-1] >= 0: 
        return N if sum(a) > 0 else -1
    
    # accumulated sum of the whole list
    accu_sum = sum(a)

    # array of ranges to carry the balance factor
    ranges = [0 for _ in range(N+2)]
    ranges[0] += 1
    ranges[N//2 + 1] -= 1

    for i in range(N - N//2):
        # accumulated sum of the last i elements of the list
        if accu_sum <= 0:
            j = min(N//2, floor(accu_sum / a[N-1]))
            ranges[N - i - j] += 1
            ranges[N + 1 - i] -= 1
            
        accu_sum -= a[i]

    return exist_k(ranges, N)
