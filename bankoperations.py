name = input("What is your username? \n")

allowedusers = ["Tersoo","David","Maleek"]
allowedpassword = ["5643","1234","4321"]

if(name in allowedusers):
    password = input("Your password? \n")
    userid =  allowedusers.index(name)

    if(password == allowedpassword[userid]):
        print("Welcome %s! You are now logged in." % name)
        print("These are the available operations today:")
        print("1. Withdrwal")
        print("2. Transfer")
        print("3. Submit deposit")
        selectoperation = int(input("Select a number to choose an operation \n"))
#Withdraw
        if(selectoperation == 1):
            print("You have selected option %d" % selectoperation)
        else:
            print("Error! Please select an available operation on the screen") 
        if(selectoperation == 1):
                transferamount = int(input("How much do you want to withdraw \n"))
                if(transferamount <= 100000 and transferamount > 0):
                    print("Withdrawal successful. Thank you for banking with us.")
                if(transferamount == 0):
                    print("Please insert a valid number, You cannot withdraw zero.")
                if(transferamount > 100000):
                    print("You cannot withdraw more than a N100,000, please try again")
    #Transfer
        if(selectoperation == 2):
            print("You have selected option %d" % selectoperation)
        if(selectoperation == 2):
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
                        
                confirmation = int(input("Confirm transaction \n")) 
                if(confirmation == 1):
                    print("Your transfer of Naira %d to %d %s was successful" % (amountoftransfer,accountnumber,bankname[bankid]))
                elif(confirmation == 2):
                    print("Your transaction was successfully cancelled. Please try again")
                else:
                    print("Please select a valid operation. Thank you.")
            else:
                print("Error! Please select an available bank.")
#Deposit                            
        if(selectoperation == 3):
            print("You have selected option %d" % selectoperation)
        if(selectoperation == 3):
                depositamount = int(input("Please type the amount you wish to deposit: \n"))
                accountnum = int(input("Type your 10 digit account number: \n"))
                print("1. Savings")
                print("2. Current")
                accounttype = int(input("Select account type: \n"))
                if(accounttype == 1):
                    print("Your deposit of %d was to %d successful Thank you." % (depositamount,accountnum))
                elif(accounttype == 2):
                    print("Your deposit of %d was to %d successful Thank you." % (depositamount,accountnum))         
    else:
        print("Password incorrect, Please try again")
else:
    print("Name not found, Please try again")