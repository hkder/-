import cv2
import numpy as np
from keras.models import Sequential, save_model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D

before = np.load('before.npy', allow_pickle=True)
after = np.load('after.npy', allow_pickle=True)

model = Sequential()
model.add(Conv2D(128, (5, 5), input_shape=before[0].shape, padding='same'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(64, (2, 2), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(3, (5, 5), activation='relu', padding='same'))

model.summary()

model.compile(optimizer='adadelta', loss='binary_crossentropy')

EPOCHS = 100
BATCH_SIZE = 2

model.fit(before, after,
          epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)

result = model.predict(before)
save_model(model, 'weights.h5')
for image in result:
    cv2.imshow("result", image)
    if cv2.waitKey() & 0xFF == ord('q'):
        break
