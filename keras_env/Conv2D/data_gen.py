import cv2
from glob import glob
import numpy as np

before = []
after = []
image = None
for file in glob('./DataSet/*.jpg'):
    before.append(image)
    image = cv2.imread(file) / 255
    after.append(image)

np.save('before.npy', np.array(before[1:]), allow_pickle=True)
np.save('after.npy', np.array(after[:-1]), allow_pickle=True)
