from itertools import combinations

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for combo in combinations(cards, m):
    ab_sum = sum(card[0] + card[1] for card in combo)
    cd_sum = max(card[2] + card[3] for card in combo)
    max_sum = max(max_sum, ab_sum + cd_sum)

print(max_sum)
