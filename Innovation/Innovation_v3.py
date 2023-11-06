n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

cards.sort(key=lambda x: -(x[0] + x[1]))

selected_cards_ab = cards[:m]

max_cd_card = max(cards, key=lambda x: x[2] + x[3])

sums_of_selected_cards = [(sum(card), i) for i, card in enumerate(selected_cards_ab)]
sum_of_max_cd_card = sum(max_cd_card)

if min(sums_of_selected_cards)[0] < sum_of_max_cd_card:
    selected_cards_ab[min(sums_of_selected_cards)[1]] = max_cd_card
    sum_ab = sum(card[0] + card[1] for card in selected_cards_ab)
    max_total_sum = sum_ab + max_cd_card[2] + max_cd_card[3]
else:
    max_total_sum = sum_ab + selected_cards_ab[max(sums_of_selected_cards)[1]][2] + selected_cards_ab[max(sums_of_selected_cards)[1]][3]

print(max_total_sum)