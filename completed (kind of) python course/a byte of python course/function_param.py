def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


def print_min(a, b):
    if a < b:
        print(a, 'is minimum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is minimum')


# directly pass literal values
# print_max(3, 4)

x = int(input("x: "))
y = int(input("y: "))

# pass variables as arguments
print_max(x, y)
print_min(x, y)
