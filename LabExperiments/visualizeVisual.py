import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('pilotData.csv')
numDis = []
print(data.numberDistractors.iloc[0])
delay = [-10, 0, 20, 40, 60, 80, 100]
for each in range(0,28):
    plt.plot(range(0,50), data.numberDistractors.iloc[each*50:(each+1)*50])
    print(each*50)
    # plt.plot(data.trial, np.equal(data.isAnimal,data.response))
    plt.show()
