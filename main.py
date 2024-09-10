import datetime
import random
import read
import write
import operation
def display():
    print("Welcome to the laptop store")
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
    

def buy_laptop():
    user_name = to_get_user_name()
    user_phone = to_get_user_phone()
    user_address = to_get_user_address()
    print(f"Hello {user_name}, you chose to buy a laptop.")
    print(f"Phone: {user_phone}, Address: {user_address}")
    # logic for buying a laptop goes here

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


# def main():
#     read.header()
#     '''THIS FUNCTION ASKS THE USER TO SELL BUY OR EXIT '''
#     laptops = True 
#     while laptops :
#         print("-+-+-+-+-+-+-+-+-select an option to continue-+-+-+-+-+-+-+-+-\n ")
#         print("press 1 to sell laptop")
#         print("press 2 to buy laptop")
#         print("press 3 to Exit the program")
#         first_process = True
#         #validate user_input
#         while first_process:
#             try:
#                 user_input =to_get_user_input()
#                 int(input('enter the option to continue\n '))
#             except ValueError:
#                 print("Enter appropriate number!!")
#             else:
#                 first_process = False
# def to_get_user_name():
#         if user_input== 1:
#             nameenter = True
#             while nameenter:
#                 enter_name = str(input("ENTER YOUR FIRST NAME : "))
#                 try:# validate user input where name should be nothing other than alphabetic
#                     if enter_name.replace(" ","").isalpha():
#                         break
#                     else:
#                         raise ValueError('please enter your name only!!')# raise value error exception 
#                 except ValueError as Es:
#                     print(f"Error:{Es}")
#             number_test = True
#             while number_test:
#                 try:
#                     enter_phone = int(input('ENTER YOUR PHONE NUMBER: '))
#                 except ValueError:
#                     print(" Enter Number only!")
#                 else:
#                     number_test = False
#             add_test = True
#             while add_test:
#                 enter_address = str(input("ENTER YOUR ADDRESS : "))
#                 try:
#                     if enter_address.isalpha():
#                         break
#                     else:
#                         raise ValueError("please enter your address only!!!")
#                 except ValueError as ad:
#                     print(f" Please Only enter your address!!{ad}")

#             laplist = []
#             loop_fun = True
#             while loop_fun:
#                 read.Display()
#                 dicton = read.read_laptop()
#                 a = False
#                 lap_num = operation.num_select(dicton)
#                 if int(dicton[lap_num][3]) == 0:
#                     print("no stock")
#                     lop_1 = True
#                     while lop_1:
#                         ask = input("Do you want to continue y/n ")
#                         if ask.lower() == "y":
#                             lap_num = operation.num_select(dicton)
#                             lop_1 = False
#                         elif ask.lower() == "n":
#                             a = True
#                             break
#                         else:
#                             print("Appropriate values")
#                 if a :
#                     print("Thank you for using our software")
#                     break
#                 else:
#                     quantity_laptop=operation.laptopQuantity(dicton,lap_num)
#                     operation.updatedictionary(lap_num, dicton, quantity_laptop, laplist)
#                     write.update(dicton)
#                     loop = True
#                     while loop:
#                         yn = input("Do you want to continue(Y/N): ")
#                         if yn.upper() == "N":
#                             loop = False
#                             loop_fun = False
#                         elif yn.upper() == "Y":
#                             loop = False
#                         else:
#                             print("Enter appropriate choice")
#             if len(laplist) != 0:
#                 bill_num = random.randint(0, 1000)
#                 date = datetime.datetime.now().strftime("%d/%m/%Y")
#                 time = datetime.datetime.now().strftime("%H:%M/%S")
#                 write.bill_maker(enter_name, enter_address, enter_phone, laplist, bill_num, date, time)
#                 write.bill_creator(enter_name, enter_address, enter_phone, laplist, bill_num, date, time)

#         elif user_input == 2:
#             name_test1 = True
#             while name_test1:
#                 enter_name = str(input("ENTER YOUR FIRST NAME : "))
#                 try:
#                     if enter_name.isalpha():
#                         break
#                     else:
#                         raise ValueError('please enter your name only!!')
#                 except ValueError as Ea:
#                     print(f"Error:{Ea}")
#             loop_fun1 = True
#             laplist1 = []
#             dicton1 = read.read_laptop()
#             while loop_fun1:
#                 read.Display()
#                 lap_num = operation.num_select(dicton1)
#                 loop_3 = True
#                 while loop_3:
#                     try:
#                         quantity_laptop = int(input("Enter the quantity for the laptop you want to buy: "))
#                     except ValueError as ex:
#                         print("Enter numeric value")
#                     else:
#                         if quantity_laptop > 0:
#                             loop_3 = False
#                 while quantity_laptop <= 0:
#                     print("Enter appropriate values")
#                     quantity_laptop = int(input("Enter the laptop quantity you want to sell : "))
#                     operation.quantity_lap1()
#                 operation.updatedictionary1(lap_num, dicton1, quantity_laptop, laplist1)
#                 write.update(dicton1)
#                 loop = True
#                 while loop:
#                     yn = input("Do you want to continue(Y/N): ")
#                     if yn.upper() == "N":
#                         loop,loop_fun1 = False
#                     elif yn.upper() == "Y":
#                         loop = False
#                     else:
#                         print("Enter inappropriate choice")
#             bill_num = random.randint(0, 1000)
#             date = datetime.datetime.now().strftime("%d/%m/%Y")
#             time = datetime.datetime.now().strftime("%H:%M/%S")
#             write.bill_maker1(enter_name, laplist1, bill_num, date, time)
#             write.bill_creator1(enter_name, laplist1, bill_num, date, time)
#         elif user_input == 3:
#             user_input = False
#         elif user_input == "1":
#             print("Option 1 selected")
#         elif user_input == "2":
#             print("Option 2 selected")
#         else:
#             print(user_input, " is not the correct option ")
            
__name__ == "__main__"
