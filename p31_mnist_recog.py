#!/usr/bin/env python 
# encoding: utf-8 


"""
@author: Wu Wentong
@software: PyCharm
@file: p31_mnist_recog.py
@time: 2021/2/28 15:33
"""
from tensorflow.examples.tutorials.mnist.input_data import read_data_sets
import tensorflow as tf
import numpy as np


class Tensors:
    def __init__(self, mid_units=2000):
        """
        the member variables: img, label train_op, lr
        """
        self.img = tf.placeholder(tf.float32, [None, 784], "img")
        self.label = tf.placeholder(tf.float32, [None], 'label')
        self.lr = tf.placeholder(tf.float32, [], "lr")

        t = tf.layers.dense(self.img, mid_units, activation=tf.nn.relu)  # 自动创建FC层完成矩阵计算和偏置相加,最后使用relu激活
        t = tf.layers.dense(t, 10)
        self.predict = tf.argmax(t, axis=1)
        p = tf.nn.softmax(t)

        label = tf.one_hot(self.label, 10)
        loss = tf.reduce_mean(tf.square(p - label))
        opt = tf.train.AdamOptimizer(self.lr)

        self.train_op = opt.minimize(loss)


class Model:
    def __init__(self, lr=0.01, batch_size=100, epoches=20):
        self.lr = lr
        self.batch_size = batch_size
        self.epoches = epoches
        self.tesors = Tensors()
        self.session = session
        self.dss = read_data_sets("../MNIST_data")

    def train(self):
        batches = self.dss.train.num_examples // self.batch_size
        ts = self.tesors
        self.session.run(tf.global_variables_initializer())
        for epoch in range(self.epoches):
            for batch in range(batches):
                imgs, lables = self.dss.train.next_batch(self.batch_size)
                self.session.run(ts.train_op,{ts.lr:self.lr, ts.img: imgs, ts.label: labels})
            print('epoch %d finished' % epoch)
        print("training is finished")

    def test(self):
        pass


if __name__ == '__main__':
    with tf.Session() as session:
        model = Model()
        model.train()
        model.test()
