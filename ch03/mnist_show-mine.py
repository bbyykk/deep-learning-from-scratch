# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 愛囥佇和書頂仔仝款ê 目錄deep-learning-from-scratch/ch03/
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

yaxis = 0
img3 = None
for i in range(20):
    img = x_train[i]
    label = t_train[i]
    print(label)  # 印出這張ê真正數字
    
    if i == 0:
        img3 = img
    else:
        img3 = np.append(img3, img)

    yaxis = 28 + yaxis # y 杆一直疊起--lih

img3 = img3.reshape(yaxis, 28)  # 共伊tsiânn-tsuè 二維陣列, 予 img_show 用
print(img3.shape)  # (28, 28)

img_show(img3)
