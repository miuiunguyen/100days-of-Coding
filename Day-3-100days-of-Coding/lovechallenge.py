print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
lower_case_name12 = lower_case_name1 + lower_case_name2
count_name1 = lower_case_name12.count("t")
count_name2 = lower_case_name12.count("r")
count_name3 = lower_case_name12.count("u")
count_name4 = lower_case_name12.count("e")
true_total = int(count_name1) + int(count_name2) + int(count_name3) + int(count_name4)

count_name5 = lower_case_name12.count("l")
count_name6 = lower_case_name12.count("o")
count_name7 = lower_case_name12.count("v")
count_name8 = lower_case_name12.count("e")
love_total = int(count_name5) + int(count_name6) + int(count_name7) + int(count_name8)

percent_match = str(true_total) + str(love_total)
percent_match_int = int(percent_match)

if percent_match_int <10 or percent_match_int >90:
    print(f"Your score is {percent_match_int}, you go together like coke and mentos.")
elif percent_match_int >=40 and percent_match_int <=50:
    print(f"Your score is {percent_match_int}, you are alright together.")
else:
    print(f"Your score is {percent_match_int}.")



