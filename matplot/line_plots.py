import matplotlib.pyplot as plt
import numpy as np

gas = np.array([50,40,20,50,10,50,60,30,60,30,40,80])
electric = np.array([100,200,150,90,175,250,186,185,178,165,153,200])
month = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

plt.figure()
plt.plot(month, gas, label='Gas bill per month')
plt.plot(month, electric, label='Electric bill per month')

plt.title('Bill Tracking')
plt.xlabel('Month of the Year')
plt.ylabel('USD')

plt.legend()
plt.show()