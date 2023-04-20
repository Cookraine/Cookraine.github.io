first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))

if first and second > 100:
    print(max(first, second))
else:
    print(second + 100)