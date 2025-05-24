
# -*- coding: utf-8 -*-

# @ author Milo Mitchell-Brooks
# @ Version 1
# @BudgetTracker using UI

# Imports
import tkinter as tk
from tkinter import ttk
import pandas as pd
from ttkbootstrap import Style




# Setting up window
Main = tk.Tk()
Main.geometry("1920x1080")
Main.title("Budget Tracker")
Frame = ttk.Frame(Main, width = 100, height = 200)


# Dataframes
dfIncome = pd.DataFrame(columns = ["Amount", "Category"])
dfExpense = pd.DataFrame(columns = ["Amount", "Category"])
dfIncomeGrouped = pd.DataFrame(columns = [])

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
szIncomeCategoryInput = tk.StringVar()
szExpenseCategoryInput = tk.StringVar()
szIncomeCategoryOutput = tk.StringVar()
szExpenseCategoryOutput = tk.StringVar()
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
    IncomeEntry.config(text = "Enter Category", textvariable = szIncomeCategoryInput)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Category")
    IncomeButton.pack(pady = 0, padx = 10)

    szCategory = szIncomeCategoryInput.get()
    
    szIncomeCategoryInput.set("")
    if len(szCategory) != 0:
        # Saves to dataframe
        dfIncome.loc[len(dfIncome)] = [fAmount, szCategory.lower()]
        SaveData()

        # Resetting GUI
        ResetIncomeUI()
        print(dfIncome)
        AllInfo()
def ResetIncomeUI():
    # Income Entry
    IncomeEntry.config(text = "Enter Income", textvariable = fIncomeAmount)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Income", command = AddIncomeInfo)
    IncomeButton.pack(pady = 0, padx = 10)
    fIncomeAmount.set("")
    szIncomeCategoryInput.set("")

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
    ExpenseEntry.config(text = "Enter Category", textvariable = szExpenseCategoryInput)
    ExpenseEntry.pack(pady = 20)

    # Expense Button
    ExpenseButton.config(text = "Add Category", command = AddExpenseInfo)
    ExpenseButton.pack(padx = 10)

    szCategory = szExpenseCategoryInput.get()
    
    
    if len(szCategory) != 0:
        # Saves to dataframe
        dfExpense.loc[len(dfExpense)] = [fAmount, szCategory.lower()]
        SaveData()
        
        # Resetting GUI
        ResetExpenseUI()
        print(dfExpense)
    AllInfo()
def ResetExpenseUI():
    # ExpenseEntry
    ExpenseEntry.config(text = "Enter Expense", textvariable = fExpenseAmount)
    ExpenseEntry.pack(pady = 20)

    # ExpenseButton
    ExpenseButton.config(text = "Add Expense", command = AddExpenseInfo)
    ExpenseButton.pack(pady = 0, padx = 10)

    fExpenseAmount.set("")
    szExpenseCategoryInput.set("")

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
ClearDataButton.pack(pady = 50)


# Infomation Functionality
def AllInfo():
    global dfIncomeGrouped, dfExpenseGrouped
    fTotalIncome = dfIncome["Amount"].sum()
    fTotalExpense = dfExpense["Amount"].sum()
    fBalance = fTotalIncome - fTotalExpense
    szInfomation.set(f"Total Income: {fTotalIncome:.2f} | Total Expenses: {fTotalExpense:.2f} | Balance: {fBalance:.2f}")
    if dfIncome.empty:
        szIncomeCategoryOutput.set("")
    else:
        dfIncomeGrouped = dfIncome.groupby("Category", as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)
        szIncomeCategoryOutput.set(dfIncomeGrouped)
        IncomeOverall = ["------------Income------------"]
        for index, row in dfIncomeGrouped.iterrows():
            szCategory = row["Category"]
            szAmount = row["Amount"]
            IncomeOverall.append(f"Amount: {szAmount} || Category: {szCategory}")
            szIncomeCategoryOutput.set("\n".join(IncomeOverall))
    if dfExpense.empty:
        szExpenseCategoryOutput.set("")
    else:
        dfExpenseGrouped = dfExpense.groupby("Category", as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)
        szExpenseCategoryOutput.set(dfExpenseGrouped)
        ExpenseOverall = ["------------Expense------------"]
        for index, row in dfExpenseGrouped.iterrows():
            szCategory = row["Category"]
            szAmount = row["Amount"]
            ExpenseOverall.append(f"Amount: {szAmount} || Category: {szCategory}")
            szExpenseCategoryOutput.set("\n".join(ExpenseOverall))
        

# Infomation Button
InfomationButton = ttk.Button(master = Frame, text = "All info", command = AllInfo)
InfomationButton.pack(pady = 10)

# Infomation Output
InfomationOutput = ttk.Label(master = Frame, textvariable = szInfomation)
InfomationOutput.pack(pady = 25)
CategoryOutputIncome = ttk.Label(master = Frame, textvariable = szIncomeCategoryOutput)
CategoryOutputIncome.pack(pady = 10)
CategoryOutputExpense = ttk.Label(master = Frame, textvariable = szExpenseCategoryOutput)
CategoryOutputExpense.pack(pady = 10)















    



    
    

    



























Frame.pack()
Main.mainloop()



