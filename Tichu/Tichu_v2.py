N, K = map(int, input().split())
cards_p = list(set([int(i) for i in input().split()]))
cards = sorted(cards_p)

longest_run = 0

for start in range(len(cards)):
    current_run = 1
    wildcard_used = 0
    for i in range(start, len(cards) - 1):
        if cards[i+1] == cards[i]+1:
            current_run += 1
        elif cards[i+1] - cards[i] - 1 <= K - wildcard_used:
            current_run += cards[i+1] - cards[i]
            wildcard_used += cards[i+1] - cards[i] - 1
        else:
            break
    current_run += min(K - wildcard_used, 1 if start == 0 else cards[start] - 1)
    longest_run = max(longest_run, current_run)

print(longest_run)
