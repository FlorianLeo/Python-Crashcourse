ask_user_name = input("Please enter you name: ")
print(f"\nHello {ask_user_name}!\n")



prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
ask_user_name = input(prompt)
ask_user_age = input("And what is your age? ")
ask_user_age = int(ask_user_age)
print(f"\nHello {ask_user_name}! Your age is {ask_user_age}\n")