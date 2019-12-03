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


# Data
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })
 
# multiple line plot
plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.legend()

