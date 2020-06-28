import cv2
import numpy as np


def merge_cloud(cloud):
    bg = cv2.imread('./Background.png', 0) / 255
    return np.where(cloud > 0.5, 1, bg).astype('float32')


if __name__ == "__main__":
    train_set, train_label = (
        np.load('./train_set.npy'), np.load('./train_label.npy'))
    test_set, test_label = (
        np.load('./test_set.npy'), np.load('./test_label.npy'))

    for data, label in zip(train_set, train_label):
        data = data.reshape(data.shape[:3])
        label = label.reshape(label.shape[:2])
        for i in range(3):
            if i == 0:
                sequence = cv2.resize(merge_cloud(data[i]), (100, 100))
            else:
                sequence = cv2.hconcat([sequence,
                                        cv2.resize(merge_cloud(data[i]),
                                                   (100, 100))])
        result = cv2.vconcat([sequence,
                              cv2.resize(merge_cloud(label), (300, 300))])
        cv2.imshow('data', result)
        if cv2.waitKey() & 0xFF == ord('q'):
            break
