import cv2
import numpy as np

train_set, train_label = (
    np.load('./train_set.npy'), np.load('./train_label.npy'))
test_set, test_label = (
    np.load('./test_set.npy'), np.load('./test_label.npy'))

for data, label in zip(train_set, train_label):
    for image in data:
        cv2.imshow('data', cv2.cvtColor(image.astype('float32'), cv2.COLOR_RGB2BGR))
        cv2.waitKey(50)
    cv2.waitKey()
    cv2.imshow('data', cv2.cvtColor(label.astype('float32'), cv2.COLOR_RGB2BGR))
    if cv2.waitKey() & 0xFF == ord('q'):
        break
