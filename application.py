# A SIMPLE ATM MACHINE

import random
import validation
import database
from getpass import getpass


#Initializing the system/System Home Page Interface
def initialize():
    
    validoption = False
    print("Welcome to KiaKia Bank")

    while validoption == False:

        accountCheck = int(input("Do you have an account with us? Type 1 for 'Yes' and 2 for 'No' \n"))
        if accountCheck == 1:
            validoption = True
            login()
        elif accountCheck == 2:
            validoption = True
            register()
        else:
            print("You have selected an invalid operation")

#register
    # firstname, lastname, email and password
    # generate user account number
def register():

    email = input("Type your Email \n")
    firstname = input("What is your first name? \n")
    lastname = input("What is your last name? \n")
    password = getpass("Create a password \n")

    accountNumber = genaccountnumber()

    isUserCreated = database.create(accountNumber, firstname, lastname, email, password)

    if isUserCreated:
        print("Dear %s %s, your Bank Account Number '%d' has been successfully created" % (firstname, lastname, accountNumber))
        login()
    else:
        print("Something went wrong, please try again")
        register()

#login
    # account number and password
def login():
    print("Login to your account")

    userAccountnumber = input("What is your correct Account Number \n")
    
    validuserAccountnumber = validation.accountNumVal(userAccountnumber)

    if validuserAccountnumber:
        password = getpass("What is your valid Password \n")
        
        user = database.authenticateUser(userAccountnumber, password)
        if user:
            bankoperation(user)    
        else:
            print("Invalid account number or password, please try again")
            login()
    
    else:
        print("Please input a valid Account Number. Check that you have up to ten digits and only integers")
        initialize()

#ATM operations
def bankoperation(user):

    validBankoperation = False
    
    print("Welcome %s %s " % (user[0], user[1]))
    print("These are the available operations today:")
    print("1. Withdrwal")
    print("2. Transfer")
    print("3. Submit deposit")
    print("4. Log out")
    print("5. Exit the system")

    while(validBankoperation == False):
        selectoperation = int(input("Select a number to choose an operation \n"))

        if(selectoperation == 1):
            validBankoperation = True
            withdrawOperation()

        elif(selectoperation == 2):
            validBankoperation = True
            transferOperation()

        elif(selectoperation == 3):
            validBankoperation = True
            depositOperation()

        elif(selectoperation == 4):
            validBankoperation = True
            login()

        elif(selectoperation == 5):
            validBankoperation = True
            exit()

        else:
            print("Error! Please select an available operation on the screen")  

def withdrawOperation():
    transferamount = int(input("How much do you want to withdraw \n"))
    if(transferamount <= 100000 and transferamount > 0):
        print("Withdrawal successful. Thank you for banking with us.")
        contOps()
    if(transferamount == 0):
        print("Please insert a valid number, You cannot withdraw zero.")
        withdrawOperation()
    if(transferamount > 100000):
        print("You cannot withdraw more than a N100,000, please try again")
        withdrawOperation()

def transferOperation():
    accountnumber = int(input("Type in the 10 digit number of the receiving account: \n"))
    print("1. Zenith Bank")
    print("2. Access Bank")

    bankpos = [1,2]
    bankname = ["Zenith Bank", "Access Bank"]
        
    receivingbank = int(input("Select bank: \n"))
    if(receivingbank in bankpos):
        amountoftransfer = int(input("How much do you wish to transfer: \n"))
        bankid = bankpos.index(receivingbank)
        print("You are about to transfer Naira %d to %d %s." % (amountoftransfer,accountnumber,bankname[bankid]))
        print("Select 1 to continue")
        print("Select 2 to cancel")

        validop = False
        while(validop == False):                
            confirmation = int(input("Confirm transaction \n")) 
            if(confirmation == 1):
                validop = True
                print("Your transfer of Naira %d to %d %s was successful" % (amountoftransfer,accountnumber,bankname[bankid]))
                contOps()
            elif(confirmation == 2):
                validop = True
                print("Your transaction was successfully cancelled.")
                contOps()
            else:
                print("Please select a valid operation. Thank you.")
    else:
        print("Error! Please select an available bank.")

def depositOperation():
    depositamount = int(input("Please type the amount you wish to deposit: \n"))
    accountnum = int(input("Type the 10 digit account number: \n"))
    
    validOps = False
    while(validOps == False):

        print("1. Savings")
        print("2. Current")

        accounttype = int(input("Select account type: \n"))
        if(accounttype == 1):
            validOps = True
            print("Your deposit of %d was to %d successful Thank you." % (depositamount,accountnum))
            contOps()
        elif(accounttype == 2):
            validOps = True
            print("Your deposit of %d was to %d successful Thank you." % (depositamount,accountnum))
            contOps()
        else:
            print("You have selected an invalid option, please try again")         

def genaccountnumber():
    return random.randrange(1111111111,9999999999)

def contOps():
    print("Would you like to perform another transaction")
    print("1. Yes")
    print("2. No")

    answer = int(input("Select an operation \n"))

    if answer == 1:
        login()
    elif answer == 2:    
        print("Thank you for banking with us.")
        exit()
    else:
        print("Kindly select a valid operation")
        contOps()

#### Banking System Interface ####
initialize()