from keras.layers import ConvLSTM2D, BatchNormalization
from keras.models import Sequential, save_model
import cv2
import numpy as np

train_set, train_label = (
    np.load('./train_set.npy'), np.load('./train_label.npy'))
test_set, test_label = (
    np.load('./test_set.npy'), np.load('./test_label.npy'))


model = Sequential()
model.add(ConvLSTM2D(5, (3, 3), input_shape=(3, 224, 224, 3),
                     padding='same', return_sequences=True))
model.add(BatchNormalization())
model.add(ConvLSTM2D(3, (3, 3), padding='same', activation='relu'))

model.summary()

model.compile(optimizer='adadelta', loss='binary_crossentropy')

EPOCHS = 10
BATCH_SIZE = 16

model.fit(train_set, train_label,
          epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1,
          validation_data=(test_set, test_label))


result = model.predict(train_set)
save_model(model, 'weights-relu.h5')
for image in result:
    cv2.imshow("result", image)
    if cv2.waitKey() & 0xFF == ord('q'):
        break
