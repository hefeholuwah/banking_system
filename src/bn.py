import datetime
import random
import string
import os

x= datetime.datetime.now()


menu_= True
def login():
    while menu_:
        print("***************************************")
        username = input("please enter your username:")
        print("***************************************")
        password = input("please enter your password:")
        staff = open("staff1.txt",'r')
        content=staff.seek(0)
        content= staff.readlines()
        content=[i.rstrip("\n") for i in content]
        content=[i.split(' ') for i in content]
        content.remove([''])
        # a= content[0][0],content[1][0]
        # b= content[0][1],content[1][1]
        usern = []
        passw = []
        for i in content:
            usern.append(i[0])
            passw.append(i[1])
        if username in usern and password == passw[usern.index(username)]:
            print("login successful")
            user= open("session.txt",'w')
            use_= user.write(username + " logged in at " + x.strftime("%Y-%B-%A:%H:%M:%S") + ("\n"))
            user.close()
            break
        else:
            print("incorrect credentials")
    return False
        
    


def menu():
    print("***********WELCOME TO First BANK*************")
    main_menu = ["1-staff login","2-close App"]
    for i in main_menu:
        print(i+"\n")
    opt = True     
    while opt:
        command = (input("please select your option:"))
        if command == "1":
            login()
            break
        elif command == "2":
            print("Close")
            exit()
        else:
            print("invalid input please try again")


main_menu = ["1-staff login","2-close App"]
menu()

print("-------------------------------------------------------")

values = ''.join(random.choices(string.digits, k=10))
    



def create():
    AN = input("please input your account name:")
    print("***************************************")
    OB = float(input("please input your opening balance: $ "))
    print("***************************************")
    AT = input("please input your account type:")
    print("***************************************")
    AE =input("please input your account email:")
    global values
    print("below is your account number")
    print(values)
    cust= open("customer.txt",'w')
    arr= [AN,str(OB),AT,AE,str(values)]
    for item in arr:
        cust.write(item+"\n")
    cust.close()  

def check():
    number= int(input("please input your account Number:"))
    numbers= str(number)
    global values
    if numbers == int(values):
         details= open("customer.txt",'r')
         detail = [i.rstrip("\n") for i in details]
         detail= details.seek(0)
         detail= details.read()
         print(detail)
         
    else:
        menu()
    

def logout():
    os.remove("session.txt")
    menu()
    

Login_ = ["O-create new bank account","C-check account details","L-logout"]
for i in Login_:
    print(i+"\n")
opt= True
while opt:
    command_ = (input("please input your option:"))
    if command_ == "O":
        create()
    elif command_ == "C":
        check()
    elif command_ == "L":
        logout()
    else:
        print ("invalid input")
      
               

    
    




    

    
              





staff = open("staff1.txt",'r')
content=staff.seek(0)
content=staff.read()
staff.close()

customers = open("customer.txt",'r')
path=customers.seek(0)
path=customers.read()
customers.close()


Login_ = ["1-create new bank account","2-check account details","3-logout"]

