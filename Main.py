from User import User
from Admin import Admin 
from Instructor import Instructor
from Student import Student


commands2 = {
    1:"TITLE_KEYWORD",
    2:"ID",
    3:"INSTRUCTOR_ID"
}

commands4 = {
    1:"ID",
    2:"KEYWORD",
    3:"COURSE_ID"
}


def show_menu(user=None):

    print("""
    1. EXTRACT_DATA
    2. VIEW_COURSES
    3. VIEW_USERS
    4. VIEW_REVIEWS
    5. REMOVE_DATA
    """)
    


def process_operations(user,isAdmin=False):

    methods = {
        1:user.extract_info,
        2:user.view_courses,
        3:user.view_users,
        4:user.view_reviews,
        5:user.remove_data,
    }
    
    choice = int(input())

    if choice==2 and isAdmin:
        
        print("""
        1.TITLE_KEYWORD
        2.ID
        3.INSTRUCTOR_ID
        """)

        command_int = str(input())
        if command_int=="": 
            methods[choice]()
            return

        command =  commands2.get(int(command_int))
        if command=="": 
            methods[choice]()
            return

        if not command: 
            print("invalid command")
            return 
        
        value = input("Value: ")
        
        methods[choice](args=[command,value])
        return

    if choice==4 and isAdmin:
        
        print("""
        1.ID
        2.KEYWORD
        3.COURSE_ID
        """)

        command_int = str(input())
        if command_int=="": 
            methods[choice]()
            return

        command =  commands4.get(int(command_int))

        if not command: 
            print("invalid command")
            return 
        
        value = input("Value: ")

        methods[choice](args=[command,value])
        return
    
    methods[choice]()


def main():
    while True:
        print("please input username and password to login:(format username password)")

        cred = input()
        if cred=="exit":
            break
        username,password = cred.split(" ")

        user = User(username=username,password=password)
        login_result,login_role,login_info =  user.login()

        users={
            "Admin":Admin,
            "Instructor":Instructor,
            "Student":Student
        }

        if login_result:
            print(login_role,"login successfully")

        else:
            print("incorrect credentials")
            continue

        if login_role=="Student":
            login_info = login_info.split(";;;")
            user = users[login_role](
                login_info[0],
                user.username,
                user.password,
                login_info[3],
                login_info[4],
                login_info[5],
                login_info[6],
                ) 
        elif login_role=="Instructor":
            login_info = login_info.split(";;;")
            user = users[login_role](
                login_info[0],
                user.username,
                user.password,
                login_info[3],
                login_info[4],
                login_info[5],
                login_info[6],
                ) 

        elif login_role=="Admin":
            user = users[login_role](
                username=user.username,
                password=user.password
            )

        print(f"welcome {login_role.lower()} your role is {login_role}")
        
        while True:
            show_menu()
            process_operations(user,isAdmin=True if login_role=="Admin" else False)
        
    print("system closed")


if __name__ == "__main__":
    print("Welcome to our system")

    # manually register admin

    main()







