master_pass = "Vaibhav99199"     #It is a master password you need to view all the username and password

def add():
    user_name = input("User Name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(user_name + "|" + password + "\n")

def view():
    view_pass = input("Enter a master password to view the usernames and passwords: ")
    if view_pass == master_pass:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("UserName:", user,", Password:",passw)
    else:
        print("Invalid Password")


while True:
    option = input("What do you want add new password, view a password (add/view) or Q for quit: ").lower()

    if option == "q":
        break

    if option == "add":
        add()
    elif option == "view":
        view()
    else:
        print("Invalid option!")
        continue