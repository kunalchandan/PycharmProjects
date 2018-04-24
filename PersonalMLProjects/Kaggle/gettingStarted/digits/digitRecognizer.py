import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
np.random.seed(2)

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools

from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau


train = pd.read_csv('train.csv', delimiter=',')
test = pd.read_csv('test.csv', delimiter=',')
Y_train = train["label"]
X_train = train.drop(labels=["label"], axis=1)

del train
g = sns.countplot(Y_train)

print(Y_train.value_counts())
print(X_train.isnull().any().describe())

X_train = X_train / 255.0
test = test / 255.0

X_train = X_train.values.reshape(-1, 28, 28, 1)
test = test.values.reshape(-1, 28, 28, 1)

Y_train = to_categorical(Y_train, num_classes=10)

rand_seed = 2

X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.1, random_state=rand_seed)

g = plt.imshow(X_train[0][:, :, 0])
plt.show()
