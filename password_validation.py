#Regular Expression - password validation
#Requirement:
# 1. Minimum 8 characters.
# 2. Must have at least one lowercase letter between [a-z]
# 3. Must have at least one uppercase letter between [A-Z]
# 4. Must have at least one number or digit between [0-9].
# 5. Must have at least one special character among [@ or # or $ or % or ^ or & or + or =].

import re

#pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}")

def password_check(password):    
    while True:   
        if (len(password)<8):
            return "Not a Valid Password. Should be at least 8 character long."
        elif not re.search("[a-z]", password):
            return "Not a Valid Password. Should contain at least one lowercase letter."
        elif not re.search("[A-Z]", password):
            return "Not a Valid Password. Should contain at least one uppercase letter."
        elif not re.search("[0-9]", password):
            return "Not a Valid Password. Should contain at least one number."
        elif not re.search("[!@#$%^&+=]", password):
            return "Not a Valid Password. Should contain at least one special character."
        elif re.search("\s", password):
            return "Not a Valid Password. Should not contain space."
        else:
            return "Congratulations! Your password fulfils standard password requirement."
