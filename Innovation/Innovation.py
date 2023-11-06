def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]
 
# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)==n]

n, m =[int(i) for i in input().split()]

cards = []
for i in range(n):
    cards.append([int(j) for j in input().split()])

highest = 0

decks = subsets_of_given_size(cards, m)

for deck in decks:
    num = sum(map(sum, list(zip(*deck))[:2]))
    num_t = 0
    for card in deck:
        largest_sum = card[-1] + card[-2]
        if largest_sum > num_t:
            num_t = largest_sum
    num += num_t
    if num > highest:
        highest = num

print(highest)
