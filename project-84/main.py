import keras
import tensorflow.keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from keras.constraints import maxnorm
from keras.utils import np_utils
from tensorflow.keras.optimizers import SGD
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive

drive.mount('/content/drive')

dataset_path = '/content/drive/MyDrive/PetDataset/'

data_gen = ImageDataGenerator()
dataset_stream = data_gen.flow_from_directory(
    directory=dataset_path,
    target_size=(32, 32),
    batch_size=100,
    class_mode='sparse',
    shuffle=True,
    seed=42
)

x_all, y_all = next(dataset_stream)

split_index = int(0.8 * len(x_all))
x_train, x_test = x_all[:split_index], x_all[split_index:]
y_train, y_test = y_all[:split_index], y_all[split_index:]

for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i].astype('uint8')) 
plt.show()

from tensorflow.keras.utils import to_categorical
num_classes = 2

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape, 'train samples')
print(x_test.shape, 'test samples')

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32,32,3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

print(model.summary())

opt = SGD(learning_rate=0.01, momentum=0.9, decay=0.0002, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
