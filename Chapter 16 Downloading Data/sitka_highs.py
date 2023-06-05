import csv
import matplotlib.pyplot as bildschirmausgabe
from datetime import datetime

# Store the path to the file that is to be examined
quelle = 'data/sitka_weather_2018_simple.csv'

# Open the file with an alias of "q"
with open(quelle) as q:
	# Call the csv-reader and pass "q" to it - store it in a variable called reader
	reader = csv.reader(q)
	# Call the next-function and pass the variable reader
	# next creates a list (header_row) of the extracted line - the header-line in this case
	header_row = next(reader)
	# print the variable header_row
	print(header_row)

	# Loop with for through the list header_row but use enumerate to count the iterations
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# Get high temperatures from the file, store them in a list
	# Create the lists
	all_dates, all_highs = [], []
	# Loop through reader
	for each_row in reader:
		# extract the date
		# take the 3rd element, index is 2 and store it as days_date
		days_date = datetime.strptime(each_row[2], '%Y-%m-%d')
		# append it to the all_dates list
		all_dates.append(days_date)

		# extract the high temperature
		# take the 6th element, index is 5 and store it as days_high
		days_high = int(each_row[5])
		# append it to the all_highs list
		all_highs.append(days_high)

	print(all_dates)
	print(all_highs)

# Plot the high temperatures.
bildschirmausgabe.style.use('seaborn')
fig, ax = bildschirmausgabe.subplots()

# Format the plot.
# Pass both lists to plot-function and colour the resulting line in red
ax.plot(all_dates, all_highs, c='red')
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
# Draw the date labels diagonally
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

bildschirmausgabe.show()