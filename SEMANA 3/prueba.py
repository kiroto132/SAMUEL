#You were hired to create a system that organizes the products in an inventory and makes it optimal for the administrator,
#easy to use, and fast in searching for products.
inventory = [{'product': 'rice', 'price' : 5000, 'quantity' : 100},
            {'product': 'rhicken', 'price' : 16000,  'quantity': 90},
            {'product' : 'rugar', 'price': 4500, 'quantity': 70},
            {'product': 'ratmeal', 'price' : 3500, 'quantity': 50}
            ]

#Here you add the product, price and quantity to display in the inventory.
def add_products(name, price, quantity):
    inventory.append({'product': name, 'price' : price, 'quantity' : quantity})
    print(f"The {name} products with price: {price:.2f} and the quantity: {quantity} was successfully added! ")

#This is optional, here you see the entire inventory to verify if the new product was successfully added.
def meet_product():
    for i in inventory:
        print(i)
    if not i:
        print("There are no products")

#Search for a specific product to see if it is in stock, see its price and quantity.
def search_products(name):
    for inv in inventory:
        if inv['product'] == name:
            print(f"The product is {name} and price is {inv['price']:.2f} and quantity is {inv['quantity']}")
            return inv
    print(f"The product {name} not exist, please re-enter an existing product.")
    return None

#Price update in case any product increases or decreases in price
def update_the_product(name, price_new):
    for to in inventory:
        if to['product'] == name:
            to['price'] = price_new
            print(f"The {name} with the new price is ${price_new:.2f}")
            print(inventory)
            return
    print(f"The product {name} not exist")
    return None

#delete a product you no longer want to sell
def remove_a_product(name):
    for ry in inventory:
        if ry['product'] == name:
            inventory.remove(ry)
            print(f"The product remove {name}")
            return
    print("The product not exist.")

#Calculate the price and quantity of all products and see the total profit price
def calculate_the_products():
    worth = 0 
    for ve in inventory:
        suma = ve['price'] * ve['quantity']
        worth = suma + worth
        print(f"The worth total is ${worth:.2f}")
        return

#Interactive menu to choose the function or section you want to see
def menu():
    while True:
        print("1. Add products")
        print("2. Meet the products")
        print("3. Search products")
        print("4. Update products")
        print("5. Remove products")
        print("6. Calculate products")
        print("7. get out of inventory")

        
        try:
            option = int(input("Select option:\n"))
            match option:
                case 1:
                    name = str(input("What is the producto:\n")).lower()
                    price = float(input("What is the price the products:\n"))
                    quantity = int(input("Quantity?:\n"))
                    add_products(name, price, quantity)
                case 2:
                    meet_product()
                case 3:
                    name = str(input("What is the product you want to search for?:\n")).lower()
                    search_products(name)
                case 4:
                    print(inventory)
                    name = str(input("What is the product?:\n")).lower()
                    price_new = float(input("What is the new price?:\n"))
                    update_the_product(name,price_new)
                case 5:
                    print(inventory)
                    name = str(input("What is the prpoduct you want to remove?:·\n")).lower()
                    remove_a_product(name)
                case 6:
                    calculate_the_products()
                case 7:
                    print("Closing.")
                    break
                case _:
                    print("Incorrect.")          
        except ValueError:
            print("Invalid option, please select an option shown on the screen.")
menu()