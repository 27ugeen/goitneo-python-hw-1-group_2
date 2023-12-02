from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    weekend_days = ["Saturday", "Sunday"]
    work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    def get_birthday_this_year(birthday, today):
        birthday_this_year = birthday.replace(year=today.year)
        return birthday_this_year if birthday_this_year >= today else birthday_this_year.replace(year=today.year + 1)

    def get_weekday_name(date):
        return date.strftime("%A")

    birthday_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = get_birthday_this_year(birthday, today)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = get_weekday_name(today + timedelta(days=delta_days))

            weekday = "Monday" if weekday in weekend_days else weekday

            birthday_dict[weekday].append(name)

    for day in work_days:
        names = birthday_dict.get(day, [])
        print(f"{day}: {', '.join(names)}")

# Приклад використання на всі дні тижня:
users = [
    {"name": "Terrible Monday", "birthday": datetime(1950, 12, 4)},
    {"name": "Normal Tuesday", "birthday": datetime(1984, 12, 5)},
    {"name": "Work Wednesday", "birthday": datetime(1979, 12, 6)},
    {"name": "Unbearable Thursday", "birthday": datetime(1991, 12, 7)},
    {"name": "Happy Friday", "birthday": datetime(1999, 12, 8)},
    {"name": "Party Saturday", "birthday": datetime(2003, 12, 2)},
    {"name": "Relax Sunday", "birthday": datetime(1980, 12, 3)},
    {"name": "Alice NextMonday", "birthday": datetime(1997, 12, 11)},
    {"name": "Alice NextTuesday", "birthday": datetime(2010, 12, 12)},
    {"name": "Alice NextWednesday", "birthday": datetime(1986, 12, 13)},
    {"name": "Alice NextThursday", "birthday": datetime(2020, 12, 14)},
]

get_birthdays_per_week(users)
