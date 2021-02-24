"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/21 4:22 下午
@Site    : 
@File    : p25_two_x.py
@Software: PyCharm
"""
import tensorflow as tf

x1 = tf.get_variable('x', [], tf.float32, tf.initializers.ones)
a = tf.placeholder(tf.float32, [], 'a')
lr = tf.placeholder(tf.float32, [], 'lr')
y = (x1 * 2 - a) ** 2
opt = tf.train.GradientDescentOptimizer(lr)
train_op = opt.minimize(y)


def sqrt(a_v, lr_v=0.001, epoches=2000):
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        for _ in range(epoches):
            session.run(train_op, {a: a_v, lr: lr_v})
        return session.run(x)


def main():
    for x in range(1, 11):
        print("sqrt{} = {}".format(x, sqrt(x)))


main()
