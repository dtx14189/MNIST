import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from matplotlib import pyplot

from keras.datasets import mnist

(train_X, train_y), (test_X, test_y) = mnist.load_data()

i = 30
print(test_y[i])
pyplot.subplot(331 + i)
pyplot.imshow(test_X[i], cmap=pyplot.get_cmap('gray'))
pyplot.show()