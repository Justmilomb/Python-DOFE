from pynput import keyboard
import time
import os
is_locked = False
def KilometertoMiles(km):
    return km * 0.621371
def MilestoKilometer(m):
    return m * 1.60934
def CelsiustoFahrenheight(c):
    return (c * 9/5) + 32
def FahrenheightoCelcius(f):
    return (f - 32) * 5/9
def KilogramstoPounds(kg):
    return kg * 2.20462
def PoundstoKilograms(lb):
    return lb * 0.453592
def unitconverter():
    def lock_keyboard(key):
        global is_locked
        is_locked = True

    print("Welcome to unit converter")
    time.sleep(0.5)
    print("Lets get started!!")
    print("Press 1 for Kilometers to Miles")
    time.sleep(1)
    print("Press 2 for Miles to Kilometers")
    time.sleep(1)
    print("Press 3 for Celsius to Fahrenheit")
    time.sleep(1)
    print("Press 4 for Fahrenheit to Celcsius")
    time.sleep(1)
    print("Press 5 for Kilograms to Pounds")
    time.sleep(1)
    print("Press 6 for Pounds to Kilograms")
    
    def unlock_keyboard(key):
    
    choice = int(input("Enter the number of your choice..."))
    time.sleep(1)
    os.system("clear")     
    if choice == 1:
        km = float(input("Distance in Kilometers?..."))
        print(f"{km} km is equal to {KilometertoMiles(km)}m")
    elif choice == 2:
        m = float(input("Distance in Miles?..."))
        print(f"{m} m is equal to {MilestoKilometer(m)}km")
    elif choice == 3:
        c = float(input("Temprature in Celsius?..."))
        print(f"{c} c is equal to {CelsiustoFahrenheight(c)}f")
    elif choice == 4:
        f = float(input("Temprature in Fahrenheight?..."))
        print(f"{f} f is equal to {FahrenheightoCelcius(f)}c")
    elif choice == 5:
        kg = float(input("Weight in Kilograms?..."))
        print(f"{kg} kg is equal to {KilogramstoPounds(kg)}lb")
    elif choice == 6:
        lb = float(input("Weight in Pounds?..."))
        print(f"{lb} lb is equal to {PoundstoKilograms(lb)}kg")
    else:
        print("ERROR")
        time.sleep(0.5)
        print("Please choose a number between 1-6")
        time.sleep(1.5)
        print("Restarting in...")
        time.sleep(1.5)
        print("3")
        unitconverter()

unitconverter()       time.sleep(0.4)
        print('2')
        time.sleep(0.2)
        print("1")
        time.sleep(0.8)
        os.system("clear")
        unitconverter()

unitconverter()