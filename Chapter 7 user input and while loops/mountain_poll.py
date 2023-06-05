answers = {}

the_flag_for_the_loop_is_boolean_true = True

while the_flag_for_the_loop_is_boolean_true:
	ask_for_name = input(f"\nWhat is your name, please: ")
	ask_for_mountain = input(f"Which mountain would you like to clime someday: ")
	answers[ask_for_name] = ask_for_mountain
	do_you_whish_to_continue = input("\nWould like to add another entry? (yes|no)")
	if do_you_whish_to_continue == 'no':
		the_flag_for_the_loop_is_boolean_true = False
	while not (do_you_whish_to_continue == 'yes' or do_you_whish_to_continue == 'no'):
		print(f"Please, answer 'yes' or 'no'")
		do_you_whish_to_continue = input("Which is it: ")

print(f"\n\n--- POLL RESULTS ---")
for key, value in answers.items():
	print(f"So, {key} would like to climb {value}.")