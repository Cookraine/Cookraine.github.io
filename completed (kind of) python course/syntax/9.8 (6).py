human = list(input().split())
print(human)


new_human = [float(element.replace(',', '.')) for element in human]

print(new_human)

index_mass = round((new_human[0] / (new_human[1]**2)), 1)
print(index_mass)