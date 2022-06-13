def accountNumVal(userAccountnumber):
    # check if accountNumber is empty (1)

    # Check if accountNumber is 10 digits (2)

    # Check if the accountNumber is an integer (3)

    if userAccountnumber:                      #(1)
        
        if len(str(userAccountnumber)) == 10:  #(2)

            try:                               #(3)
                int(userAccountnumber)
                return True
            except ValueError:
                print("Inavlid Account Number, your account number should a 10 digit number/integer")
                return False
            except TypeError:
                print("Invalid Data Type, please try again")
                return False

        else:
            print("Account Number cannot be lesser or greater than 10 digits")
            return False

    else:
        print("Your account number is required")
        return False