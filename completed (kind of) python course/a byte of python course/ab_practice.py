ab = {
    'Argo': 'peasantking@gmail.com 0671937730',
    'Grant': 'cityborn&raised@hotmail.com 0987275501',
    'Oscar': 'subwaynovelist@outlook.com 0507739532',
     }


def out():
    print('My address book looks like this:')
    for name, address in ab.items():
        print('\nContact {} at {}'.format(name, address))


out()

del ab['Oscar']

out()

ab['Theo'] = 'pu$$ypr!nc3@gmail.com 0996454211'

out()

if 'Diederich' in ab:
    print("\nWhere did you get him? O.o")
else:
    ab['\nDiederich'] = 'bestprof3ver@hotmail.com 0660694201'
    print('Diederich:', ab['Diederich'])

print('Let\'s fix something!')
ab['Diederich'] = 'piratecolleague@hotmail.com 0959372855'

out()