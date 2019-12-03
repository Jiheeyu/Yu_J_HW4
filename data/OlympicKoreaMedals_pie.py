import csv
import numpy as np
import matplotlib.pyplot as plt

Women = []
Men = []

categories = [] # first row -> not data

with open('Koreamedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[5] == "Women":
				print("Women won medals")
				Women.append(row[5])
			else:
				print("Man won medals")
				Men.append(row[5])

			print(line_count)
			line_count += 1
#now we can see our medal counts
print(len(Women), "Women medals")
print(len(Men), "Men medals")

labels = ["Women", "Men"]
sizes = [len(Women), len(Men)]
colors = ['#cc3745', '#3b9423']



plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Korea Skating Medal Wins - between Woman and Man")
plt.xlabel("Medal Counts Since 1992")
plt.show()