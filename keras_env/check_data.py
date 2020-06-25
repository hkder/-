import cv2
import numpy as np

before = np.load('./before.npy', allow_pickle=True)
after = np.load('./after.npy', allow_pickle=True)

print(before[0].shape)
print(after.shape)
#print(before[0])
