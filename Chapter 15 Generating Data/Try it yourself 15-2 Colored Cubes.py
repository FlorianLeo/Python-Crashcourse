import matplotlib.pyplot as plt

#Erzeuge Liste von 1-5
x_values = range(1, 6)
#Bilde das Kubik von jeder Zahl aus x_values
y_values = [jeder_wert**3 for jeder_wert in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Kubik von 1 bis 5", fontsize=24)
ax.set_xlabel("Zahl", fontsize=10)
ax.set_ylabel("Kubik der Zahl", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)
# Ausdehnung der Achsen festlegen
# Werte x  x    y  y
ax.axis([0, 6, 0, 150])

plt.savefig('Tiy15-2.v1.png', bbox_inches='tight')
plt.show()