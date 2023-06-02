def loop(l):
    loop = True
    while loop:
        yn = input("Do you want to continue(Y/N): ")
        if yn.upper() == "N":
            l = False
            loop = False
            return False
        elif yn.upper() == "Y":
            loop = False
            l = True
            return l
        else:
            print("Enter appropriate choice")
            print(l)
def updict(lap_num,dicton,quantity_laptop,laplist):
    value = int(dicton[lap_num][3])
    if value >= quantity_laptop:
        dicton[lap_num][3] = value - quantity_laptop
        price = quantity_laptop * int(dicton[lap_num][2].replace("$", ""))
    laplist.append([dicton[lap_num][0],dicton[lap_num][1],dicton[lap_num][2],price,quantity_laptop])

def updict1(lap_num,dicton,quantity_laptop,laplist1):
    value = int(dicton[lap_num][3])
    dicton[lap_num][3] = value + quantity_laptop
    price1 = quantity_laptop * int(dicton[lap_num][2].replace("$",""))
    laplist1.append([dicton[lap_num][0],dicton[lap_num][1],dicton[lap_num][2],price1,quantity_laptop])

def num_select(dict):
    lop_test = True
    while lop_test:
            try:
                lap_num = int(input('Enter laptop Number: '))
            except ValueError:
                print("Reenter your input")
            else:

                if lap_num>0 and lap_num<=len(dict):
                    lop_test = False
    return lap_num

def quantity_lap(dict,lap_num):
    lop_test = True
    while lop_test:
        try:
            quantity_laptop = int(input("Enter the laptop quantity you want to buy : "))
        except ValueError:
            print("Reenter your input")
        else:

            if quantity_laptop> 0 and quantity_laptop <= int(dict[lap_num][3]):
                lop_test = False
    return quantity_laptop
def quantity_lap1(dict,lap_num):
    lop_test = True
    while lop_test:
        try:
            quantity_laptop = int(input("Enter the laptop quantity you want to buy : "))
        except ValueError:
            print("Re-enter your input")
        else:

             if quantity_laptop<=0:
                lop_test = False
    return quantity_laptop