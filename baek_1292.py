# baek_1292
# 쉽게 푸는 문제

n, m = map(int, input().split())

data = [0]
sum = 0

for i in range(1, m+1):
    for j in range(i):
        data.append(i)

for i in range(n, m+1):
    sum += data[i]
print(sum)