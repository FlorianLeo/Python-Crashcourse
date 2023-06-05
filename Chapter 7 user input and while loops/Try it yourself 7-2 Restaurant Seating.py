# multiline prompt
prompt = "Please, would mind and tell us how many seats you want for dinner?"
prompt +="\nNumber of Seats requested: "
# ask user for input with the prompt, store it, and convert it to an integer
ask_user_seats = input(prompt)
ask_user_seats = int(ask_user_seats)

if ask_user_seats <= 8:
	print(f"\nWe have a table with {ask_user_seats} seats ready for you.")
else:
	print(f"\nWe are sorry but for a table with {ask_user_seats} seats you have to wait.")