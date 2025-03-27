# -*- coding: latin_1 -*-

# python uibudgettracker.py

import csv
import os
import ttkbootstrap as ttk
import tkinter as tk
# from tkinter import Button, ttk

# Creates window
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
    with open("income.csv", "w", newline="", encoding = "latin_1") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount"])
        for item in incomelist:
            print(item)
            writer.writerow([item["Amount"]])

def SaveExpenses():
    with open("expense.csv", "w", newline="", encoding = "latin_1") as big:
        writer = csv.writer(big)
        writer.writerow(["Amount"])
        for item in expenselist:
            writer.writerow([item["Amount"]])

def LoadData():
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
                    incomelist.append({"Amount": amount})
    else:
        SaveIncome()
    if os.path.exists("expense.csv"):
        with open("expense.csv", "r") as big:
            reader = csv.reader(big)
            next(reader)
            expenselist = []
            for row in reader:
                if len(row) == 2:
                    amount = float(row[0])
                    category = (row[1])
                    expenselist.append({"Amount": amount})
    else:
        SaveExpenses()

Window = tk.Tk()
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

# Output 



# Runs the window
Window.mainloop()