
store1 = {
    "Apple": 50,
    "Banana": 30,
    "Mango": 20
}

store2 = {
    "Banana": 40,
    "Orange": 25,
    "Mango": 15
}

store3 = {
    "Apple": 10,
    "Orange": 35,
    "Grapes": 20
}

# Display individual store inventories
print("Store 1 Inventory:", store1)
print("Store 2 Inventory:", store2)
print("Store 3 Inventory:", store3)

# Check whether an item exists
item = "Apple"

if item in store1:
    print(item, "exists in Store 1")
else:
    print(item, "does not exist in Store 1")

# Safely access inventory using get()
print("Mango stock in Store 1:", store1.get("Mango", 0))
print("Pineapple stock in Store 1:", store1.get("Pineapple", 0))

# Merge inventories using dictionary comprehension
all_stores = {item: store1.get(item, 0) +
              store2.get(item, 0) +
              store3.get(item, 0)
              for item in set(store1) | set(store2) | set(store3)}

print("\nCombined Inventory:", all_stores)

# Update inventory using the update() method
new_stock = {"Pineapple": 15, "Apple": 5}
all_stores.update(new_stock)

print("Updated Inventory:", all_stores)

# Display items with stock greater than 30
print("\nItems with stock greater than 30:")
for item, quantity in all_stores.items():
    if quantity > 30:
        print(item, ":", quantity)
