# baek 10179

x = int(input())
prices = []

for i in range(x):
    y = float(input())
    prices.append(y)

for j in range(x):
    print(f"${prices[j] * 0.8:.2f}")