def subsetSums(nums, n, k):
    # Initialize a dictionary to store the frequency of subset sums
    freq = {0: 1}
    mod = 998244353

    # Iterate over each number in the array
    for num in nums:
        # Create a copy of the current state of the dictionary
        temp = freq.copy()
        # For each sum in the dictionary, add the current number and update the frequency
        for sum in freq:
            new_sum = sum + num
            if new_sum in temp:
                temp[new_sum] += freq[sum]
            else:
                temp[new_sum] = freq[sum]
        # Update the original dictionary
        freq = temp

    # Calculate the sum of powers
    result = 0
    for sum in freq:
        result = (result + pow(sum, k, mod) * freq[sum]) % mod

    return result

# Driver code
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(subsetSums(arr, n, k))
