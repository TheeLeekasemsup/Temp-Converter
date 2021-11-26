import os
import sys
import time
from os import system, name

def clearConsole():
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    #for mac and linux (here, os.name is 'posix')
    else:
        command = 'clear'
    os.system(command)
clearConsole()

def menu():
    clearConsole()
    print("---------------")
    print("Temp Converter")
    print("---------------")
    print("Please navigate the menu to open the category")
    print("1 Celcius")
    print("2 Fahrenheit")
    print("3 Kelvin")
    global functionSelect
menu()
functionSelect = input("Please select a function 1-3: ")

def cMenu():
    clearConsole()
    print("1 C to F")
    print("2 C to F Table")
    print("3 C to K")
    print("4 C to K Table")

#cMenu functions
#converting Celsius to Fahrenheit
def cTof():
    print("Please enter the temp in Celcius:")
    c = float(input(""))
    f = (c * 9/5) + 32
    if(type(c) == float):
        print("Conversion Completed!")
        print("Results:{0}°C = {1}°F".format(c,f))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            backToMenu = input("back to the menu type y or quit n:")
            if backToMenu == "y".lower:
                menu()
            else:
                sys.exit()
#conversion table from Celcius to Fahrenheit
def cTofTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        f = (i * 9/5) + 32
        print("Celcius : Fahrenheit")
        print("{0}°C   : {1}°F".format(i,f))
#Convert from Celcius to Kelvin
def cTok():
    print("Please enter the temp in Celcius:")
    c = float(input(""))
    k = c + 273.15
    if(type(c) == float):
        print("Conversion Completed!")
        print("Results:{0}°C = {1}°K".format(c,k))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            print("this program will quit in 5 seconds")
            time.sleep(5)
#Conversion table from Celcius to Kelvin
def cTokTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        k = i + 273.15
        print("Celcius : Kelvin")
        print("{0}°C   : {1}°K".format(i,k))
#select Celsius functions
def selectC():
    select_function = input("Please select a function 1-4: ")
    if(select_function == "1"):
        cTof()
    elif(select_function == "2"):
        cTofTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)
    elif(select_function == "3"):
        cTok()
    elif(select_function == "4"):
        cTokTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)
def fMenu():
    clearConsole()
    print("1 F to C")
    print("2 F to C Table")
    print("3 F to K")
    print("4 F to K Table")
#fMenu functions
#converting Fahrenheit to Celcius
def fToc():
    print("Please enter the temp in Fahrenheit:")
    f = float(input(""))
    c = (f - 32) * 5/9
    if(type(f) == float):
        print("Conversion Completed!")
        print("Results:{0}°F = {1}°C".format(f,c))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            backToMenu = input("back to the menu type y or quit n:")
            if backToMenu == "y".lower:
                menu()
            else:
                sys.exit()
#conversion table from Fahrenheit to Celcius
def fTocTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        f = (i - 32) * 5/9
        print("Fahrenheit : Celcius")
        print("{0}°F   : {1}°C".format(f,i))
#Convert from Fahrenheit to Kelvin
def fTok():
    print("Please enter the temp in Celcius:")
    f = float(input(""))
    k = (f - 32) * 5/9 + 273.15
    if(type(f) == float):
        print("Conversion Completed!")
        print("Results:{0}°F = {1}°K".format(f,k))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            print("this program will quit in 5 seconds")
            time.sleep(5)
#Conversion table from Fahrenheit to Kelvin
def fTokTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        k = (i - 32) - 5/9 + 273.15
        print("Fahrenheit : Kelvin")
        print("{0}°F      : {1}°K".format(i,k))
#select Fahrenheit functions
def selectf():
    select_function = input("Please select a function 1-4: ")
    if(select_function == "1"):
        fToc()
    elif(select_function == "2"):
        fTocTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)
    elif(select_function == "3"):
        fTok()
    elif(select_function == "4"):
        fTokTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)
    
def kMenu():
    clearConsole()
    print("1 K to F")
    print("2 K to F Table")
    print("3 K to C")
    print("4 K to C Table")
#kMenu functions
#converting kelvin to fahrenheit
def kTof():
    print("Please enter the temp in Fahrenheit:")
    k = float(input(""))
    c = (k - 273.15) * 9/5 + 32
    if(type(k) == float):
        print("Conversion Completed!")
        print("Results:{0}°K = {1}°C".format(k,c))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            backToMenu = input("back to the menu type y or quit n:")
            if backToMenu == "y".lower:
                menu()
            else:
                sys.exit()
#conversion table from kelvin to Fahrenheit
def kTofTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        k = (k - 273.15) * 9/5 + 32
        print("Kelvin : Fahrenheit")
        print("{0}°K  : {1}°F".format(i,k))
#Convert from Kelvin to Celcius
def kToc():
    print("Please enter the temp in kelvin:")
    k = float(input(""))
    c = k - 273.15
    if(type(k) == float):
        print("Conversion Completed!")
        print("Results:{0}°K = {1}°C".format(k,c))
        restart = input("Want to calculate again? y/n:")
        if(restart == "y"):
            clearConsole()
            cTof()
        elif(restart == "n"):
            print("this program will quit in 5 seconds")
            time.sleep(5)
#Conversion table from Celcius to Kelvin
def kTocTable():
    print("Please input the start range:")
    start_range = int(input(''))
    print("Please input the end range:")
    end_range = int(input(''))
    print("Please input the spacing range(if no spacing type 0):")
    spacing_range = int(input(''))
    for i in range(start_range, end_range, spacing_range):
        k = i - 273.15
        print("Kelvin : Celcius")
        print("{0}°K  : {1}°C".format(k,i))
#select Celsius functions
def selectf():
    select_function = input("Please select a function 1-4: ")
    if(select_function == "1"):
        fToc()
    elif(select_function == "2"):
        fTocTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)
    elif(select_function == "3"):
        fTok()
    elif(select_function == "4"):
        fTokTable()
        exitProgram = input("Exit right now? if no then don't type anything if yes then type y: ")
        if(exitProgram == "y"):
            print("this program will close in 3 seconds")
            time.sleep(3)


if(functionSelect == "1"):
    cMenu()
    selectC()
elif(functionSelect == "2"):
    fMenu()
    selectf()
elif(functionSelect == "3"):
    kMenu()
    select_function = input("Please select a number:")
else:
    menu()

