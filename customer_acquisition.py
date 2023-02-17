print("Welcome to Flight Club.")
print("We find the best flight deals and email them to you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

emails_match = False

while not emails_match:
    email = input("What is your email?\n")
    email_repeated = input("Type your email again.\n")
    if email == email_repeated:
        emails_match = True
        print("You're in the club!")
    else:
        print("Sorry that didn't work! Emails have to match.")
