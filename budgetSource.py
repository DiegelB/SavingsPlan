# This is a my budgeting program so i can keep track of that bread yo

checkingBalance = [0]
savingsBalance = [0]
transactions = {}

def mainMenu():
    userInput = input("Key  |   Action\n\n" +
                      "'C'  Display balance\n"+
                      "'A'  Add to balance\n"+
                      "'S'  Subtract from balance\n"+
                      "'T'  Displays balance changes\n"+
                      "'V'  Display savings\n"+
                      "'AV' Add to savings\n"+
                      "'SV' Subtract from savings\n"+
                      "'E'  Exit\n>> ")

    userInput = userInput.upper()

    if userInput == "C":
        print("$" + str(displayBalanceChecking(checkingBalance)))
        input("--Press enter to go back to the menu--\n")
        mainMenu()
    elif userInput == "A":
        addBalanceChecking(checkingBalance, transactions)
    elif userInput == "S":
        subtractBalanceChecking()
    elif userInput == "T":
        checkingTransactions()
    elif userInput == "V":
        checkBalanceSavings()
    elif userInput == "AV":
        addBalanceSavings()
    elif userInput == "SV":
        subtractBalanceSavings()

# if user inputs C
def displayBalanceChecking(checkingBalance):
    return checkingBalance[0]  # returns the balance of the checking account

# if the user inputs A
# adds to their checking balance
def addBalanceChecking(checkingBalance, transactions):
    print("| Current Balance: " + str(checkingBalance))
    print("|")
    print("| Please enter the ammount you want to add to your balance")
    numInput = input("| >>")
    
    print("| Please name this addition. Ex. 'Paycheck'")
    nameInput = input("| >>")

    transactions[nameInput] = numInput    
    checkingBalance[0] = checkingBalance[0] + int(numInput)

    mainMenu()

mainMenu()