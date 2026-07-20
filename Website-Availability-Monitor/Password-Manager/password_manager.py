import random
import string
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))
while True:
    print("\nPassword Manager")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. View Saved Passwords")
    print("4. Exit")
    choice = input("Choose an option: ")
    print(repr(choice))
    if choice == "1":
        password = generate_password()
        print(f"\nGenerated Password: {password}")
    
    elif choice == "2":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        with open("Password.txt", "a")as file:
            file.write(f"{website} | {username} | {password}\n")

        print("Password saved succesfully!")
    elif choice == "3":
        try:
            with open("password.txt", "r") as file:
                print("\nSaved Password:")
                print(file.read())
        except FileNotFoundError:
            print("No passwords have been saved yet.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Plsase try again.")
        

