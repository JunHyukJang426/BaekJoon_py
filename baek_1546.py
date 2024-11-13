# baek_1546
# 평균


n = int(input())
score = list(map(int, input().split()))

max_score = max(score)
avg = sum(score)/n

new_avg = avg / max_score * 100

print(new_avg)