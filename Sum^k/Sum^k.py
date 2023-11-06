def subsetSums(nums,n):
    # There are total 2^n subsets
    s = [0]
    for i in range(n):
        v = len(s)
        for t in range(v):
            s.append(s[t] + nums[i]) # add this element with previous subsets
    # Print
    return s
 
# Driver code
n, k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

print(sum([i**k for i in subsetSums(arr, n)]) % 998244353)