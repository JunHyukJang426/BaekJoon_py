# baek_1934 최소공배수(LCM)

x = int(input())

for i in range(x):
    a, b = map(int, input().split())
    a_1, b_1 = a, b
    while a % b != 0:
        r = a % b
        a, b = b, r
    print(a_1 * b_1 // b)