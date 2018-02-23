import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import pandas as pd


train = pd.read_csv('train.csv', delimiter=',')
print(train.shape)


image1 = np.array((29, 28))
print(train[0][0])
np.delete(train, 0, axis=1)
print(train[0][0])

for each in range(len(train[0]-1)):
    image1[int(each/28)][(each%28)] = train[each][3]
print(image1)
# BTW above step is completely useless now that i think about it
