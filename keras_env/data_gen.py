import cv2
from glob import glob
from os import path

for filepath in glob('../data/jpg/*.jpg'):
    image = cv2.imread(filepath)
    image = cv2.resize(image, (224, 224))
    cv2.imwrite(f'./DataSet/{path.basename(filepath)}', image)
