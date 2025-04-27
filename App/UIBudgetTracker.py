
# -*- coding: utf-8 -*-

# @ author Milo Mitchell-Brooks
# @ Version 1
# @BudgetTracker using UI

# Imports
import tkinter as tk
from tkinter import ttk
import pandas as pd
from ttkbootstrap import Style
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Setting up window
Main = tk.Tk()
Main.geometry("1920x1080")
Main.title("Budget Tracker")
Frame = ttk.Frame(Main, width = 100, height = 200)


# Dataframes
dfIncome = pd.DataFrame(columns = ["Amount", "Category"])
dfExpense = pd.DataFrame(columns = ["Amount", "Category"])

# Save data
def SaveData():
    dfExpense.to_csv("expense.csv", index = False)
    dfIncome.to_csv("income.csv", index = False)

# Load files
try: 
    dfIncome = pd.read_csv("income.csv")
except FileNotFoundError:
    SaveData()
    
try:
    dfExpense = pd.read_csv("expense.csv")
except FileNotFoundError:
    SaveData()

  

# Variables
fIncomeAmount = tk.DoubleVar()
fExpenseAmount = tk.DoubleVar()
szIncomeCategory = tk.StringVar()
szExpenseCategory = tk.StringVar()
szInfomation = tk.StringVar()


# Label
MainLabel = ttk.Label(master = Frame, text = "Budget Tracker")
MainLabel.pack(pady = 10)

# Income Functionality
def AddIncomeInfo():
    fAmount = 0.0
    szCategory = ""
    dfIncome["Category"] = dfIncome["Category"].astype("string")

    
    fAmount = fIncomeAmount.get()

    # Income Entry
    IncomeEntry.config(text = "Enter Category", textvariable = szIncomeCategory)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Category")
    IncomeButton.pack(pady = 0, padx = 10)

    szCategory = szIncomeCategory.get()
    
    
    if len(szCategory) != 0:
        # Saves to dataframe
        dfIncome.loc[len(dfIncome)] = [fAmount, szCategory.lower()]
        SaveData()

        # Resetting GUI
        ResetIncomeUI()
        print(dfIncome)
def ResetIncomeUI():
    # Income Entry
    IncomeEntry.config(text = "Enter Income", textvariable = fIncomeAmount)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Income", command = AddIncomeInfo)
    IncomeButton.pack(pady = 0, padx = 10)
    fIncomeAmount.set("")
    szIncomeCategory.set("")

# IncomeEntry
IncomeEntry = ttk.Entry(master = Frame, text = "Enter Income", textvariable = fIncomeAmount)
IncomeEntry.pack(pady = 20)

# IncomeButton
IncomeButton = ttk.Button(master = Frame, text = "Add Income", command = AddIncomeInfo)
IncomeButton.pack(pady = 0, padx = 10)


# Expense Functionality
def AddExpenseInfo():
    fAmount = 0.0
    szCategory = ""
    dfExpense["Category"] = dfExpense["Category"].astype("string")

    
    fAmount = fExpenseAmount.get()

    # Expense Entry
    ExpenseEntry.config(text = "Enter Category", textvariable = szExpenseCategory)
    ExpenseEntry.pack(pady = 20)

    # Expense Button
    ExpenseButton.config(text = "Add Category",)
    ExpenseButton.pack(padx = 10)

    szCategory = szExpenseCategory.get()
    
    
    if len(szCategory) != 0:
        # Saves to dataframe
        dfExpense.loc[len(dfExpense)] = [fAmount, szCategory.lower()]
        SaveData()
        
        # Resetting GUI
        ResetExpenseUI()
        print(dfExpense)
def ResetExpenseUI():
    # ExpenseEntry
    ExpenseEntry.config(text = "Enter Expense", textvariable = fExpenseAmount)
    ExpenseEntry.pack(pady = 20)

    # ExpenseButton
    ExpenseButton.config(text = "Add Expense", command = AddExpenseInfo)
    ExpenseButton.pack(pady = 0, padx = 10)

    fExpenseAmount.set("")
    szExpenseCategory.set("")

# Expense Entry
ExpenseEntry = ttk.Entry(master = Frame, text = "Enter Expense", textvariable = fExpenseAmount)
ExpenseEntry.pack(pady = 20)

# Expense Button
ExpenseButton = ttk.Button(master = Frame, text = "Add Expense", command = AddExpenseInfo)
ExpenseButton.pack(pady = 0, padx = 10)


# Clear Data Functionality
def ClearData():
    global dfExpense, dfIncome
    dfExpense = pd.DataFrame(columns = ["Amount", "Category"])
    dfIncome = pd.DataFrame(columns = ["Amount", "Category"])
    SaveData()
    AllInfo()

# Clear Data Button
ClearDataButton = ttk.Button(master = Frame, text = "Clear Data", command = ClearData)
ClearDataButton.pack(pady = 10)


# Infomation Functionality
def AllInfo():
    fTotalIncome = dfIncome["Amount"].sum()
    fTotalExpense = dfExpense["Amount"].sum()
    fBalance = fTotalIncome - fTotalExpense
    szInfomation.set(f"Total Income: {fTotalIncome:.2f} | Total Expenses: {fTotalExpense:.2f} | Balance: {fBalance:.2f}")

# Infomation Button
InfomationButton = ttk.Button(master = Frame, text = "All info", command = AllInfo)
InfomationButton.pack(pady = 10)

# Infomation Output
InfomationOutput = ttk.Label(master = Frame, textvariable = szInfomation)
InfomationOutput.pack(pady = 50)















    



    
    

    



























Frame.pack()
Main.mainloop()



