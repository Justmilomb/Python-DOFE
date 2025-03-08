import os
import time 
import csv

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
    time.sleep(0.5)
    print("Choose 1 to add an income")
    time.sleep(0.5)
    print("Choose 2 to add an expense")
    time.sleep(0.5)
    print("Choose 3 to view you're balance")
    time.sleep(0.5)
    print("Choose 4 to clear all data")    
    time.sleep(0.5)
    print("Choose 5 to exit the program")
    time.sleep(0.5)
    chosen = input("What number do you choose?\n")
    if chosen == "1":
        income()
    elif chosen == "2":
        expense()
    elif chosen == "3":
        balance()
    elif chosen == "4":
        cleardata()
    elif chosen == "5":
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
    while True:
        try:
            amount = float(input("Enter income amount\n"))
        except ValueError:
            print("Please enter a numerical number")
            time.sleep(1)
            income()
        category = input("What category would this income be under?\n")
        incomelist.append({"Amount": amount,"Category": category})
        print(f"£{amount} has been saved under the category {category}")
        time.sleep(2)
        saveincome()
        mainmenu()

def expense():
    clearterminal()
    while True:
        try:
            amount = float(input("Enter expense amount\n"))     
        except ValueError:
            print("Please enter a numerical number")
            time.sleep(1)
            expense()
        category = input("What category would this expense be under?\n")
        expenselist.append({"Amount": amount,"Category": category})
        print(f"£{amount} has been saved under the category {category}")
        time.sleep(2)
        saveexpense()
        mainmenu()

def balance():
    clearterminal()
    totalincome = sum(item["Amount"] for item in incomelist)
    totalexpense = sum(item["Amount"] for item in expenselist)
    balance = totalincome - totalexpense
    print("-----Financial Summary------")
    print(f"Total Income: £{totalincome}")
    print(f"Total Expenses: £{totalexpense}")
    if balance >= 0:
        print(f"Overall Balance: £{balance}")
        print("Well done your saving money!")
        time.sleep(1)
        exit = input("Ready to go back?\n'Y' or 'N'\n")
        if exit == "y".strip().lower():
            mainmenu()
        elif exit == "n".strip().lower():
            balance()
        else:
            print("INVALID Input")
            balance()
        
    else:
        print(f"Overall Balance: £{balance}")
        print("Your in debt. You need to spend less?")
        time.sleep(1)
        exit = input("Ready to go back?\n'Y' or 'N'\n")
        if exit == "y".strip().lower():
            mainmenu()
        elif exit == "n".strip().lower():
            balance()
        else:
            print("INVALID Input")
            balance()
        
    

def exit():
    while True:
        clearterminal()
        exit = input("Are you sure you want to leave?\n 'Y' or 'N'\n")
        if exit == "y".strip().lower():
            exit()
        elif exit == "n".strip().lower():
            print("Going back to menu...")
            time.sleep(1)
            mainmenu()
        else:
            clearterminal()
            print("INVALID Input")
            time.sleep(1)

def saveincome():
    with open("income.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category"])
        for item in incomelist:
            writer.writerow([item["Amount"],item["Category"]])

def saveexpense():
    with open("expense.csv", "w", newline="") as big:
        writer = csv.writer(big)
        writer.writerow(["Amount", "Category"])
        for item in expenselist:
            writer.writerow([item["Amount"],item["Category"]])

def loaddata():
    global expenselist, incomelist
    if os.path.exists("income.csv"):
        with open("income.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            incomelist = []
            for row in reader:
                if len(row) == 2:
                    amount = float(row[0])
                    category = (row[1])
                    incomelist.append({"Amount": amount, "Category": category})
    else:
        saveincome()
    if os.path.exists("expense.csv"):
        with open("expense.csv", "r") as big:
            reader = csv.reader(big)
            next(reader)
            expenselist = []
            for row in reader:
                if len(row) == 2:
                    amount = float(row[0])
                    category = (row[1])
                    expenselist.append({"Amount": amount, "Category": category})
    else:
        saveexpense()

def cleardata():
    clearterminal()
    global expenselist, incomelist
    incomelist = []
    expenselist = []
    saveexpense()
    saveincome()
    loaddata()
    print("Data has been wiped")
    time.sleep(0.5)
    print("Going back to menu now")
    time.sleep(1)
    mainmenu()



loaddata()        
mainmenu()
