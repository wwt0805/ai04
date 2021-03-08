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


class Tensors:
    def __init__(self, mid_units=2000):
        """
        the member variables: img, label train_op, lr
        """
        self.img = tf.placeholder(tf.float32, [None, 784], "img")  # placeholder的不确定数为None，不是-1
        self.label = tf.placeholder(tf.int32, [None], 'label')
        self.lr = tf.placeholder(tf.float32, [], "lr")

        t = tf.layers.dense(self.img, mid_units, activation=tf.nn.relu)  # 自动创建FC层完成矩阵计算和偏置相加,最后使用relu激活
        t = tf.layers.dense(t, 10)  # 得到最后一层全连接，输出10维表示最后的10个类别
        self.predict = tf.argmax(t, axis=1)  # t里面最大的值就是当前的预测值,列所在的维度
        p = tf.nn.softmax(t)

        label = tf.one_hot(self.label, 10)  # 每一个label转成一个10维向量[-1, 10]
        loss = tf.reduce_mean(tf.square(p - label))
        opt = tf.train.AdamOptimizer(self.lr)

        self.train_op = opt.minimize(loss)


class Model:
    def __init__(self, session, lr=0.01, batch_size=100, epoches=20):
        self.lr = lr
        self.batch_size = batch_size
        self.epoches = epoches
        self.tesors = Tensors()  # 获取张量
        self.session = session
        self.dss = read_data_sets("../MNIST_data")

    def train(self):
        print("Training is started")
        batches = self.dss.train.num_examples // self.batch_size
        ts = self.tesors
        self.session.run(tf.global_variables_initializer())
        for epoch in range(self.epoches):
            for _ in range(batches):
                imgs, labels = self.dss.train.next_batch(self.batch_size)  # imgs: [bs, 784], labels:[bs]
                self.session.run(ts.train_op, {ts.lr: self.lr, ts.img: imgs, ts.label: labels})
            print('epoch %d finished' % epoch)
        print("training is finished")

    def test(self):
        pass


if __name__ == '__main__':
    with tf.Session() as session:
        model = Model(session)
        model.train()  # 训练
        model.test()  # 测试
