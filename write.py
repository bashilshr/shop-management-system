import read
def update(diction):
    file=open("laptops.txt","w")
    for i in diction.values():
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
        file.write("\n")
    file.close()

def bill_maker(name,address,phone,list,bill_num,date,time):
    global transport

    loop= True
    while loop:
        transport = input("Do you want transportation: ").upper()
        if transport == "y":
            loop = False
        elif transport =="n":
            loop = False
        else:
            print("we have not that function to perform... reenter your choice")

    total_price = 0
    read.header()
    print(f"\t\t\tdate  : {date}")
    print(f"\t\t\tBill No: {bill_num}")
    print(f"\t\t\tName : {name}")
    print(f"\t\t\tPhone : {phone}")
    print(f"\t\t\tBill No: {bill_num}")
    print(f"\t\t\tAddress {address}")
    print(f"\t\t\tTime: {time}")
    for y in range(len(list)):
        value = list[y][1].replace('',"")
        print(f"Laptop Name: {list[y][0]}\t\tlaptop brand :{value}")
        price = list[y][2].replace(" ","")
        print(f"price : {price}\t\t\t quantity: {list[y][4]}")
        print(f"Total price : {list[y][3]}")
        total_price = total_price + int(list[y][3])
        print("\n")
    if transport == y:
        print(f"Transport fee: {250}")
        print(f"Total : {total_price}")
        print(f"Grand Total : {total_price+250}")
    else:
        print(f"Grand total: {total_price}")

def bill_maker1(name,list,bill_num,date,time):
    read.header()
    print(f"\t\t\tdate  : {date}")
    print(f"\t\t\ttime :{time}")
    print(f"\t\t\tBill No: {bill_num}")
    print(f"\t\t\tName : {name}")
    total_price = 0
    for y in range(len(list)):
        value = list[y][1].replace('', "")
        print(f"Laptop Name: {list[y][0]}\t\tlaptop brand :{value}")
        price = list[y][2].replace(" ", "")
        print(f"price : {price}\t\t\t quantity: {list[y][4]}")
        print(f"Total price : {list[y][3]}")
        total_price = total_price + int(list[y][3])
        print("\n")
        print(f"VAT percent: {0.13}")
        print(f"VAT amount : {total_price * 0.13}")
        print(f"Grand Total : {total_price + (0.13 * total_price)}")


def bill_creator1(name,list,bill_num,date,time):

    file = open(f"{bill_num}.txt", "w")
    file.write("\n")
    file.write("\t \t \t \t \t Islington Electronics")  # one tab space
    file.write("\n")
    file.write("\t \t \t \t  putalisadak,kathmandu,| 9869274740")
    file.write("\n")

    file.write("----------------------------------------------------------------------------------------------------------")
    file.write("\t \t \t \t Welcome to our store, and we are glad to you are here!!")
    file.write("----------------------------------------------------------------------------------------------------------")
    file.write("\n")

    file.write(f"\t\t\tdate  : {date}")
    file.write(f"\t\t\ttime :{time}")
    file.write(f"\t\t\tBill No: {bill_num}")
    file.write(f"\t\t\tName : {name}")
    total_price = 0
    for y in range(len(list)):
        value = list[y][1].replace('',"")
        file.write(f"Laptop Name: {list[y][0]}\t\tlaptop brand :{value}")
        price = list[y][2].replace(" ","")
        file.write(f"price : {price}\t\t\t quantity: {list[y][4]}")
        file.write(f"Total price : {list[y][3]}")
        total_price = total_price + int(list[y][3])
        file.write("\n")
        file.write(f"VAT percent: {0.13}")
        file.write(f"VAT amount : {total_price *0.13}")
        file.write(f"Grand Total : {total_price+(0.13*total_price)}")
        
def bill_creator(name,address,phone,list,bill_num,date,time):
    file= open(f"{bill_num}.txt","w")
    file.write(f"\t\t\tdate  : {date}")
    file.write(f"\t\t\tBill No: {bill_num}")
    file.write(f"\t\t\tName : {name}")
    file.write(f"\t\t\tPhone : {phone}")
    file.write(f"\t\t\tBill No: {bill_num}")
    file.write(f"\t\t\tAddress {address}")
    total_price = 0
    for y in range(len(list)):
        value = list[y][1].replace('', "")
        file.write(f"Laptop Name: {list[y][0]}\t\tlaptop brand :{value}")
        price = list[y][2].replace(" ", "")
        file.write(f"price : {price}\t\t\t quantity: {list[y][4]}")
        file.write(f"Total price : {list[y][3]}")
        total_price = total_price + int(list[y][3])
        file.write("\n")
    if transport == y:
        file.write(f"Transport fee: {250}")
        file.write(f"Total : {total_price}")
        file.write(f"Grand Total : {total_price + 250}")
    else:
        file.write(f"Grand total: {total_price}")
