
# -*- coding: utf-8 -*-

# @ author Milo Mitchell-Brooks
# @ Version 1
# @ ToDoList using UI 

# Imports
from queue import Empty
import tkinter as tk 
from tkinter import ttk 
from ttkbootstrap import Style
import pandas as pd 



# Setting up window
Main = tk.Tk()
Main.geometry("1920x1080")
Main.title("To-Do-List")
Frame = ttk.Frame(Main, width = 100, height = 200)

# Dataframes 
dfToDo = pd.DataFrame(columns = ["ToDo"])

# Save data 
def SaveData():
    dfToDo.to_csv("ToDo.csv", index = False)

# Load data
try:
    dfToDo = pd.read_csv("ToDo.csv")
except FileNotFoundError:
    SaveData()


# Variables 
szToDo = tk.StringVar()
szInfo = tk.StringVar()

# Label 
MainLable = ttk.Label(master = Frame, text = "To-Do List")
MainLable.pack(pady = 10)

# ToDo Functionality
def AddToDo():
    global dfToDo
    ToDo = szToDo.get()
    print(ToDo)
    if ToDo != "":
        dfToDo.loc[len(dfToDo)] = [ToDo]
        SaveData()
        szInfo.set(dfToDo)

# ToDo Entry 
ToDoEntry = ttk.Entry(master = Frame, text = "", textvariable= szToDo)
ToDoEntry.pack(pady = 25)
ToDoButton = ttk.Button(master = Frame, text = "Enter", command = AddToDo)
ToDoButton.pack(pady = 5)

# Clear Data Functionality
def ClearData():
    global dfToDo
    dfToDo = pd.DataFrame(columns = ["ToDo"])
    SaveData()
    if dfToDo.empty:
        szInfo.set("Nothing to do")

# Clear Data Button
ClearDataButton = ttk.Button(master = Frame, text = "Clear Data", command = ClearData)
ClearDataButton.pack(pady = 25)

# Info
if dfToDo.empty:
    szInfo.set("Nothing to do")
InfoOutput = ttk.Label(master = Frame, textvariable = szInfo)
InfoOutput.pack()


Frame.pack()
Main.mainloop()