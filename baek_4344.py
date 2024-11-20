# baek_4344
# 평균은 넘겠지

import sys

test = int(input())

n_list = []
over_avg = []

for i in range(test):
    n_list = list(map(int, sys.stdin.readline().strip().split()))
    n = n_list[0]
    scores = n_list[1:]
    average = sum(scores)/n
    over_avg = [x for x in scores if x > average]
    print(f'{len(over_avg) / n *100 :.3f}%')
    # over = 
    # #over_avg.count(scores > average)
    # print(f'{over_avg/n*100 :.3f}%')