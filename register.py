#user registration Signin, SignUp
from database import *
import random

def Signup():
    username = input("Create User Name: ")
    temp = cursor.execute(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Exist")
        Signup()
    else:
        print("Username is available please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter name: ")
        age= input("Enter your age: ")
        city = input("enter your city: ")
        account_number = random.randint(10000000, 99999999)



#calling function
Signup()

