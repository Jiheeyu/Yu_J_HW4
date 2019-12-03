import csv
import numpy as np
import matplotlib.pyplot as plt

KOR = []
CHN = []
JPN = []

categories = [] # first row -> not data

with open('Asianmedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[4] == "KOR":
				print("Korea won medals")
				KOR.append(row[7])
			elif row[4] == "CHN":
				print("China won medals")
				CHN.append(row[7])
			else: 
				print("Japan won medals")
				JPN.append(row[7])

			print(line_count)
			line_count += 1
#now we can see our medal counts
print(len(KOR), "Korea won medals")
print(len(CHN), "China won medals")
print(len(JPN), "Japan won medals")

labels = ["Korea", "China", "Japan"]
sizes = [len(KOR), len(CHN), len(JPN)]
colors = ['#3ea1fe', '#fe3e4b', '#fea63e']



plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Asians Skating Medal Wins")
plt.xlabel("Medal Counts")
plt.show()