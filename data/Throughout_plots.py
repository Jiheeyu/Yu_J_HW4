import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
 
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

x = [0, 2, 4, 6, 8, 10, 12]
Gold = [5, 8, 6, 5, 14, 6, 7]
Silver = [0, 1, 4, 2, 3, 10, 5]
Bronze = [1, 1, 2, 0, 2, 2, 2]
labels = [1992, 1994, 1998, 2002, 2006, 2010, 2014]


plt.plot(x, Gold, color="#fea63e", label='Gold')
plt.plot(x, Silver, color="#867e74", label='Silver')
plt.plot(x, Bronze, color="#803e2d", label='Bronze')
plt.xticks(x, labels, rotation="horizontal")
plt.subplots_adjust(bottom=0.15)
plt.title("Medals Count Of Korea Throughout The Years")
plt.ylabel("Medal Counts Since 1992")
plt.xlabel("Year")
plt.legend()
plt.show()