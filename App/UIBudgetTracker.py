
# -*- coding: utf-8 -*-

# @ author Milo Mitchell-Brooks
# @ Version 1
# @BudgetTracker using UI

# Imports
import tkinter as tk
import pandas as pd


# Setting up window
Main = tk.Tk()
Main.geometry("1920x1080")
Main.title("Budget Tracker")
Frame = tk.Frame(Main, width = 100, height = 200)


# Dataframes
dfIncome = pd.DataFrame(columns = ["Amount", "Category"])
dfExpense = pd.DataFrame(columns = ["Amount", "Category"])


# Variables
fltIncomeAmount = tk.DoubleVar()
fltExpenseAmount = tk.DoubleVar()
szIncomeCategory = tk.StringVar()
szExpenseCategory = tk.StringVar()
szInfomation = tk.StringVar()


# Label
MainLabel = tk.Label(master = Frame, text = "Budget Tracker", font=("Arial", 25))
MainLabel.pack(pady = 10)


# Income Functionality
def AddIncomeInfo():
    fltAmount = 0.0
    szCategory = ""
    dfIncome["Category"] = dfIncome["Category"].astype("string")

    
    fltAmount = fltIncomeAmount.get()

    # Income Entry
    IncomeEntry.config(text = "Enter Category", textvariable = szIncomeCategory)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Category", font = ("Arial", 12))
    IncomeButton.pack(pady = 0, padx = 10)

    szCategory = szIncomeCategory.get()
    
    
    if len(szCategory) != 0:
        # Saves to dataframe
        dfIncome.loc[len(dfIncome)] = [fltAmount, szCategory.lower()]
        
        # Resetting GUI
        ResetIncomeUI()
        print(dfIncome)
def ResetIncomeUI():
    # Income Entry
    IncomeEntry.config(text = "Enter Income", textvariable = fltIncomeAmount)
    IncomeEntry.pack(pady = 20)

    # Income Button
    IncomeButton.config(text = "Add Income", font = ("Arial", 12), command = AddIncomeInfo)
    IncomeButton.pack(pady = 0, padx = 10)
    fltIncomeAmount.set("")
    szIncomeCategory.set("")

# IncomeEntry
IncomeEntry = tk.Entry(master = Frame, text = "Enter Income", textvariable = fltIncomeAmount)
IncomeEntry.pack(pady = 20)

# IncomeButton
IncomeButton = tk.Button(master = Frame, text = "Add Income", font = ("Arial", 12), command = AddIncomeInfo)
IncomeButton.pack(pady = 0, padx = 10)


# Expense Functionality
def AddExpenseInfo():
    fltAmount = 0.0
    szCategory = ""
    dfExpense["Category"] = dfExpense["Category"].astype("string")

    
    fltAmount = fltExpenseAmount.get()

    # Expense Entry
    ExpenseEntry.config(text = "Enter Category", textvariable = szExpenseCategory)
    ExpenseEntry.pack(pady = 20)

    # Expense Button
    ExpenseButton.config(text = "Add Category", font = ("Arial", 12))
    ExpenseButton.pack(padx = 10)

    szCategory = szExpenseCategory.get()
    
    
    if len(szCategory) != 0:
        # Saves to dataframe
        dfExpense.loc[len(dfExpense)] = [fltAmount, szCategory.lower()]
        # Resetting GUI
        ResetExpenseUI()
        print(dfExpense)
def ResetExpenseUI():
    # ExpenseEntry
    ExpenseEntry.config(text = "Enter Expense", textvariable = fltExpenseAmount)
    ExpenseEntry.pack(pady = 20)

    # ExpenseButton
    ExpenseButton.config(text = "Add Expense", font = ("Arial", 12), command = AddExpenseInfo)
    ExpenseButton.pack(pady = 0, padx = 10)

    fltExpenseAmount.set("")
    szExpenseCategory.set("")

# Expense Entry
ExpenseEntry = tk.Entry(master = Frame, text = "Enter Expense", textvariable = fltExpenseAmount)
ExpenseEntry.pack(pady = 20)

# Expense Button
ExpenseButton = tk.Button(master = Frame, text = "Add Expense", font = ("Arial", 12), command = AddExpenseInfo)
ExpenseButton.pack(pady = 0, padx = 10)


# Clear Data Functionality
def ClearData():
    global dfExpense, dfIncome
    dfExpense = pd.DataFrame(columns = ["Amount", "Category"])
    dfIncome = pd.DataFrame(columns = ["Amount", "Category"])

# Clear Data Button
ClearDataButton = tk.Button(master = Frame, text = "Clear Data", command = ClearData)
ClearDataButton.pack(pady = 10)


# Infomation Functionality
def AllInfo():
    fltTotalIncome = dfIncome["Amount"].sum()
    fltTotalExpense = dfExpense["Amount"].sum()
    fltBalance = fltTotalIncome - fltTotalExpense
    szInfomation.set(f"Total Income: ${fltTotalIncome:.2f} | Total Expenses: {fltTotalExpense:.2f} | Balance: {fltBalance:.2f}")

# Infomation Button
InfomationButton = tk.Button(master = Frame, text = "All info", command = AllInfo)
InfomationButton.pack(pady = 10)

# Infomation Output
InfomationOutput = tk.Label(master = Frame, textvariable = szInfomation, font = ("Arial", 25))
InfomationOutput.pack(pady = 50)


# Pie Chart Functionality
def PieChart():
    Canvas = tk.Canvas(master = Frame, width = 400, height = 400, bg="white")
    Canvas.pack(pady= 20)






    



    
    

    



























Frame.pack()
Main.mainloop()



