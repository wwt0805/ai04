import numpy as np
from matplotlib import pyplot as plt
import math
import tensorflow as tf

mid_units = 1000
num_samples = 1000  # 样本少再多的神经元也不能得到很好的结果，如果样本质量不好，则需要调小对应的神经元个数避免过拟合学习到噪声点和离群点。数量、质量和分布


def get_tensors(lr=0.001):
    x = tf.placeholder(tf.float32, [None], 'x')
    z = tf.placeholder(tf.float32, [None, 2], 'z')

    t = tf.expand_dims(x, 1)                                # [None, 1]
    w1 = tf.get_variable('w1', [1, mid_units], tf.float32)
    t = tf.matmul(t, w1)                                    # [None, mid_units]
    b1 = tf.get_variable('b1', [mid_units], tf.float32)
    t += b1                                                 # [None, mid_units]

    t = tf.nn.relu(t)
    w2 = tf.get_variable('w2', [mid_units, 2], tf.float32)
    predict = tf.matmul(t, w2)                              # [None, 2]
    # predict = tf.reshape(predict, [-1])                     # [None]

    loss = tf.reduce_mean(tf.square(predict - z))           # **2, === np.mean(), shape: []

    opt = tf.train.AdamOptimizer(lr)
    train_op = opt.minimize(loss)

    return x, z, predict, train_op


def train(tensors, samples, session, epoches=3000):
    x, z, _, train_op = tensors
    xs, zs = samples
    print('training is started!')
    for _ in range(epoches):
        session.run(train_op, {x: xs, z: zs})
    print('training is finished!!!')


def predict(tensors, xs, session):
    x, _, predict, _ = tensors
    return session.run(predict, {x: xs})


def main():
    xs = np.arange(0, 2 * math.pi, 2 * math.pi / (num_samples - 1))  # range(4, 10+1, 2)
    zs = [np.sin(xs) + np.cos(xs)]  # [2, num_samples]
    zs = np.transpose(zs)           # [num_samples, 2]
    plt.plot(xs, zs)

    with tf.Session() as session:
        tensors = get_tensors()  # x, predict, train_op
        session.run(tf.global_variables_initializer())
        train(tensors, (xs, zs), session)

        xs = np.random.uniform(-math.pi / 2, 2.5 * math.pi, [600])
        xs = np.sort(xs)
        zs = predict(tensors, xs, session)  # [None, 2]

    plt.plot(xs, zs)
    plt.show()


main()
