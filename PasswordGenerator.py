import random
import string
def Password_Generator():
    user=input("if you want to generate a password:")
    if user=="yes":
        length_of_password=int(input("enter the length of the password:"))
        password="".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=length_of_password))
        print(f"The generated password is {password}")
        Password_Generator()
    else:
        print("Done")
Password_Generator()
