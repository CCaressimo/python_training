"""
This module is to simulate a shopping at a grocery store
"""
import random

store_items = {
    "apples": {"price": 1.20, "quantity": random.randint(0, 15)},
    "bananas": {"price": 0.50, "quantity": random.randint(0, 15)},
    "oranges": {"price": 1.00, "quantity": random.randint(0, 15)},
    "grapes": {"price": 2.50, "quantity": random.randint(0, 15)},
    "carrots": {"price": 0.80, "quantity": random.randint(0, 15)},
    "potatoes": {"price": 1.50, "quantity": random.randint(0, 15)},
    "onions": {"price": 0.70, "quantity": random.randint(0, 15)},
    "tomatoes": {"price": 1.30, "quantity": random.randint(0, 15)},
    "broccoli": {"price": 2.00, "quantity": random.randint(0, 15)},
    "spinach": {"price": 1.75, "quantity": random.randint(0, 15)},
    "chicken breast": {"price": 5.50, "quantity": random.randint(0, 15)},
    "ground beef": {"price": 6.00, "quantity": random.randint(0, 15)},
    "salmon": {"price": 10.00, "quantity": random.randint(0, 15)},
    "eggs": {"price": 3.50, "quantity": random.randint(0, 15)},
    "milk": {"price": 2.80, "quantity": random.randint(0, 15)},
    "cheese": {"price": 4.50, "quantity": random.randint(0, 15)},
    "butter": {"price": 3.00, "quantity": random.randint(0, 15)},
    "yogurt": {"price": 1.25, "quantity": random.randint(0, 15)},
    "bread": {"price": 2.50, "quantity": random.randint(0, 15)},
    "rice": {"price": 1.90, "quantity": random.randint(0, 15)},
    "pasta": {"price": 1.20, "quantity": random.randint(0, 15)},
    "cereal": {"price": 3.80, "quantity": random.randint(0, 15)},
    "peanut butter": {"price": 3.30, "quantity": random.randint(0, 15)},
    "jam": {"price": 2.70, "quantity": random.randint(0, 15)},
    "coffee": {"price": 5.00, "quantity": random.randint(0, 15)},
    "tea": {"price": 2.50, "quantity": random.randint(0, 15)},
    "sugar": {"price": 2.00, "quantity": random.randint(0, 15)},
    "salt": {"price": 1.20, "quantity": random.randint(0, 15)},
    "flour": {"price": 2.50, "quantity": random.randint(0, 15)},
    "canned beans": {"price": 1.30, "quantity": random.randint(0, 15)},
    "canned tuna": {"price": 2.20, "quantity": random.randint(0, 15)},
    "frozen pizza": {"price": 6.50, "quantity": random.randint(0, 15)},
    "ice cream": {"price": 4.00, "quantity": random.randint(0, 15)},
    "chips": {"price": 3.00, "quantity": random.randint(0, 15)},
    "chocolate": {"price": 2.80, "quantity": random.randint(0, 15)},
    "soda": {"price": 1.50, "quantity": random.randint(0, 15)},
    "bottled water": {"price": 1.00, "quantity": random.randint(0, 15)},
    "toilet paper": {"price": 5.00, "quantity": random.randint(0, 15)},
    "laundry detergent": {"price": 7.50, "quantity": random.randint(0, 15)},
    "dish soap": {"price": 2.50, "quantity": random.randint(0, 15)},
    "paper towels": {"price": 4.50, "quantity": random.randint(0, 15)},
    "shampoo": {"price": 6.00, "quantity": random.randint(0, 15)},
    "conditioner": {"price": 6.00, "quantity": random.randint(0, 15)},
    "body wash": {"price": 5.00, "quantity": random.randint(0, 15)},
    "toothpaste": {"price": 3.00, "quantity": random.randint(0, 15)},
}

def available_items():
    """Display available store items"""
    print("\nAvailable Items:")
    print("=" * 30)
    print(f"{'Item':<15}{'Price':<8}{'Stock':<6}")
    print("-" * 30)

    for item, details in store_items.items():
        print(f"{item.title():<20} ${details['price']:<5.2f}  Quantity: {details['quantity']}")

    print("=" * 30 + "\n")

def calculate_totals(cart):
    """Calculate shopping cart totals and format output."""

    sales_tax_rate = 0.065
    subtotal = sum(store_items[item]["price"] * quantity for item, quantity in cart)
    sales_tax = sales_tax_rate * subtotal
    total = sales_tax + subtotal

    shopping_list = (f"Your cart: {', '.join([f'{quantity} {item}(s)' for item, quantity in cart])}" if cart else "Your cart is empty.")
    s_subtotal = "$" + f"{subtotal:,.2f}"
    s_tax = "$" + f"{sales_tax:,.2f}"
    s_total= "$" + f"{total:,.2f}"

    return shopping_list, s_subtotal, s_tax, s_total, total, subtotal, sales_tax


def display_cart(cart):
    """Function to display the cart"""
    shopping_list, s_subtotal, s_tax, s_total, total, subtotal, sales_tax = calculate_totals(cart)

    if not cart:
        print("\nYour cart is empty.\n")
        return total

    print("\n" + "=" * 35)
    print("       Grocery Store Receipt")
    print("=" * 35)
    print(f"{'Item':<15}{'Qty':<5}{'Price':>10}")
    print("-" * 35)

    for item, quantity in cart:
        price = store_items[item]["price"]
        total_price = price * quantity
        print(f"{item.capitalize():<15}{quantity:<5}${total_price:>9.2f}")

    print("-" * 35)
    print(f"{'Subtotal:':<20}{s_subtotal:>10}")
    print(f"{'Sales Tax:':<20}{s_tax:>10}")
    print(f"{'Total:':<20}{s_total:>10}")
    print("=" * 35)
    print("    Thank you for shopping with us!")
    print("=" * 35 + "\n")

    return total, subtotal, sales_tax


def checkout(cart):
    """Checkout function"""

    display_cart(cart)
    shopping_list, s_subtotal, s_tax, s_total, total, subtotal, sales_tax = calculate_totals(cart)

    if total == 0:
        print("Your cart is empty. Nothing to checkout.")
        return

    while True:
        try:
            payment = float(input("Enter your payment amount: $"))
            if payment >= total:
                change = payment - total
                print(f"\nPayment successful! Your change: ${change:.2f}")
                print("Thank you for shopping with us!\n")
                break
            else:
                print("Insufficient funds. You need at least ${total:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def add_to_cart():
    """Add items to shopping cart"""

    cart = []
    available_items()

    while True:
        item = input(
            """
Enter an item to add to your cart,
'cart' for shopping cart,
'items' for item list 
or 'checkout' to finish: """ ).lower()

        if item == 'items':
            available_items()
        elif item == 'cart':
            display_cart(cart)
        elif item in store_items and store_items[item]["quantity"] > 0:
            try:
                quantity = int(input(f"How many {item} would you like to buy?\n"))
                if quantity <= store_items[item]["quantity"]:
                    store_items[item]["quantity"] -= quantity
                    cart.append((item, quantity))
                    print(f"Added {quantity} {item}(s) to your cart.")
                else:
                    print(f"Sorry, we only have {store_items[item]['quantity']} {item}(s) left.")
            except ValueError:
                print("Please enter a valid number for quantity.")
        elif item == "checkout":
            checkout(cart)
            break
        else:
            print("Item not available, please try again.")


def main():
    """Start the grocery store simulation"""
    print("\nWelcome to the Python Grocery Store!")
    add_to_cart()
    print("\nGoodbye! Have a great day!")

if __name__ == "__main__":
    main()
