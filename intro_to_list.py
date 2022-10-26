# create a list
items = ['Cell Phone', 'Watch','Car','Drone']

# accesing the elements in the list
print(f'item_1:{items[0]}\n')

# Update elements in the list 
items[0] = 'Apple'
print(f'updated item_1: {items[0]}\n')
print(f'items review: {items}\n')

# add items in the list
items.append('Laptop')
print(f'items_added:{items}\n')

# delete element in the list
del items[0]
print(f'Deleted_items:{items}\n')

# other way to delete the elements in the list
popped_item = items.pop(-1)
print(f'last_item_popped: {popped_item}\n')

# insert element in the list
items.insert(len(items),'Laptop')
print(items)

# sort a list
items.sort()
print(f'sorted items: {items}')

# reverse the items in the list
items.reverse()
print(f'Items in the list are reversed: {items}')
