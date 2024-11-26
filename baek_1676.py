# baek_1676
# 팩토리얼 0의 개수

def factorial(n):
    if n==1:
        return 1
    elif n > 1:
        return n * factorial(n-1)
    
n = int(input())
n_fac = factorial(n)
n_list = []
count = 0

n_list = str(n_fac)[::-1]

for i in n_list:
    if i == '0':
        count += 1
    else:
        break
print(count)