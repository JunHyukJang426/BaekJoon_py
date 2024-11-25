# baek_2675
# 문자열 반복

import sys

n = int(sys.stdin.readline())
str_list = []


for i in range(n):
    re, string = sys.stdin.readline().split()
    for x in string:
        print(int(re) * x, end='')
    print()
   