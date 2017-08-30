inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = []
print(inventory)


inventory['pocket'] = ['seashell', 'strange berry','lint']
print(inventory)

sort_backpack = (inventory['backpack']).sort()
print(sort_backpack)

inventory['backpack'].remove('dagger')
print(inventory['backpack'])

inventory['gold'] += 50
print(inventory['gold'])