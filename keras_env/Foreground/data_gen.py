import cv2
import numpy as np
from glob import glob


def find_cloud(source):
    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    return np.where(source > 200, 1, 0).astype('float32')


train_set = []
train_label = []
test_set = []
test_label = []

DEPTH = 3

buffer = []

for i, file in enumerate(glob('../../data/GK2A/Train/*.png')):
    image = cv2.imread(file)
    cloud = find_cloud(image)[:, :, np.newaxis]
    if i < DEPTH:
        buffer.append(cloud.copy())
    else:
        train_set.append(buffer.copy())
        train_label.append(cloud)
        buffer.pop(0)
        buffer.append(cloud)

train_set = np.array(train_set)
train_label = np.array(train_label)
print(train_label.shape, train_set.shape)

buffer = []

for i, file in enumerate(glob('../../data/GK2A/Test/*.png')):
    image = cv2.imread(file)
    cloud = find_cloud(image)[:, :, np.newaxis]
    if i < DEPTH:
        buffer.append(cloud.copy())
    else:
        test_set.append(buffer.copy())
        test_label.append(cloud)
        buffer.pop(0)
        buffer.append(cloud)

test_set = np.array(test_set)
test_label = np.array(test_label)

print(test_label.shape, test_set.shape)

np.save('./train_set', train_set, allow_pickle=True)
np.save('./train_label', train_label, allow_pickle=True)
np.save('./test_set', test_set, allow_pickle=True)
np.save('./test_label', test_label, allow_pickle=True)
