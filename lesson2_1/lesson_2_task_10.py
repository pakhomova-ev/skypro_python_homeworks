def bank(x,y):
    percentOneYear = 0.1           # 10%
    for result in range(y):
        x += x * percentOneYear    # oneYear = x + x * percentOneYear
    return x

print(bank(50, 5))
