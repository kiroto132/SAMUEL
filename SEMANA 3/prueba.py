inventory = [
    {"title": "el diablo y la señorita pym", "price": 10.0, "quantity": 100},
    {"title": "satanas", "price": 15.0, "quantity": 50},
    {"title": "las ventajas de ser invisible", "price": 20.0, "quantity": 30},
    {"title": "it", "price": 25.0, "quantity": 10},
    {"title": "cien años de soledad", "price": 30.0, "quantity": 5}
]


def added_book(title, price, quantity):
        inventory.append({"title": title, "price":price, "quantity":quantity} )
        print("the book was added effectively")

#
def search_book(title):
    for inve in inventory:
        if inve["title"] == title:
            print(f"the book is {title} and preci is {inve['price']} and quantity is {inve['quantity']}")
            return inve
    print(f"the book {title} not exists")
    return None
def meet_the_books():
    for inv in inventory:
        print(inv)
    if not inv:
        print("not the books")
        return
def update_inventory(title,price_n):
    for inve in inventory:
        if inve["title"] == title:
            inve["price"] = price_n
            return 
    print(f"the book {title} not exists")
    return None
def remove_books(title):
    for chesk in inventory:
        if chesk["title"] == title:
            inventory.remove(chesk)
            print(f"the book remove {title}")
            return
    print("not exists the book")
def calculate_value():
    worth = 0
    for tory in inventory:
        sumu = tory['price'] * tory['quantity']
        worth = sumu + worth
    print(f"the worth totality is ${worth:.2f}")
    return
def menu():
    while True:
        print("1. add new book. ")
        print("2. research a book by his name. ")
        print("3. show all the inventory. ")
        print("4. Update the inventory. ")
        print("5. Remove a book from the inventory. ")
        print("6. Calculate total value of the inventory. ")
        print("7. exit")

        opcion = int(input("Select an option:\n"))

        match opcion:
            case 1:
                title = str(input("Enter the book into the inventory:\n"))
                price = float(input("the price of the book:\n"))
                quantity = int(input("what is the quantity:\n"))
                added_book(title, price, quantity)
            case 2:
                title = str(input("what is the book like yours search:\n"))
                search_book(title)
            case 3:
                meet_the_books()
            case 4:
                title = str(input("what is the book update?"))
                price_n= float(input("price new?"))
                update_inventory(title,price_n)
            case 5:
                title = str(input("what is the remove the book?"))
                remove_books(title)
            case 6:
                calculate_value()
            case 7:
                print("closing")
                break
            case _:
                print("incorrect")
            
menu()