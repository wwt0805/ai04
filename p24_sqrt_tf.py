"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/21 3:05 下午
@Site    : 
@File    : p24_sqrt_tf.py
@Software: PyCharm
"""
import tensorflow as tf
x = tf.get_variable('x', [], tf.float32, tf.initializers.ones)
a = tf.placeholder(tf.float32, [], 'a')
lr = tf.placeholder(tf.float32, [], 'lr')
y = (x ** 2 - a) ** 2
opt = tf.train.GradientDescentOptimizer(lr)
train_op = opt.minimize(y)
session = tf.Session()
session.run(tf.global_variables_initializer())


def sqrt(a_v, lr_v=0.001, epoches=2000):
        for _ in range(epoches):
            session.run(train_op, {a: a_v, lr: lr_v})
        return session.run(x)


def main():
    with session:
        for x in range(1, 11):
            print("sqrt{} = {}".format(x, sqrt(x)))


main()
