# Project "Birthdays and Assistant Bot"

This project consists of two Python scripts:

1. **task_01.py**: Calculates upcoming birthdays for the current week and categorizes them by day.

   To run the script, use the following command:
```bash
$ python3 task_01.py
```

## Project "Birthdays"
    The script defines a function get_birthdays_per_week(users) that takes a list of user dictionaries with names and birthdays. It prints the upcoming birthdays categorized by the days of the week.

### Example usage:
```bash
users = [
    {"name": "Terrible Monday", "birthday": datetime(1950, 12, 4)},
    {"name": "Normal Tuesday", "birthday": datetime(1984, 12, 5)},
    {"name": "Work Wednesday", "birthday": datetime(1979, 12, 6)},
    # ... (other user entries)
]

get_birthdays_per_week(users)
```

2. **task_02.py**: Implements a console assistant bot that responds to user commands.

    To run the script, use the following command:
```bash
$ python task_02.py
```

## Project "Assistant Bot"
    This is a console assistant bot capable of interacting with the user and executing various commands.
    The bot responds to various commands, such as adding, changing, and displaying contacts, as well as saying hello and exiting.

### Bot Commands:

1. `hello`: Outputs the message "How can I help you?".
2. `add [name] [phone number]`: Adds a new contact with the specified name and phone number.
3. `change [name] [new phone number]`: Changes the phone number for an existing contact.
4. `phone [name]`: Outputs the phone number for the specified contact.
5. `all`: Outputs all saved contacts with phone numbers.
6. `close` or `exit`: Exits the bot.

### How to Use:

1. Enter a command in the console.
2. Follow the prompts to add, change, view, or display all contacts.
3. To exit, enter `close` or `exit`.

### Running the Program:

1. Open the terminal or command prompt.
2. Navigate to the project directory.
3. Use the command `python your_script_name.py`, where `your_script_name.py` is the name of your code file.

### Example Usage:
```bash
$ python your_script_name.py
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: phone John
1234567890
Enter a command: all
John: 1234567890
Enter a command: exit
Good bye!
```