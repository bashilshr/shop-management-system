def read_laptop():
    laptops={} #dictionary for storing the content of files
    File = open('laptops.txt','r')#opening the laptop file using read mode
    lap_id = 1 #to keep track of laptop's ID
    for a in File:#iteration infinite.
        a = a.replace('\n', '')#repalcing space with n\.
        laptops. update({lap_id: a.split(',')})

        lap_id += 1
    File.close()
    return laptops

def Display():
    i = 1
    file = open ('laptops.txt','r')
    print('|========================================================================================================|')
    print('SN''\t',"Name",'\t\t\t\t','Brand',"\t\t\t",'Price',"\t", "Quantity",'\t\t',"Processor","\t\t","Graphics card")
    print('|========================================================================================================|')
    for lap in file: 
        print(i, '\t'+ lap.replace(',',"\t\t"))
        i = i+1
    return lap
def header():
    print("\n")  # one tab down
    print("\n")
    print("\t \t \t \t \t Islington Electronics")
    print("\n")
    print("\t \t \t \t  Putalisadak,Kathmandu,| 9869274740")
    print("\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t Welcome to our store, and we are glad to you are here!!")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n")

