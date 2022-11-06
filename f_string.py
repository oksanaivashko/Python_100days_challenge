# f Strings

#your age
age = input("What is your current age?")
#convert age in int
age_as_int = int(age)
#define the remaining years
years_remaining = 90 - age_as_int
#define remaining days
days_remaining = years_remaining * 365
#define remaining weeks
weeks_remaining = years_remaining * 52
#define remaining month
months_remaining = years_remaining * 12

message = f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} month left"
print(message)