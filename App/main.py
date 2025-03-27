
import tkinter as tk
from tkinter import Button, ttk

# Creates window
Window = tk.Tk()
Window.title("Productivity")
Window.geometry("1920x1080")

def Expense():
    print(ExpenseEntryInt.get())
    #ExpenseOutput.set(ExpenseEntryInt.get())

def Income():
    print(IncomeEntryInt.get())
    IncomeOutput.set(f"{IncomeEntryInt.get()} has been added as a income")




# Title
TitleLable = ttk.Label(master = Window, text = "Budget Tracker", font = "calibri 24 bold")
TitleLable.pack() 

# Input
InputFrameIncome = ttk.Frame(master = Window)
IncomeEntryInt = tk.IntVar()
IncomeOutput = tk.StringVar()
IncomeEntry = ttk.Entry(master = InputFrameIncome, textvariable = IncomeEntryInt)
IncomeButton = ttk.Button(master = InputFrameIncome, text = "Add Income", command = Income)
IncomeEntry.pack(side = "left", padx = 10)
IncomeButton.pack(side = "left", padx = 10)
InputFrameIncome.pack(pady = 50)
OutputFrameIncome = ttk.Frame(master = Window)
OutputIncomeText = ttk.Label(master = OutputFrameIncome, textvariable = IncomeOutput)
OutputIncomeText.pack()
OutputFrameIncome.pack(pady = 25)
ExpenseEntryInt = tk.IntVar()
InputFrameExpense = ttk.Frame(master = Window)
ExpenseEntry = ttk.Entry(master = InputFrameExpense, textvariable = ExpenseEntryInt)
ExpenseButton = ttk.Button(master = InputFrameExpense, text = "Add Expense", command = Expense)
ExpenseEntry.pack(side = "left", padx = 10)
ExpenseButton.pack(side = "left", padx = 10)
InputFrameExpense.pack(pady = 25)



# Runs the window
Window.mainloop()