from matplotlib import use
from User import User
from Admin import Admin 
from Instructor import Instructor
from Student import Student

def show_menu():
    
    pass



    

    

def process_operations():
    pass

def main():
    while True:
        print("Welcome to our system")
        print("please input username and password to login:(format username password)")

        cred = input()
        username,password = cred.split(" ")

        user = User(username=username,password=password)
        login_result,login_role,login_info =  user.login()

        if username=="exit":
            break

        elif login_result:
                print(login_role,"login successfully")
        else:
            print("incorrect credentials")
            continue
                
        
    print("system closed")


if __name__ == "__main__":
    # print a welcome message

    # manually register admin

    main()







