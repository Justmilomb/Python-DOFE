import os
import time 
incomelist = []
expenselist = []

def clearterminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mainmenu():
    clearterminal()
    print("Welcome to you're Budget-Tracker\nLets get started...")
    time.sleep(1.5)
    print("Choose 1 to add an income")
    time.sleep(0.5)
    print("Choose 2 to add an expense")
    time.sleep(0.5)
    print("Choose 3 to view you're balance")
    time.sleep(0.5)
    print("Choose 4 to exit the program")    
    time.sleep(0.5)
    chosen = input("What number do you choose?\n")
    if chosen == "1":
        income()
    elif chosen == "2":
        expense()
    elif chosen == "3":
        balance()
    elif chosen == "4":
        exit()
    else: 
        clearterminal()
        print("INVALID")
        time.sleep(0.5)
        print("Choose a number between 1-4")
        time.sleep(1)
        mainmenu()

def income():
    clearterminal()
    try:
        amount = float(input("Enter income amount\n"))
    except ValueError:
        print("Please enter a numerical number")
        time.sleep(1)
        income()
    category = input("What category would this be under?\n")
    incomelist.append({"Amount": amount,"Category": category})
    print(f"£{amount} has been saved under the category {category}")
    mainmenu()

def expense():
    clearterminal()
    try:
        amount = float(input("Enter expense amount\n"))
    except ValueError:
        print("Please enter a numerical number")
        time.sleep(1)
        expense()
    category = input("What category would this be under?\n")
    expenselist.append({"Amount": amount,"Category": category})
    print(f"£{amount} has been saved under the category {category}")
    mainmenu()

def balance():
    



mainmenu()