import math

cargo = int(input())

tariff = cargo / 100;
if cargo <= 10000:
    if cargo > 1000:
        price = tariff * 65
        print(math.ceil(price))
    elif cargo > 500:
        price = tariff * 70
        print(math.ceil(price))
    else:
        price = tariff * 80
        print(math.ceil(price))
else:
    print("unavailable")