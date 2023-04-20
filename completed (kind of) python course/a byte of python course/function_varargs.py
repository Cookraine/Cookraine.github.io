def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(7,1,2,3,4,5,6,7,8,9,11,727,Jack=1123,John=2231,Inge=1560,Cook=1959,Argo=3791)