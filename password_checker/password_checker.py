#import regular expressions
import re

# If one of the below conditions is not met the password is invalid
def password_is_valid(password):
# password should exist
    if len(password) == 0:
        raise Exception('password does not exist')
# password should be longer than 8 characters
    else:
        if  len(password) <= 8:
            raise Exception('password should be longer than 8 characters')

        else:
#password should have at least one lowercase letter
            if not re.search("[a-z]", password):
                raise Exception('password should have at least one lowercase letter')
# password should have at least one uppercase letter  
            if not re.search("[A-Z]", password):
                raise Exception('password should have at least one uppercase letter')
# password should at least have one digit         
            if not re.search("[0-9]", password):
                raise Exception('password should at least have one digit')
#password should have at least one special character
            if not re.search("[$#@]",password):
                raise Exception('password should have at least one special character')

            print('valid password')
       
def password_is_ok(password):
    if len(password) == 0:
        raise Exception('password does not exist')
    else: 
        if len(password) <= 8:
            raise Exception('password should be longer than 8 characters')

# password_is_valid(password)

#password is ok
def password_is_ok(password):
#  Initialise count for compulsory and optional conditions  to zero
    compulsory_conditions = 0

    optional_conditions = 0
# two compulsory conditions should be met: password should not be equal to 0 and should be greater than 8 
    if len(password) > 8:

        compulsory_conditions = 2
# password should have at least one lowercase letter        
    if re.search("[a-z]", password):

        optional_conditions += 1
# password should have at least one uppercase letter         
    elif re.search("[A-Z]", password):
        optional_conditions += 1
    
# password should at least have one digit         
    elif re.search("[0-9]", password):
        optional_conditions += 1
                        

    else:
# password should have at least one special character
        if re.search("[$#@]",password):
            optional_conditions += 1
# check if the compulsory conditions have been met and one optional conditions
    if comp_conditions == 2 and optional_conditions >= 1:
        return True
    else:
        return False
                            