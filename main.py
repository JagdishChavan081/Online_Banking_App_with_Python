from register import *

print("Welcome to CodeAlly Banking System")

while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register ==1  or register ==2:
            if register==1:
                Signup()
        else:
            print("Enter valid Option")
    
    except ValueError:
        print("Invalid Inpur Try Again with Numbers")