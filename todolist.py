import os
import time
tasks = []
def clear_terminal():
    if os.__name__ == "nt":
        os.system("cls")
    else:
        os.system("clear")

def display_menu():
    clear_terminal()
    print("Welcome to your to do list")
    time.sleep(0.5)
    print("1. Add a new task")
    time.sleep(0.5)
    print("2. View current tasks")
    time.sleep(0.5)
    print("3. Delete a task")
    time.sleep(0.5)
    print("4. Exit")
    time.sleep(0.5)
    print("Choose what you want to do")

def log_task():
    task = input("Enter the name of your task:  ")
    tasks.append(task)
    time.sleep(0.25)
    print(f"'{task}' has been logged")
    time.sleep(1)

def view_tasks():
    if len(tasks) == 0:
        print("No tasks logged...")
        time.sleep(1)
        
    else:
        print("Here are you logged tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            while True:
                goback = input("Go back to menu? Y/N  ")
                if goback == "N" or goback == "n":
                    clear_terminal()
                    print(f"{i}. {task}")
                elif goback == "Y" or goback == "y":
                    print("Going back to menu")
                    time.sleep(0.5)
                    
                    break   
                else:
                    print("Invalid input choose Y/N")
                    clear_terminal


def delete_log():
    view_tasks()
    task_num = int(input("Enter the task number to delete:  "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"'{removed}' has been deleted")
    else:
        print("Invalid input try again")
        delete_log()

        

def choose_task():
    chosen = input("Enter a number between 1-4:  ")
    if chosen == "1":
        clear_terminal()
        log_task()
    elif chosen == "2":
        clear_terminal()
        view_tasks()
    elif chosen == "3":
        clear_terminal()
        delete_log()
    elif chosen == "4":
        clear_terminal()
        print("Are you sure you want to leave nothing will be saved?")
        time.sleep(0.25)
        while True:
            yn = input("Do you want to close the program Y/N  ")
            if yn == "Y" or yn == "y":
                print("Goodbye!")
                time.sleep(0.5)
                exit()
            elif yn == "N" or yn == "n":
                print("Going back to menu")
                time.sleep(0.5)
                
                break   
            else:
                print("Invalid input choose Y/N")
                clear_terminal
        

    else:
        print("Invalid input choose 1-4")
        time.sleep(1)
        choose_task()



while True:
    display_menu()
    choose_task()

