N, K = map(int, input().split())
cards_p = list(set([int(i) for i in input().split()]))
cards = sorted(cards_p)

current_run = 1
longest_run = 1
wildcard_used = 0
for i in range(len(cards)):
    if cards[i] == cards[-1]:
        current_run += K - wildcard_used
        longest_run = max(longest_run, current_run)
        current_run = 1
        wildcard_used = 0
    elif cards[i+1] == cards[i]+1:
        current_run += 1
    elif cards[i+1] - cards[i] - 1 <= K - wildcard_used:
        current_run += cards[i+1] - cards[i]
        wildcard_used += cards[i+1] - cards[i] - 1
    else:
        longest_run = max(longest_run, current_run)
        current_run = 1
        wildcard_used = 0

if cards == []:
    longest_run = K

print(longest_run)