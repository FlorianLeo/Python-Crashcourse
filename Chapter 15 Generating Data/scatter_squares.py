import matplotlib.pyplot as plt

x_values = [6, 7, 8, 9, 10, 11]
y_values = [36, 49, 64, 81, 100, 121]
x2_values = range(12, 21)
y2_values = [jeder_wert**2 for jeder_wert in x2_values]
x3_values = range(21, 51)
y3_values = [jeder_wert**2 for jeder_wert in x3_values]
x4_values = range(50, 101)
y4_values = [jeder_wert**2 for jeder_wert in x4_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Achsen   x  y  Punktdicke
ax.scatter(2, 4, s=10)
ax.scatter(3, 9, s=10)
ax.scatter(4, 16, s=10)
ax.scatter(5, 25, s=10)
ax.scatter(x_values, y_values, s=10)
ax.scatter(x2_values, y2_values, s=10)
ax.scatter(x3_values, y3_values, c='red', s=10)
ax.scatter(x4_values, y4_values, c=y4_values, cmap=plt.cm.Blues, s=20)

ax.set_title("Quadrate einer Zahl", fontsize=24)
ax.set_xlabel("Zahl", fontsize=10)
ax.set_ylabel("Quadrat der Zahl", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)
# Ausdehnung der Achsen festlegen
# Werte x  x    y  y
ax.axis([0, 110, 0, 11000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()