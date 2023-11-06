def sum_of_all_subsets(array):
  # Initialize the table of solutions.
  dp = [0 for i in range(len(array) + 1)]

  # Solve the base cases.
  dp[0] = 0

  # Recursively compute the solutions to the larger subproblems.
  for i in range(1, len(array) + 1):
    dp[i] = dp[i - 1] + array[i - 1]

  # Return the sum of all possible subsets.
  return dp[len(array)]

n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

total = 0

for subset in generate_all_subsets_using_lexicographic_code(nums):
    total += sum(subset)**k

print(total)