import cv2
from keras.models import load_model
import numpy as np


model = load_model('adadelta-binary.h5')
original = np.load('./test_label.npy')

seed = list(original[:3])
train_set = original[3:]

for image in train_set:
    result = model.predict(np.array([seed]))[0]
    seed.pop(0)
    seed.append(result)
    cv2.imshow('result', result)
    cv2.imshow('original', image)
    if cv2.waitKey() & 0xFF == ord('q'):
        break
