"""
Programmer: Ben Diegel
Program: Savings program
Notes: This program saves 20% of each paycheck, as well as 10% of whatever was left over 
       in the users account.
"""
import os
import os.path

# Checks to see if the file balance.txt exsits
# if it does it opens it and returns the amount inside 
# if its not it creates the file and sets it to 0
def checkSave():
    if os.path.exists('balance.txt'): 
        savingFile = open('balance.txt', 'r')
        savingsBalance = savingFile.readline() #reads the file into the savingsBalance
        savingFile.close()
        return savingsBalance
    else:
        savingFile = open('balance.txt', 'w')
        savingFile.write("0")
        savingFile.close()
        return "0" # returns a string for later use in printSavingsTotal()
    

# this is on a loop to keep displaying the main options
# you can enter a paycheck, check your current savings, and quit
def mainMenu():
    userInput = "" # initilizes the input to start the loop
    while(userInput != 'q'):
        os.system("clear")
        print("\n")
        print("Welcome to Super-Saver! What would you like to do?\n"\
              "--------------------------------------------------\n"
              "(E)nter paycheck.\n"\
              "(C)heck savings.\n"\
              "(Q)uit\n")

        userInput = input(">>")
        userInput.lower() # for ease of programing 

        if(userInput == 'c'):
            printSavingsTotal()
        elif(userInput == 'e'):
            enterPaycheck()
    

# simple funciton to display your savings 
def printSavingsTotal():
    savings = checkSave() # runs check save to grab the acount amount
    print("You currently have: $" + savings.strip() + " in your account") # .strip() removed whitespace before and after
    input("Press enter to continue\n")                                    # strings. removes \n in this case

# asks the user to input current amount in account, to save 10% and saves it to file
# then asks to enter what they got paid and saves 20% and saves to file
def enterPaycheck():
    previousBalance = float(input("Please enter the current amount in your checking account.\n>>"))
    
    if(previousBalance >= 30): # if the current balance is under 30$ then it wont save lol
        addToSavings = previousBalance * .1
        print("Now adding $" + str(addToSavings) + " (10%) to your savings account.")
        input("Press enter to continue\n>>")
        addToSavingsBalance(addToSavings) # calls addToSavingsBalance and passes addToSavings

    else:
        print("Current account balance too low to add any to savings.") 

    savingsFromPaycheck = float(input("Please enter the amount you were paid.\n>>"))
    savingsFromPaycheck = savingsFromPaycheck * .2
    addToSavingsBalance(savingsFromPaycheck) # calls addToSavingsBalance and passes savingsfrompaycheck
    print("Now adding $" + str(savingsFromPaycheck) + " (20%) to your savings account.")
    input("Press enter to continue\n>>")

# saves what ever amount is passed to it to file
def addToSavingsBalance(savings):
    checkSave() # first checks to see if the file exits, if it does not it creates it
    savingFile = open("balance.txt", "r") # opens to read
    savingInFile = savingFile.read() # reads the current amount to hold it as temp
    savingFile.close() 

    newSave = open("balance.txt", "w") # then erases current file so when the amount is sequentially read it grabs the  
    savingInFile = float(savingInFile) # most up-to-date number.
    totalSavings = savingInFile + float(savings) # adds the passed argument to the current balance
    newSave.write(str(totalSavings)) # writes to file 
    newSave.close()

mainMenu() # runs the program at launch