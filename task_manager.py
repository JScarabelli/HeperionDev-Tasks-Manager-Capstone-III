# compulsory task part 1

# =====importing libraries===========

from datetime import datetime


# ====Login Section====

# I have not deleted the pseudo-code as a comment guide for the file.
# global variable and granted to run code.
user_name = "admin"
granted = False

# This function allows new users to be added inside the register function
def grant():
    global granted
    granted = True

# prompt option to the user:
def main():
    global option
    print("\nMain Menu")
    print("══════════")
    print("Type 1 - Register (only admin)")
    print("Type 2 - Login")

    while True:
        print()
        option = input("Choose an option: ")
        if option in ["1", "2"]:
            break


# this function will prompt the user with option to login or register.
def access(option):

    while option == "2":
        user_name = input("Please enter your username: ")
        user_password = input("Please enter your password: ")
        login(user_name, user_password)
    else:
        user_name = input("Please create your username: ")
        user_password = input("Please create your password: ")
        #register(user_name, user_password)

        # confirming that the passwords match.
        while True:
            confirm_password = input("Confirm your Password: ")
            if confirm_password == user_password:
                break
            else:
                print("Passwords do not match!")
                print("Please try again")


# this function will allow to login as admin or if you are already registered.
def login(user_name, user_password):

    # checking the user to validate its entry.
    success = False
    file = open("user.txt", "r")
    for i in file:
         a, b = i.split(",")
         b = b.strip()
         if a == user_name and b == user_password:
            success = True
            break
    file.close()

    # if login is successful print successful or else
    if success:
        print("\nLogin Successful")
        menu()
    else:
        print("wrong username or password")


# adding user information to user.txt file and split them with white space and creating a new line.
def register(user_name, user_password):
    file = open("user.txt", "a")
    file.write(f"\n{user_name}, {user_password}")
    grant()


