import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./gearsparks_emporium_weekly_sales.csv')

plt.figure()
plt.plot(df['Day'], df['Weapon'], label='Weapon Sales', color='blue', linestyle='-.')

plt.title('Gearsparks Emporium Weekly Sales')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Weapons Sold')

plt.legend()
plt.show()