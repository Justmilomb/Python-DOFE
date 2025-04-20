
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


# Label
MainLabel = tk.Label(Frame, text = "Budget Tracker", font=("Arial", 25))
MainLabel.pack(pady = 10)


# Income Functionality
def AddIncomeInfo():
    fltAmount = fltIncomeAmount.get()
    dfIncome.loc[len(dfIncome)] = [fltAmount, None]
def ResetIncomeUI():
    # IncomeEntry
    IncomeEntry.config(text = "Enter Income", textvariable = fltIncomeAmount)
    IncomeEntry.pack(pady = 20)

    # IncomeButton
    IncomeButton.config(text = "Add Income", font = ("Arial", 12), command = AddIncomeInfo)
    IncomeButton.pack(pady = 0, padx = 10)

# IncomeEntry
IncomeEntry = tk.Entry(Frame, text = "Enter Income", textvariable = fltIncomeAmount)
IncomeEntry.pack(pady = 20)

# IncomeButton
IncomeButton = tk.Button(Frame, text = "Add Income", font = ("Arial", 12), command = AddIncomeInfo)
IncomeButton.pack(pady = 0, padx = 10)


#Expense Functionality
def AddExpenseInfo():
    fltAmount = 0
    szCategory = ""
    dfExpense["Category"] = dfExpense["Category"].astype("string")

    
    fltAmount = fltExpenseAmount.get()
    dfExpense.loc[len(dfExpense)] = [fltAmount, None]

    # ExpenseEntry
    ExpenseEntry.config(text = "Enter Category", textvariable = szExpenseCategory)
    ExpenseEntry.pack(pady = 20)

    # ExpenseButton
    ExpenseButton.config(text = "Add Category", font = ("Arial", 12))
    ExpenseButton.pack(pady = 0, padx = 10)

    szCategory = szExpenseCategory.get()
    dfExpense.loc[len(dfExpense)-1, "Category"] = szCategory
    print(dfExpense)
    if len(szCategory) != 0:
        ResetExpenseUI()
def ResetExpenseUI():
    # ExpenseEntry
    ExpenseEntry.config(text = "Enter Expense", textvariable = fltExpenseAmount)
    ExpenseEntry.pack(pady = 20)

    # ExpenseButton
    ExpenseButton.config(text = "Add Expense", font = ("Arial", 12), command = AddExpenseInfo)
    ExpenseButton.pack(pady = 0, padx = 10)

    fltExpenseAmount.set("")
    szExpenseCategory.set("")

# ExpenseEntry
ExpenseEntry = tk.Entry(Frame, text = "Enter Expense", textvariable = fltExpenseAmount)
ExpenseEntry.pack(pady = 20)

# ExpenseButton
ExpenseButton = tk.Button(Frame, text = "Add Expense", font = ("Arial", 12), command = AddExpenseInfo)
ExpenseButton.pack(pady = 0, padx = 10)

fltTest = 0.0



    



    
    

    



























Frame.pack()
Main.mainloop()