# this function is to manipulate data from tasks.txt file.
def menu():

    while True:
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        print(f"══════════════════════\n")
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - Statistics
        e - Exit
        : ''').lower()

        # registering a new user.
        if menu == 'r':

            # only admin can add a new user.
            user_name = input("Please confirm your username: ")
            if user_name == "admin":
                print("Hi admin, you can add an account")

            else:
                print("You ara not allowed to add an account.")
                break

            # checking whether user already exists in user.txt file.
            while True:
                tasks_read = open("user.txt", "r")
                data = tasks_read.readlines()
                new_user_name = input("Please enter a username: ")

                for user in data:
                    split_data = user.split(", ")

                    if split_data[0] != new_user_name:
                        break
                    else:
                        print("Username already exist")
                        new_user_name = input("Please re-enter a username: ")

                # checking whether the password matches.
                new_user_password = input("Please enter a password: ")
                conf_password = input("Please re-enter the password: ")

                if new_user_password != conf_password:
                    print("password did not match. Please Try again")

                elif new_user_password == conf_password:
                    print("password matches. New user created")

                # appending the new user and password into the user.txt file.
                append = open("user.txt", "a")
                append.write(f"\n{new_user_name}, {conf_password}")
                append.close()
                break

        elif menu == 'a':

            # appending new task to the task.txt file.
            with open("tasks.txt", "a") as file:
                print("\n══════════════════")
                new_user = input("Please enter a username of the person whom the task is assigned to: ").lower()
                new_title = input("\nPlease enter a title of a task: ").lower()
                new_description = input("\nPlease enter a description of the task: ").lower()
                new_assigned_date = input("\nPlease enter the due date of the task: ").lower()
                current_date = input("\nPlease enter the current date: ").lower()
                new_completion = "No"
                file.write(f"\n{new_user}, {new_title}, {new_description}, {new_assigned_date}, "
                           f"{current_date}, {new_completion}")
                print("══════════════════\n")

        elif menu == "va":

            # print out the task.txt data in format requested using the split function.
            tasks_read = open("tasks.txt", "r")
            data = tasks_read.readlines()

            # using enumerate to display the number of the task, starting at 1.
            for pos, line in enumerate(data, 1):
                split_data = line.split(", ")

                output = f"\n════════[{pos}]══════════\n"
                output += f"Assigned to:\t{split_data[0]}\n"
                output += f"Task:\t\t{split_data[1]}\n"
                output += f"Description: \t{split_data[2]}\n"
                output += f"assigned Date: \t{split_data[3]}\n"
                output += f"Due date: \t{split_data[4]}\n"
                output += f"Is completed: \t{split_data[5]}\n"
                output += f"══════════════════════\n"

                print(output)

        # verifying each user task and its number.
        elif menu == 'vm':

            # reading through the task.txt file to very tasks and users.
            data = open("tasks.txt", "r")
            data_read = data.readlines()

            # using enumerate to display the number of the task, starting at 1.
            for pos, options in enumerate(data_read, 1):
                split_data = options.split(", ")

                output = f"\n════════[{pos}]══════════\n"
                output += f"Assigned to:\t{split_data[0]}\n"
                output += f"Task:\t\t{split_data[1]}\n"
                output += f"Description: \t{split_data[2]}\n"
                output += f"assigned Date: \t{split_data[3]}\n"
                output += f"Due date: \t{split_data[4]}\n"
                output += f"Is completed: \t{split_data[5]}\n"
                output += f"══════════════════════\n"

                print(output)

            # setting an error check for the user. if task number does not exist.
            while True:
                task_choice = int(input("Please select a task number: "))-1

                if task_choice < 0 or task_choice > len(data_read):
                    print("You have selected an invalid option, try again: ")
                    continue

                edit_data = data_read[task_choice]
                break

            # giving the option for the user to take an action.
            while True:
                output = f"\n════════[Select an Option]══════════\n"
                output += "1- Edit task\n"
                output += "2- Mark as completed\n"
                output += "-1 Return to main menu\n"
                output += f"══════════════════════\n"

                choice = int(input(output))

                # setting an error check for the user, if the option does not exist.
                if choice < -1 or choice >= 3:
                    print("You have selected an invalid option, try again: ")
                    continue

                # if option  -1 is chosen sending the user back to the main menu.
                if choice == -1:
                    main()

                # if option 1 is chosen and task already completed, print task already completed a user sent to main.
                if choice == 1:
                    split_data = edit_data.split(", ")

                    if split_data[-1] == 'Yes\n':
                        print("Task already completed")
                        main()
                        break

                    # if user option not completed before a new_user and date will be written into task.txt file.
                    else:
                        split_data = edit_data.split(", ")
                        split_data[0] = 'New_user'
                        split_data[-2] = "25 Jan 2023"
                        new_data = ", ".join(split_data)
                        data_read[task_choice] = new_data

                # if option 2 is chosen task will be marked completed.
                elif choice == 2:
                    split_data = edit_data.split(", ")
                    split_data[-1] = 'Yes\n'
                    new_data = ", ".join(split_data)
                    data_read[task_choice] = new_data

                # new data will be written in the task.txt file.
                task_write = open("tasks.txt", "w")
                for line in data_read:
                    task_write.write(line)

                # closing all files.
                task_write.close()
                data.close()
                break

        # generating new file reports.
        elif menu == "gr":
            file = open("tasks.txt", "r")
            task_list = file.readlines()
            file.close()
            over_due = 0
            uncompleted_task = 0

            # counting the number of tasks uncompleted.
            # counting the number of over due tasks.
            for line in task_list:
                data_list = line.strip("\n").split(", ")

                # setting dates for comparison with current date.
                if data_list[-1].lower() == "no":
                    uncompleted_task += 1
                    due_date = data_list[-2]
                    date_obj = datetime.strptime(due_date, "%d %b %Y")
                    today_date = datetime.today()

                    # checking variables against dates.
                    if date_obj < today_date:
                        over_due += 1

            print(f"Uncompleted tasks: {uncompleted_task}, overdue task: {over_due}")

            # creating task_overview.txt file. With the number of uncompleted and over due tasks.
            with open("task_overview.txt", "w") as file:
                file.write(f"Uncompleted tasks: {uncompleted_task}, overdue task: {over_due}")



        # counting the number of tasks and users.
        elif menu == "ds":

            # as we have 1 user per line counted the total number of lines.
            with open("user.txt", "r") as file:
                data = file.read()
                lines = data.split("\n")
            num_users = 0
            for users in lines:
                if users:
                    num_users += 1

            # as we have 1 task per line counted the total number of lines.
            with open("tasks.txt", "r") as file_1:
                data = file_1.read()
                lines = data.split("\n")
            num_tasks = 0
            for tasks in lines:
                if tasks:
                    num_tasks += 1

            print("\nStatistics")
            print(f"════════════")
            print(f"Numbers of tasks: {num_tasks}\n")
            print(f"Numbers of Users: {num_users}")
            print(f"\n════════════")

            # creating user_overview.txt file with number of tasks and number of users.
            with open("user_overview.txt", "w") as file_2:
                file_2.write(f"Total number of tasks: {num_tasks}, "
                             f"Total number of users: {num_users}")

        elif menu == 'e':

            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

# looking forward for your feedback.


main()
access(option)
