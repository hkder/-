import cv2
from keras.models import load_model
import numpy as np


def merge_cloud(cloud):
    bg = cv2.imread('./Background.png', 0) / 255
    return np.where(cloud > 0.7, 1, bg).astype('float32')


model = load_model('weights.h5')
original = np.load('./train_label.npy').astype('float32')

seed = list(original[:3])
train_set = original[3:]

for image in train_set:
    result = model.predict(np.array([seed]))[0]
    seed.pop(0)
    seed.append(result.copy())
    cv2.imshow('result', merge_cloud(result.reshape(result.shape[:2])))
    cv2.imshow('original', merge_cloud(image.reshape(image.shape[:2])))
    if cv2.waitKey() & 0xFF == ord('q'):
        break
