def parse_input(user_input, expected_args=None):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    if expected_args is not None and len(args) != expected_args:
        raise ValueError(f"Expected {expected_args} arguments for command '{cmd}', but got {len(args)}.")

    return cmd, *args


def hello():
    return "How can I help you?"

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if args:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid command. Please provide a name."

    
def show_all(contacts):
    if contacts:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "No contacts found."
    
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()