def main():
    user=input("you want to calculate:")
    if user=="yes":
        user_num1=float(input("enter the first number:"))
        user_num2=float(input("enter the second number:"))
        try:
            user_choice_operation=input("enter the your choice of operation:")
            if user_choice_operation=="+" or user_choice_operation=="addition":
                Ans=user_num1+user_num2
                print(f"The addition of {user_num1} and {user_num2} is {Ans}")
                main()
            if user_choice_operation=="-" or user_choice_operation=="sub":
                Ans=user_num1-user_num2
                print(f"The subtraction of {user_num1} and {user_num2} is {Ans}")
                main()
            if user_choice_operation=="*" or user_choice_operation=="mul":
                Ans=user_num1*user_num2
                print(f"The multiplication of {user_num1} and {user_num2} is {Ans}")
                main()
            if user_choice_operation=="/" or user_choice_operation=="division":
                Ans=user_num1/user_num2
                print(f"The division of {user_num1} and {user_num2} is {Ans}")  
                main()   
        except:
            print("please give the valid operation")
    else:
        print("Done")
main()