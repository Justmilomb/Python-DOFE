
# @ author Milo Mitchell-Brooks
# @ Version 1
# @BudgetTracker using UI

# Imports
import tkinter as tk

# Setting up window
Main = tk.Tk()
Main.geometry("1920x1080")
Main.title("Budget Tracker")
Frame = tk.Frame(Main, width = 100, height = 200)

# Variables
fltIncomeAmount = 0.0

# Label
MainLabel = tk.Label(Frame, text = "Budget Tracker", font=("Arial", 25))
MainLabel.pack(pady = 10)


# IncomeEntry
IncomeEntry = tk.Entry(Frame, text = "Enter Income", textvariable = fltIncomeAmount)
IncomeEntry.pack(pady = 30)

# IncomeButton
IncomeButton = tk.Button(Frame, text = "Add Income", font = ("Arial", 12))
IncomeButton.pack(pady = 5, padx = 10)


























Frame.pack()
Main.mainloop()



