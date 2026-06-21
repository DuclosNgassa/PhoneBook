
contact = {}

def display_menu():
    menu = """
    Select an action:
    1. Add a contact
    2. Remove a contact
    3. Search for a contact
    4. View the phone book
    5. Exit
    """

    print(menu)

def take_user_input():
    user_input = int(input("Enter your choice (1-5): "))
    return user_input

def process_input(user_input):
    if user_input == 1:
        add_contact()
    if user_input == 2:
        remove_contact()
    if user_input == 3:
        search_contact()
    if user_input == 4:
        view_contact()
    if user_input == 5:
        print("Goodbye!")

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input(f"Enter the phone number of {name}: ")
    if name in contact:
        print(f"{name.title()} already exist")
    else:
        contact[name] = phone
        print(f"{name.title()} added successfully")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contact:
        del contact[name]
        print(f"Contact {name.title()} has been removed")
    else:
        print("Contact doesn't exist")

def search_contact():
    name = input("Enter the name of the contact to search for: ")
    if name in contact:
        print(f"{name}´s phone number is {contact[name]}")
    else:
        print(f"{name} doesn't exist")

def view_contact():
    if len(contact) == 0:
        print("You have no contact yet")
    for name, phone in contact.items():
        print(f"- {name.title()}: {phone}")

def main():
    print("Welcome to the phone book app!")
    while True:
        display_menu()
        user_input = take_user_input()
        process_input(user_input)
        if user_input == 5:
            break

if __name__ == '__main__':
    main()

