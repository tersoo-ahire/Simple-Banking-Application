# Handle operations regarding interactions with information stored in the "User Records" folder.

# *** CRUD OPERATIONS ***
# Create record 
# Read record 
# Update record 
# Delete record

# *** OTHER OPERATIONS ***
# Authenticate Email registration
# Authenticate Account number creation
# Authenticate Login access

import os
import validation


userDatabasePath = "ATM/data/user_record/"

def create(accountNumber, firstname, lastname, email, password):

    userDetails = firstname + "," + lastname + "," + email + "," + password + "," + str(0)

    # Check and validate if account number exists so as to not create a similar computer generated account number
    if doesAccountNumberExist(accountNumber):
        return False
    # Check if there is an already existing email when the user is registering for the first time and ask user to input a new email
    if doesEmailAddressExist(email):
        print("User Email already exists")
        return False
    
    completionState = False
    
    # Create a new file to store users registration details
    # Name of the new file would be the computer generated "account number" + ".txt"
    try:
        f = open(userDatabasePath + str(accountNumber) + ".txt", "x")
    
    # Check if the created file already exists and also if there's content in the existing file before deleting the existing file
    # If the file exists and there's no content inside, computer should delete the file and create the new file afresh
    except FileExistsError:
        doesFileContainData = read(userDatabasePath + str(accountNumber) + ".txt")
        if not doesFileContainData:
            delete(accountNumber)

    # Write new users registration details into the new file created
    else:
        f.write(str(userDetails))
        completionState = True
        
    # After writing new users registration details, the computer will finally store/save the information into the created file
    finally:
        f.close()
        return completionState

def read(accountNumber):
    # Search for user with account number
    # Fetch content of the file
    validuserAccountnumber = validation.accountNumVal(accountNumber)


    # If account number is correct, search for the file and read it
    try:
        if validuserAccountnumber:
            f = open(userDatabasePath + str(accountNumber) + ".txt", "r")
        else:
            f = open(userDatabasePath + accountNumber, "r")

    # If account number isn't correct, print error type to user        
    except FileNotFoundError:
        print("User File not found")
    except FileExistsError:
        print("User File doesn't exist")
    except TypeError:
        print("Invalid account number format")

    # If account number is correct and exists return one line from the file for the computer to fetch/search/read for the exact information 
    # continuation ... it needs for authentication purposes
    else:
        return f.readline()
    return False

def update(accountNumber):
    print("Update a new user record")
    # Search for user with account number
    # Fetch content of the file
    # Update the content of the file
    # Save the file
    # return True

def delete(accountNumber):
    # Delete the user record (file)

    # Search for user file saved with "accountNumber.txt" if it exists
    isDeleteSuccessful = False
    if os.path.exists(userDatabasePath + str(accountNumber) + ".txt"): 
        
        # If it exists, try and remove the file   
        try:
            os.remove(userDatabasePath + str(accountNumber) + ".txt")
            isDeleteSuccessful = True

        # Handle the error if there's no file
        except FileNotFoundError:
            print("User File not found.")

        # Execute code regardless of any error or command
        finally:
            return isDeleteSuccessful

def doesEmailAddressExist(email):

    # Variable that stores the list of all users files saved in the "user_record" folder.
    allUsers = os.listdir(userDatabasePath)

    # Search through the list in each users file and check for the information stored in the email variable to match whether an email saved already exists
    for user in allUsers:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def doesAccountNumberExist(accountNumber):

    # Variable that stores the list of all users files saved in the "user_record" folder.
    allUsers = os.listdir(userDatabasePath)

    # Search through all files stored in the "user_record" folder and check if there's an existing file saved with the computer generated account number
    for user in allUsers:

        # Check for account number saved as the file name
        if user == str(accountNumber) + ".txt":
            return True
    return False
  

def authenticateUser(accountNumber, password):

    # Check if the account number entered in the login page exists in order to allow the user access bank operations.
    if doesAccountNumberExist(accountNumber):

        # Check for the account number saved as the name of the users file
        user = str.split(read(accountNumber), ',')

        # Check that password is stored in the same users file named after the users account number
        if password == user[3]:
            return user
    
    return False
