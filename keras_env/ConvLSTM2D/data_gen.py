import numpy as np
import cv2
from glob import glob

train_set = []
train_label = []
test_set = []
test_label = []

DEPTH = 3

buffer = []

for i, file in enumerate(glob('../../data/GK2A/Train/*.png')):
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) / 255
    if i < DEPTH:
        buffer.append(image.copy())
    else:
        train_set.append(buffer.copy())
        train_label.append(image)
        buffer.pop(0)
        buffer.append(image)

print(np.array(train_label).shape, np.array(train_set).shape)

buffer = []

for i, file in enumerate(glob('../../data/GK2A/Test/*.png')):
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) / 255
    if i < DEPTH:
        buffer.append(image.copy())
    else:
        test_set.append(buffer.copy())
        test_label.append(image)
        buffer.pop(0)
        buffer.append(image)

print(np.array(test_label).shape, np.array(test_set).shape)

np.save('./train_set', np.array(train_set))
np.save('./train_label', np.array(train_label))
np.save('./test_set', np.array(test_set))
np.save('./test_label', np.array(test_label))
