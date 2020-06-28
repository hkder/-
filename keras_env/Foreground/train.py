from keras.layers import ConvLSTM2D, BatchNormalization, Conv2D
from keras.models import Sequential, save_model
import cv2
import numpy as np


def merge_cloud(cloud):
    bg = cv2.imread('./Background.png', 0) / 255
    return np.where(cloud > 0.5, 1, bg).astype('float32')


if __name__ == "__main__":
    train_set, train_label = (
        np.load('./train_set.npy').astype('float32'),
        np.load('./train_label.npy').astype('float32'))
    test_set, test_label = (
        np.load('./test_set.npy').astype('float32'),
        np.load('./test_label.npy').astype('float32'))

    model = Sequential()
    model.add(ConvLSTM2D(5, (3, 3), input_shape=(3, 224, 224, 1),
                         padding='same', return_sequences=True))
    model.add(BatchNormalization())
    model.add(ConvLSTM2D(3, (3, 3), padding='same', return_sequences=True))
    model.add(BatchNormalization())
    model.add(ConvLSTM2D(3, (3, 3), padding='same'))
    model.add(Conv2D(1, (3, 3), padding='same', activation='sigmoid'))
    model.summary()

    model.compile(optimizer='adadelta', loss='binary_crossentropy')

    EPOCHS = 50
    BATCH_SIZE = 16

    model.fit(train_set, train_label,
              epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1,
              validation_data=(test_set, test_label))

    result = model.predict(train_set)
    save_model(model, 'weights.h5')
    for image in result:
        image = image.reshape(image.shape[:2])
        cv2.imshow("result", merge_cloud(image))
        if cv2.waitKey() & 0xFF == ord('q'):
            break
