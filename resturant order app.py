#Restaurant_order_app.py

menu = {
    "1": {"name": "Coffee", "price": 50},
    "2": {"name": "Tea", "price": 30},
    "3": {"name": "Burger", "price": 120},
    "4": {"name": "Pizza", "price": 250},
    "5": {"name": "Sandwich", "price": 100}
}

cart = []

def show_menu_and_select():
    while True:
        print("\n--- MENU ---")
        for key, item in menu.items():
            print(f"{key}. {item['name']} - ₹{item['price']}")
        print("\nOptions:")
        print("a. View Cart")
        print("b. Remove Item from Cart")
        print("c. Proceed to Purchase")
        print("d. Back to Main Menu")
        print("e. Exit")

        choice = input("Enter item number to add to cart or option (a-e): ").strip().lower()

        if choice in menu:
            cart.append(menu[choice])
            print(f"✅ {menu[choice]['name']} added to cart.")
        elif choice == "a":
            show_cart()
        elif choice == "b":
            show_cart()
            try:
                index = int(input("Enter item number to remove: ")) - 1
                remove_from_cart(index)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "c":
            if cart:
                generate_bill()
                cart.clear()
            else:
                print("🛒 Cart is empty! Add items first.")
        elif choice == "d":
            break
        elif choice == "e":
            print("👋 Thank you for visiting!")
            exit()
        else:
            print("❌ Invalid choice! Try again.")

def show_cart():
    print("\n🛒 --- YOUR CART ---")
    if not cart:
        print("Cart is empty.")
        return

    total = 0
    for idx, item in enumerate(cart, start=1):
        print(f"{idx}. {item['name']} - ₹{item['price']}")
        total += item["price"]
    print(f"Total Amount: ₹{total}")

def remove_from_cart(index):
    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"❎ {removed['name']} removed from cart.")
    else:
        print("❌ Invalid index!")

def generate_bill():
    print("\n🧾 --- FINAL BILL ---")
    total = 0
    for idx, item in enumerate(cart, start=1):
        print(f"{idx}. {item['name']} - ₹{item['price']}")
        total += item["price"]
    print(f"\n🟢 Total Payable Amount: ₹{total}")
    print("✅ Thank you for your purchase!\n")

def main():
    while True:
        print("\n🛒 Welcome to the Ordering System")
        print("1. Show Menu and Order")
        print("2. View Cart")
        print("3. Remove Item from Cart")
        print("4. Proceed to Purchase")
        print("5. Exit")

        user_input = input("Choose an option (1-5): ").strip()

        if user_input == "1":
            show_menu_and_select()
        elif user_input == "2":
            show_cart()
        elif user_input == "3":
            show_cart()
            try:
                index = int(input("Enter item number to remove: ")) - 1
                remove_from_cart(index)
            except ValueError:
                print("❌ Invalid input.")
        elif user_input == "4":
            if cart:
                generate_bill()
                cart.clear()
            else:
                print("🛒 Cart is empty! Add items before purchasing.")
        elif user_input == "5":
            print("👋 Thank you for shopping with us!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()