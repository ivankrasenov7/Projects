import hashlib

passwords = {}

def add_password():
    website = input("Enter a website: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    passwords[website] = {'username': username, 'password': hashed_password}
    print("Password added successfully")

def view_password():
    if len(passwords) == 0:
        print("Invlaid password")
    else:
        print("Stored Passwords")
        for website, details in passwords.items():
            print(f"Website {website}")
            print(f"Username: {details['username']}")
            print("Passwords: ********")


def get_pasword():
    website = input("Enter a website:")
    if website in passwords:
        password = input("Enter the password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if passwords[website]['password'] == hashed_password:
            print(f"Username: {passwords[website]['username']}")
            print(f"Password: {passwords[website]['password']}")
        else:
            print("Incorrect password")

    else:
        print("Website not found")

def delete_password():
    website = input("Enter a website: ")

    if website in passwords:
        del passwords[website]
        print("The password has been deleted successfully")

    else:
        print("Website not found")

def show_menu():
    print("\n---- Password Manager----")
    print("1. Add Password")
    print("2. View Password")
    print("3. Get Password")
    print("4. Delete Password")
    print("5. Exit")

while True:
    show_menu()
    choice = input("enter a choice between 1-5: ")

    if choice == '1':
        add_password()
    elif choice == '2':
        view_password()
    elif choice == '3':
        get_pasword()
    elif choice == '4':
        delete_password()
    elif choice == '5':
        print("Goodbye")
        break
    else:
        print("invlaid option. try again")

