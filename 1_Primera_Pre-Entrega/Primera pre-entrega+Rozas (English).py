database = {} #Users will be saved here, usernames and passwords.

def register_user():
    #This function will create an user, that is, username and password. It will also add them to the database.
    while True:
        username = input("Type in your username: ")
        if username in database:
            print("This username is already registered, try again.")
            continue
        if not username:
            print("It is not possible to register an empty username, try again.")
        else:
            break
    while True:
        password = input("Type in your password: ")
        if not password:
            print("It is not possible to register an empty password, try again.")
        else:
            database[username] = password
            print("User has been successfully registered.")
            break

def log_in():
    #This function verifies that username and password are in the database, if they are, the user will log in.
    username = input("Type in your username: ")
    password = input("Type in your password: ")
    if username in database and database[username] == password:
        print("Log in successful.")
    else:
        print("Username and password do not match.")

def show_users():
    #This function shows all users within the database, that is, usernames and passwords. It also let us know if the database is empty or not.
    if len(database) > 0:
        for usuario , password in database.items():
            print(f"{usuario} : {password}")
    else:
        print("There are no users registered.")

def menu():
    #This function opens the menu, which offers the options that the user may need.
    while True:
        print("1. Register user")
        print("2. Log in")
        print("3. Show users")
        print("4. Exit")
        try:
            option = (int(input("Choose an option: ")))
        except:
            print("You haven't selected an option, try again.")
            continue
        if option == 1:
            register_user()
        elif option == 2:
            log_in()
        elif option == 3:
            show_users()
        elif option == 4:
            print("Hasta la vista, baby...")
            break
        else:
            print("You haven't selected an option, try again.")
menu()