unconfirmed_users = ['alice',  'brian', 'candace']
confirmed_users = []

# eine for-loop ist sehr effektiv um durch Listen zu itterieren.
# eine for-loop stolpert jedoch wenn während der Ausführung die Element der Liste mehr oder weniger werden
# verwende while-loop um durch Listen zu itterieren deren Element mehr oder weniger werden.
# Loope so lange, so lange die Liste Element hält und führe verschiedenes aus.
# höre damit auf sobald die Liste leer ist.
while unconfirmed_users:
	user_found_in_list = unconfirmed_users.pop()
	print(f"Oh - found one unconfirmed user in the List: {user_found_in_list}")
	print(f"Appending entry {user_found_in_list} to confirmed users list.")
	confirmed_users.append(user_found_in_list),
	print(f"Keep searching\n")
print(f"\nDone searching.")
print(f"List of confirmed users containes now:")
for element in confirmed_users:
	print(f"\t{element}")