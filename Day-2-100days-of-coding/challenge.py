age = input("What is your current age?")
#Calculate the days. years. months left until you will get 90 years old
years = 90 - int(age)
months = years * 12 
weeks = months * 4
days = years * 365
message = f"You have {days}, {weeks} weeks and {months} months lefts."
print(message)