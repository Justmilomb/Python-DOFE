# -*- coding: latin_1 -*-

# python uibudgettracker.py
Overall1 = ""
import csv
import os
import ttkbootstrap as ttk
import tkinter as tk

def Expense():
    print(ExpenseEntryInt.get())
    ExpenseOutput.set(f"£{ExpenseEntryInt.get()} has been added as a expense")
    Amount = ExpenseEntryInt.get()
    expenselist.append({"Amount": Amount})
    print(expenselist)
    SaveExpenses()

def Income():
    print(IncomeEntryInt.get())
    IncomeOutput.set(f"£{IncomeEntryInt.get()} has been added as a income")
    Amount = IncomeEntryInt.get()
    incomelist.append({"Amount": Amount})
    print(incomelist)
    SaveIncome()

def SaveIncome():
    FileExists = os.path.exists("income.csv")
    with open("income.csv", "w", newline="", encoding = "latin_1") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount"])
        for item in incomelist:
            writer.writerow([item["Amount"]])

def SaveExpenses():
    FileExists = os.path.exists("expense.csv")
    with open("expense.csv", "w", newline="", encoding = "latin_1") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount"])
        for item in expenselist:
            writer.writerow([item["Amount"]])

def LoadData():
    global expenselist, incomelist
    incomelist.clear()
    expenselist.clear()
    if os.path.exists("income.csv"):
        with open("income.csv", "r", encoding = "latin_1") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                amount = float(row[0])
                incomelist.append({"Amount": amount})

    if os.path.exists("expense.csv"):
        with open("expense.csv", "r", encoding = "latin_1") as big:
            reader = csv.reader(big)
            next(reader, None)
            for row in reader:
                amount = float(row[0])
                expenselist.append({"Amount": amount})


def total():
    global Overall1
    LoadData()
    totalincome = sum(item["Amount"] for item in incomelist)
    totalexpense = sum(item["Amount"] for item in expenselist)
    Overall1.set(f"Total Income: £{totalincome} : Total Expenses: £{totalexpense}")


def ClearData():
    incomelist.clear()
    expenselist.clear()
    SaveExpenses()
    SaveIncome()


Window = ttk.Window(themename = "darkly")
Window.title("Productivity")
Window.geometry("1920x1080")
incomelist = []
expenselist = []
LoadData()
# Title
TitleLable = ttk.Label(master = Window, text = "Budget Tracker", font = "calibri 24 bold")
TitleLable.pack() 

# Input income
InputFrameIncome = ttk.Frame(master = Window)
IncomeOutput = tk.StringVar()
IncomeEntryInt = tk.IntVar()
IncomeEntry = ttk.Entry(master = InputFrameIncome, textvariable = IncomeEntryInt)
IncomeButton = ttk.Button(master = InputFrameIncome, text = "Add Income", command = Income)
IncomeEntry.pack(side = "left", padx = 10)
IncomeButton.pack(side = "left", padx = 10)
InputFrameIncome.pack(pady = 20)

# Output income
IncomeOutput = tk.StringVar()
OutputFrameIncome = ttk.Frame(master = Window)
OutputIncomeText = ttk.Label(master = OutputFrameIncome, textvariable = IncomeOutput)
OutputIncomeText.pack()
OutputFrameIncome.pack(pady = 12.5)

# Input expense
InputFrameExpense = ttk.Frame(master = Window)
ExpenseOutput = tk.StringVar()
ExpenseEntryInt = tk.IntVar()
ExpenseEntry = ttk.Entry(master = InputFrameExpense, textvariable = ExpenseEntryInt)
ExpenseButton = ttk.Button(master = InputFrameExpense, text = "Add Expense", command = Expense)
ExpenseEntry.pack(side = "left", padx = 10)
ExpenseButton.pack(side = "left", padx = 10)
InputFrameExpense.pack(pady = 20)

# Output expense
OutputFrameExpense = ttk.Frame(master = Window)
OutputExpenseText = ttk.Label(master = OutputFrameExpense, textvariable = ExpenseOutput)
OutputExpenseText.pack()
OutputFrameExpense.pack(pady = 12.5)

# Output info
Overall1 = tk.StringVar()
OutputFrameConclusion = ttk.Frame(master = Window)
OutputFrameText = ttk.Label(master = OutputFrameConclusion, textvariable = Overall1)
InfoButton = ttk.Button(master = OutputFrameConclusion, text = "All info", command = total)
OutputFrameText.pack()
InfoButton.pack()
OutputFrameConclusion.pack(pady = 12.5)

# Input clear data
ClearDataFrame = ttk.Frame(master = Window)
ClearDataButton = ttk.Button(master = ClearDataFrame, text = "Clear Data", command = ClearData)
ClearDataButton.pack()
ClearDataFrame.pack(pady = 12.5)



# Runs the window
Window.mainloop()