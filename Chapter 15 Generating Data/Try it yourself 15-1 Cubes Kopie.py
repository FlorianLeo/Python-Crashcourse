import matplotlib.pyplot as plt

x_values = range(1, 501)
y_values = [jeder_wert**3 for jeder_wert in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c='blue', s=1)

ax.set_title("Kubik einer Zahl", fontsize=24)
ax.set_xlabel("Zahl", fontsize=10)
ax.set_ylabel("Kubik der Zahl", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)
# Ausdehnung der Achsen festlegen
# Werte x  x    y  y
ax.axis([0, 505, 0, 126000000])

plt.savefig('Tiy15-1.v2.png', bbox_inches='tight')
plt.show()