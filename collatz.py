n, k = map(int, input().split())
num_list = [int(i) for i in input().split()]

for k in range(k):
    new_list = []
    for i in num_list:
        if i % 2 == 0:
            new_list.append(int(i/2))
        else:
            new_list.append(int(3*i+1))
    num_list = new_list

print(sum(new_list))
