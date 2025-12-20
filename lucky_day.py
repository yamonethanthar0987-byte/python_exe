
import random
import datetime
def lucky_day_picker():
    print("☘Lucky Day Picker!")
    print("=" *30)

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    to_do = {
        "Monday": "Sleep",
        "Tuesday": "Read novel",
        "Wednesday": "Eat snacks",
        "Thursday": "Go for a walk",
        "Friday": "Watch movie",
        "Saturday": "Meet up with friends",
        "Sunday": "Lay in bed",
    }

    # Validate that every weekday has a suggested activity
    missing = [d for d in days if d not in to_do]
    if missing:
        raise RuntimeError(f"Missing activities for days: {missing}")

    lucky_day = random.choice(days)

    print(f"Your lucky day is: {lucky_day}")
    print(f"Suggested activity is: {to_do.get(lucky_day, 'No suggestion available')}")


    today = datetime.datetime.now().strftime("%A")
    print(f"Today is : {today}")

    if (today == lucky_day):
        print("WOW! Today is your lucky day! ✨")
    else:
         print(f"🎃Your lucky day is: {lucky_day}")

lucky_day_picker()