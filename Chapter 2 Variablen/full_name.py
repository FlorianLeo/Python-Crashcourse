first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)
#statt f die Format-Methode verwenden
full_name = "{} {}".format(first_name, last_name)
print(full_name)
full_name = "{} {}".format(first_name, last_name).title()
print(full_name)
#whitespaces hinzufügen - 1 Tabulatorschritt mit \t
print("Python")
print("\tPython")
#whitespaces hinzufüegen - Zeilenschaltung mit \n
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")