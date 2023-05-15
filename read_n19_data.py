import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n19_data = pd.read_pickle('./datasets/infill_n19_energy_area.pkl')

print(n19_data.describe())

n19_data['logN19_Energy'] = np.log(n19_data['N19'] / n19_data['Eem'])

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111)

n19_data.hist(column='logN19_Energy', ax = ax, bins = 20)
ax.set_yscale('log')

plt.show()
