import bisect

T = int(input())
kills_li = []

for i in range(T):
    N, A, B = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]

    p_new = sorted(p)
    kills = 0

    while A < B:
        if len(p_new) == 0:
            kills = -1
            break
        highest_power = bisect.bisect_left(p_new, A)
        if highest_power == 0:
            if p_new[highest_power] != A:
                kills = -1
                break
            else:
                kills += 1
                A += p_new[highest_power]
                p_new.pop(highest_power)
        else:
            kills += 1
            A += p_new[highest_power - 1]
            p_new.pop(highest_power - 1)
    
    kills_li.append(kills)

for i in kills_li:
    print(i)