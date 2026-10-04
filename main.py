inventory = {
    "laptop": {"price": 1200, "stock": 3},
    "mouse": {"price": 50, "stock": 2},
    "keyboard": {"price": 100, "stock": 0},
    "monitor": {"price": 200, "stock":5},
    "headphones": {"price": 150, "stock":4}   
}

cart = []
total_price = 0.0

print("Welcome to the Tech Store!")
print("Available items:", ", " .join(inventory.keys()))

while True:
    item = input("Enter item name to add (or 'done' to checkout): ").strip().lower()

    if item == 'done':
        break

    if item not in inventory:
        print("Item not found. Please choose from the list")
        continue

    if inventory[item]["stock"] > 0:
        cart.append(item)
        inventory[item]["stock"] -= 1
        price = inventory[item]["price"]
        total_price += price
        print(f"Added {item} (${price}). Stock left: {inventory[item]["stock"]}")
    else:
        print(f"Sorry, {item} is out of stock")

print("\n" + "="*40)
print("YOUR ORDER SUMMARY")
print("="*40)

if not cart:
    print("Your cart is empty")
else:
    for item in cart:
        price = inventory[item]["price"]
        if price > 500:
            category = "Premium"
        elif price > 100:
            category = "Standard"
        else:
            category = "Budget"
        print(f" {item:12}  ${price:6.2f}  [{category}]")     

    print("-"*40)
    print(f"Subtotal: ${total_price:.2f}") 

    if total_price > 500:
        dis = 0.15
        dis_name = "15%"
    elif total_price > 200:
        dis = 0.10
        dis_name = "10%"
    elif total_price > 100:
        dis = 0.05
        dis_name = "5%"
    else:
        dis = 0.0
        dis_name = "0%"

    if dis > 0:
        dis_price = total_price * dis
        final_price = total_price - dis_price
        print(f"Discount: {dis_name} (you saved ${dis_price:.2f})")
        print(f"Final: ${final_price:.2f}")
    else:
        print(f"Final: ${total_price:.2f}")

    print("\n--- Loyality Points ---")
    pass

print("\nThank you for shopping with us.")

