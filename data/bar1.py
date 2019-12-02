import numpy as np
import matplotlib.pyplot as plt
 

height = [87, 74, 28]
bars = ('Korea', 'China', 'Japan')
y_pos = np.arange(len(bars))
 

plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.title("Total Medal Counts of Asian in Skating")
plt.show()
