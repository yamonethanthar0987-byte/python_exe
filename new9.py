
import random
from datetime import datetime

num = random.randint(1,10)

print(f"🤨Your number is {num}🗽😇")

students = ["May Thae👽", "Yamone💖", "Min Khan🐱‍👤", "Wanna🐱‍🏍", "Ethan🎃"]
ran_std = random.choice(students)
print(f"Your name is {ran_std}.")

today = datetime.now().strftime("%A")
print(f"Today is {today}🐱‍🐉")