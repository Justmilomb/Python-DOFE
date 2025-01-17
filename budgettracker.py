import os
import time 
expenses = []

def loadexpenses():
    if not os.path.exists("expenses.txt"):
        open("expenses.txt", "w").close()
        return
    with open("expenses.txt", "r") as file:
        for line in file:
            expenses.append(line.strip())
            return

def saveexpenses():
    with open("expenses.txt", "w") as file:
        for amount in expenses:
            file.write(amount + "\n")

def clearterminal():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def addtransaction():
    name = input("What do you want to list this as...\n")
    category = input("Enter the category of your expenses... \n")
    amount = float(input("Enter your amount\nPS. Use negative numbers for expenditures"))
    expenses.append({'name': name,'category': category, 'amount': amount })
    print(f"Expense: {name}\nCategory: {category}\nAmount: :{amount} ")

loadexpenses()
addtransaction()
    