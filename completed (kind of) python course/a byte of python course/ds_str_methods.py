# This is a string object
name = 'Cookraine'

if name.startswith('Cook'):
    print('Yes, the string starts with "Cook"')
else:
    print('No, it does not start with "Cook"')

if 'a' in name:
    print('Yes, it contains the string "a"')
else:
    print('No, it does not contain the string "a"')

if name.find('rain') != -1:
    print('Yes, it contains the string "rain"')
else:
    print('No, it does not contain the string "rain"')

delimiter = ' || '
mylist = ['Japan', 'Ukraine', 'Poland', 'Taiwan']
print(delimiter.join(mylist))