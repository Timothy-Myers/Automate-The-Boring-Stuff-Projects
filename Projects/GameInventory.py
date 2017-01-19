stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    return inventory

displayInventory(stuff)

inv = addToInventory(inv, dragonLoot)
print ('After a hard battle you slayed the dragon!  Here is your updated loot!')
displayInventory(inv)
test = input()
