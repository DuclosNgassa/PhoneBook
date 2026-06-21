
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
    elif user_input == 2:
        remove_contact()
    elif user_input == 3:
        search_contact()
    elif user_input == 4:
        view_contact()
    elif user_input == 5:
        print("Goodbye!")
    else:
        print(f"{user_input} is not a valid choice. Please select a number between 1 and 5.")

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input(f"Enter the phone number of {name}: ")
    if is_valid_phone_number(phone):
        if name in contact:
            print(f"{name} already exist")
        else:
            contact[name] = phone
            print(f"{name} added successfully")
    else:
        print(f"{phone} is not a valid phone number. It should contain only digits, one optional hyphen (-), or a plus sign (+) at the start. It must contain 6 to 11 digits.")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contact:
        del contact[name]
        print(f"Contact {name} has been removed")
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
        print(f"- {name}: {phone}")

def is_valid_phone_number(phone_number):
    """
        - A valid phone number is defined by:
              Only digits, hyphens (-) or plus (+).
        - Exactly one hyphen (-), no less and no more.
        - If a plus sign appears, it must be the first character of the phone number.
        - The number of digits is between 6-11 (inclusive).
        :param phone_number:
        :return: True if phone number is valid, False otherwise
    """
    return validate_hyphen(phone_number) and validate_plus(phone_number) and validate_digit(phone_number)

def validate_hyphen(phone_number):
    return phone_number.count('-') == 1

def validate_plus(phone_number):
    count_plus = phone_number.count('+')
    return count_plus == 0 or (count_plus == 1 and phone_number[0] == '+')

def validate_digit(phone_number):
    new_phone_number = phone_number.replace('-', '').replace('+', '')
    return 6 <= len(new_phone_number) <= 11

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

