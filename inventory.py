from tabulate import tabulate

#========The beginning of the class==========
# defining a shoe class with the below attributes
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# defining methods
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def set_quantity(self, new_quant):
        self.quantity = new_quant

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()
    

#==========Functions outside the class==============
'''
The list will be used to store a list of objects of Shoe.
'''
shoe_list = []
shoe_obj = []

'''
reading and writing to inventory.txt file
'''
inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")


# define read_Shoe_data() that reads each line from the text file
# append items onto shoe_list
# cast each item into an object and append to object list
def read_Shoe_data():
    file = None
    try:
        for lines in inventory_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            shoe_list.append(split_lines)

        for i in range(1, len(shoe_list)):
            array = shoe_list[i]
            shoe1 =  Shoe(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(shoe1)

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!")
        print(error)

    else:
        if file is not None:
            file.close()


# define capture_Shoe() that allow a user to capture data about a shoe 
# use the data to create a shoe object and append the object inside the shoe list
def capture_Shoe():
    file = None
    try:
        new_country = input("Please enter the country of your product: ")
        new_code = input("Please enter the code of your product: ")
        new_product = input("Please enter the name of your product: ")
        new_cost = int(input("Please enter the cost of your product, only in numbers. E.g. 12345: "))
        new_quantity = int(input("Please enter the quantity of your product, only in numbers. E.g. 2: "))

        new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(new_shoe)

        inventory_write.write(f"\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}")
        print("\nThank you, your product has been loaded!")

        inventory_write.close()

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!")
        print(error)

    else:
        if file is not None:
            file.close()


# define view_all() that displays all shoes
# display using tabulate
def view_all():
    file = None
    try:
        print("\n-------------------------------STOCKLIST--------------------------------\n")
        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        for lines in shoe_obj:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ("Country","Code", "Product", "Cost", "Quantity"), tablefmt="fancy_grid"))

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!")
        print(error)

    else:
        if file is not None:
            file.close()


# define restock() that displays first 5 items with lowest stock, using sort()
# display using tabulate
# write to file and close
def restock():
    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoe_obj.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoe_obj[i])

        print("\n\n\n\n----------------------------Lowest stock items:----------------------------\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ("Country","Code", "Product", "Cost", "Quantity"), tablefmt="fancy_grid", showindex= range(1,6)))

        user_input_item = int(input("\nPlease confirm the index of the product you want to restock: "))
        user_input_qty = int(input("\nPlease confirm the new quantity: "))
        shoe_obj[user_input_item].set_quantity(user_input_qty)

        output = ""
        for item in shoe_obj:
            output += (f"{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n")

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print("\nYour product has been updated!")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    else:
        if file is not None:
            file.close()


# define search_shoe() that will search for a shoe from the list using the shoe code
def search_shoe():

    search_shoe = input("\nPlease enter the code you are searching for: ")

    for line in shoe_obj:
        if line.get_code() == search_shoe:
            print(f'\n {line}')
            print("\n---------------------------------------------------------------------------\n")
            print("Please select another option from the menu below ")

            break
     
    else:   
        print("\nSorry, this code does not exist!\n")
        print("\n\nPlease select another option from the menu below ")
   

# define value_per_item() that calculates the total value for each item
# formula for value is 'cost * quantity'
def value_per_item():

    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f"{line.get_code()} VALUE: {value}")

    print("\n------------------------------------------------------------------")
    print("\nPlease select another option from the menu below ")


# define highest_quantity() that determines the product with the highest quantity
# mark item as being for sale
def highest_quantity():
    highest_qty = []

    for line in shoe_obj:
        highest_qty.append(line)
    print("\n----------------- Highest Stock Item: ------------------\n")

    print(max(shoe_obj, key=lambda item: item.quantity))
    print("This item has now been marked on sale\n")

    print("-----------------------------------------------------------\n")
    print("\nPlease select an option from the menu below")



#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# display menu options
read_Shoe_data()
while True:
    try:
        menu = int(input('''\n
Welcome to RionDev Inventory System! 
Please select from the menu below:
1. Capture Shoes
2. View All
3. Restock
4. Search
5. View Item Values
6. View Sale Items
7. Exit
\n: '''))

        if menu == 1:
            capture_Shoe()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            print("\n----------------- Item Values: ------------------\n")
            value_per_item()

        elif menu == 6:
            highest_quantity()
        
        elif menu == 7:
            print("Goodbye!!!")
            exit()

        elif menu > 7:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")
        
    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number from the menu provided.\n")
    
