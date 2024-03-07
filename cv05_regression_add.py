import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

with np.load('cv05data.npz') as npz_file:
    # print(npz_file.keys())
    xt = npz_file['xt']
    yt = npz_file['yt']

model = keras.models.Sequential()
model.add(keras.Input(shape=(1,)))

model.add(keras.layers.Dense(10, acrivation='relu'))
model.add(keras.layers.Dense(10, acrivation='relu'))

model.add(keras.layers.Dense(1, acrivation='linear'))

model.compile(keras.layers.Dense(10, acrivation='relu'))

model.fit(xt.resgaoe(-1,1), yt.reshape(-1,1), epochs = 500)

x = np.linspace(-2, 3, 1000)
y_out = model.predict(x.reshape(-1,1))

plt.plot(x, y_out, 'b', xt, yt, 'ro')
plt.show()