import numpy as np
from multiprocessing import Pool, cpu_count

def subsetSums(nums, n, k):
    mod = 998244353
    freq = np.zeros(n*1000+1, dtype=np.int64)
    freq[0] = 1

    for num in nums:
        freq[num:]+=freq[:-num]
        freq%=mod

    result = 0
    for i in range(len(freq)):
        if freq[i]>0:
            result = (result + pow(i, k, mod) * freq[i]) % mod

    return result

# Driver code
with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    arr = list(map(int, file.readline().split()))

print(subsetSums(arr, n, k))
