# Welcome to development testing week one

Welcome, in this readme I will explain how the test code is built.


# program instructions

When you run the program you will see an interactive menu and you must choose an option that you see on the screen. If you select an option that is not on the screen, an error will appear.

# Option 1. Add product

In option number 1, you'll find a message instructing you to enter all the information about the new product.
Such as: Product name, price, and quantity.

***example of option number 1.***

**Input**

*Enter the name:*

*Price:*

*Quantity:*

**Output**

*The {name} product with price: {price} and quantity: {quantity}*

# Option 2. Meet product

If you choose option number 2, you will only find the inventory with the products that were already burned and the product you just added.

# Option 3. Search product

If you choose option number 3, it will ask you to enter the name of the product you want to search for to see all the information about that product. If you enter a name that is not in the inventory, it will send you a printout saying that the product is not in the inventory.

***example of option number 3.***

**input**

*Enter the name:*

**Output**

*The product is {name} and price is {'price'} and quantity is {'quantity'}*

# Option 4. Update the product

In option number 4, the inventory will first be shown to you so you can choose which product you want to update the price of.

***example of option number 4.***

**input**

*Enter the name:*

*new price:*

**Output**

*The {name} with the new price is {price_new}*


# Option 5. Remove a product

In option number 5 you can delete a product that you no longer want in the inventory. When you choose this option, it will show you the inventory and you can choose which one you want to delete by writing the product name correctly. If you do not write the product name correctly or write a name that is not in the inventory, you will get a warning.

***example of option number 5.***

**Input**

*Enter the name:*

**Output**

*The product remove {name}*

# Option 6. Calculate the products

Option number 6 will show us the total value of all the inventory and see how much profit the inventory is generating.

