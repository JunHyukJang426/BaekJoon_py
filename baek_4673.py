# baek_4673
# 셀프 넘버

def d(n):
    num_list = list(map(int, str(n)))
    result = n + sum(num_list)
    return result

candidate = list(range(1, 10001))

for n in range(1, 10001):
    if d(n) in candidate:
        candidate.remove(d(n))

for i in range(len(candidate)):
    print(candidate[i])


# def self_num(n):
#     x = list(map(int, str(n)))
#     result = 0
#     for i in range(x)

# for generator in range(10000):
#     gen = list(map(int, str(generator)))
#     self = generator + sum(gen)
#     if 