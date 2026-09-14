import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 12, 13)

days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Your birthday is in {days_away} days!")