import cv2
import numpy as np


def find_cloud(source):
    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    return np.where(source > 200, 255, 0).astype('uint8')

