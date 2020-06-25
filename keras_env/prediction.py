import cv2
from keras.models import load_model
import numpy as np

model = load_model('./weights.h5')

before = np.load('./before.npy', allow_pickle=True)
after = np.load('./after.npy', allow_pickle=True)

image = before[0]

for i in range(len(after) - 1):
    image = model.predict(np.array([image]))[0]
    cv2.imshow('result', image)
    cv2.waitKey(50)

cv2.imshow('result', image)
cv2.imshow('real', after[-1])
cv2.waitKey()
cv2.destroyAllWindows()
