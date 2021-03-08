#!/usr/bin/env python 
# encoding: utf-8 

"""
@author:   Wu Wentong
@software: PyCharm
@file:     p30_mnist.py
@time:     2021/2/28 14:08
"""
import cv2
import numpy as np
from tensorflow.examples.tutorials.mnist.input_data import read_data_sets


dss = read_data_sets("../MNIST_data")
print(dss.train.num_examples)         # 训练集
print(dss.train.next_batch)
print(dss.validation.num_examples)    # 验证集，在训练过程中验证模型效果的
print(dss.test.num_examples)          # 测试集，在训练完成后评价模型效果的

imgs, labels = dss.train.next_batch(100)  # 返回imags和labels，可以进入函数查看。imgs: [10, 28*28], labels:[10]
print(labels[0])  # 显示第一个样本的标签

cols = 10
imgs = np.reshape(imgs, [-1, cols, 28, 28])  # 因为images只会返回整个维度，所以需要通过其他方式转化为二维即长和宽。把img reshap成[不确定的行,列,28,28]
imgs[:, :, 27, :] = 1.0  # 图片的第28行（索引第27）都设置为1，也就是每个小图片的最后一行
imgs[:, :, :, 0] = 1.0   # 每个图片的第1列（索引0）设置为1
imgs = np.transpose(imgs, [0, 2, 1, 3])  # 把col和28所在的维度进行交换

img = np.reshape(imgs, [-1, 28 * cols])  # [280, 280]
img[0, :] = 1.0
img[:, -1] = 1.0
cv2.imshow("My image", img)
cv2.waitKey()  # 等待键盘操作，否则图片会一闪而过。
