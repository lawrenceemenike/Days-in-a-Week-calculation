# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
years_remaining = 90 - age_as_int
days = 365
weeks = 52
months = 12

d = days * years_remaining
w = weeks * years_remaining
m = months * years_remaining

message = f"You have {d} days, {w} weeks, and {m} months remaining"
print(message)





