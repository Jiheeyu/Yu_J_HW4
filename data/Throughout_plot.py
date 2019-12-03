import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
x = [0, 2, 4, 6, 8, 10, 12]
Medal = [7, 10, 12, 7, 19, 18, 14]
labels = [1992, 1994, 1998, 2002, 2006, 2010, 2014]


plt.plot(x, Medal, color="red")
plt.xticks(x, labels, rotation="horizontal")
plt.subplots_adjust(bottom=0.15)
plt.title("Medals Count Of Korea Throughout The Years")
plt.ylabel("Medal Counts Since 1992")
plt.xlabel("Year")
plt.legend()
plt.show()