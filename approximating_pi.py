import math

squared_xn = 4

for n in range(2, 40):
    power = 2 ** (n - 1)
    squared_xn = (2 * power * squared_xn) / (power + math.sqrt(power * power - squared_xn))
    print(f'|pi - x_{{{n + 1}}}| = {abs(math.pi - math.sqrt(squared_xn))}')
