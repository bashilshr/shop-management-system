import datetime
import random
import read
import write
import operation
def display():
    print("Welcome to the IIT Laptop Store")
    print("-+-+-+-+-+-+-+-+-select an option to continue-+-+-+-+-+-+-+-+-\n ")
    print("press 1 to sell laptop")
    print("press 2 to buy laptop")
    print("press 3 to Exit the program")

def to_get_user_option():
    while True:
        try:
            user_input = int(input('enter the option to continue\n '))
            if user_input in [1,2,3]:
                return user_input
            else:
                print("Enter valid option (1,2,3)")
        except ValueError:
            print("Enter appropriate number!!")

def to_get_user_name():
    while True:
        enter_name = input("ENTER YOUR FIRST NAME : ").strip()
        if enter_name.replace(" ","").isalpha():
            return enter_name
        else:
            print("please enter your name only!!")

def to_get_user_phone():
    while True:
        try:
            enter_phone = int(input('ENTER YOUR PHONE NUMBER: '))
            return enter_phone
        except ValueError:
            print(" Enter Number only!")
def to_get_user_address():
    while True:
        enter_address = str(input("ENTER YOUR ADDRESS : ")).strip()
        if enter_address.isalpha():
            return enter_address
        else:
            print("please enter your address only!!!")

def sell_laptop():
    user_name = to_get_user_name()
    user_phone = to_get_user_phone()
    user_address = to_get_user_address()
    print(f"Hello {user_name}, you chose to sell a laptop.")
    print(f"Phone: {user_phone}, Address: {user_address}")
    # logic for selling a laptop goes here
    laptoplist = []
    loop_function = True
    while loop_function:
        read.Display()
        dictionary = read.read_laptop()
        lap_number = operation.num_select(dictionary)
        if int(dictionary[lap_number][3]) == 0:
            print("no stock")
            loop_1 = True
            while loop_1:
                ask = input("Do you want to continue y/n ")
                if ask.lower() == "y":
                    lap_number = operation.num_select(dictionary)
                    loop_1 = False
                elif ask.lower() == "n":
                    loop_function = False
                    break
                else:
                    print("Appropriate values")
        if loop_function:
            quantity_laptop = operation.laptopQuantity(dictionary,lap_number)
            operation.updatedictionary(lap_number, dictionary, quantity_laptop, laptoplist)
            write.update(dictionary)
            loop = True
            while loop:
                yn = input("Do you want to continue(Y/N): ")
                if yn.upper() == "N":
                    loop,loop_function = False, False
                elif yn.upper() == "Y":
                    loop = False
                else:
                    print("Enter appropriate choice")
    if len(laptoplist) != 0:
        bill_num = random.randint(0, 1000)
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        time = datetime.datetime.now().strftime("%H:%M/%S")
        write.bill_maker(user_name, user_address, user_phone, laptoplist, bill_num, date, time)
        write.bill_creator(user_name, user_address, user_phone, laptoplist, bill_num, date, time)

def buy_laptop():
    user_name = to_get_user_name()
    user_phone = to_get_user_phone()
    user_address = to_get_user_address()
    print(f"Hello {user_name}, you chose to buy a laptop.")
    print(f"Phone: {user_phone}, Address: {user_address}")
    # logic for buying a laptop goes here
    while True:
        loop_function = True
        laptoplist = []
        dictionary = read.read_laptop()
        while loop_function:
            read.Display()
            lap_number = operation.num_select(dictionary)
            loop_3 = True
            while loop_3:
                try:
                    quantity_laptop = int(input("Enter the quantity for the laptop you want to buy: "))
                except ValueError:
                    print("Enter numeric value")
                else:
                    if quantity_laptop > 0:
                        loop_3 = False
            while quantity_laptop <= 0:
                print("Enter appropriate values")
                quantity_laptop = int(input("Enter the laptop quantity you want to sell : "))
                operation.quantity_lap1()
            operation.updatedictionary1(lap_number, dictionary, quantity_laptop, laptoplist)
            write.update(dictionary)
            loop = True
            while loop:
                yn = input("Do you want to continue(Y/N): ")
                if yn.upper() == "N":
                    loop_function = False
                    loop = False
                elif yn.upper() == "Y":
                    loop = False
                else:
                    print("Enter inappropriate choice")
        bill_num = random.randint(0, 1000)
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        time = datetime.datetime.now().strftime("%H:%M/%S")
        write.bill_maker1(user_name, laptoplist, bill_num, date, time)
        write.bill_creator1(user_name, laptoplist, bill_num, date, time)
        loop = True
        exit()

def main():
    display()
    user_option = to_get_user_option()
    if user_option == 1:
        sell_laptop()
    elif user_option == 2:
        buy_laptop()
    elif user_option == 3:
        print("Exiting the program. Goodbye!")
        exit()

if __name__ == "__main__":
    main()