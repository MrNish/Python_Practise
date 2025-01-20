"""
Conditional: if-else, if-elif
Loop: for, while
Jumping: break, continue, pass
"""


def checkAge(age):
    if age >= 18:
        print("Age is greater than 18")
    else:
        print("Age isn't greater than 18")


checkAge(18)


def displayAgeCategory(age):
    if age < 18:
        print("Child")
    elif age >= 65:
        print("Senior Citizen")
    else:
        print("Adult")

displayAgeCategory(int(input("Enter age")))
