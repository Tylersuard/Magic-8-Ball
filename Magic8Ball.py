import random

question = input("Ask, and the Magic 8-Ball will answer...")

answer_number = random.randint(0,4))

if answer_number == 0:
    print("Yes")
elif answer_number == 1:
    print("No")
elif answer_number == 2:
    print("Outlook unsure")
elif answer_number == 3:
    print("The odds are in your favor")
elif answer_number == 4:
    print("Most definitely")