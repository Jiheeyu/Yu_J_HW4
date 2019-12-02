import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns


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

# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [51, 15, 4]
bars2 = [26, 26, 9]
bars3 = [10, 33, 15]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#fea63e', width=barWidth, edgecolor='white', label='Gold')
plt.bar(r2, bars2, color='#867e74', width=barWidth, edgecolor='white', label='Sliver')
plt.bar(r3, bars3, color='#803e2d', width=barWidth, edgecolor='white', label='Bronze')
 
# Add xticks on the middle of the group bars
plt.title("Asians Skating Medal Wins")
plt.xlabel('Country')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Korea', 'China', 'Japan'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
