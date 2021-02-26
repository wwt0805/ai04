"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/26 12:09 下午
@Site    : 求 y = x * sinx, 当y = 3 时的 x
@File    : p26_xsinx.py
@Software: PyCharm
"""
import tensorflow as tf
import math

x = tf.get_variable(name="x", shape=[], dtype=tf.float32, initializer=tf.initializers.constant(6))  # 根据结果投机了一个初始化常数
y = (x * tf.sin(x) - 3) ** 2  # 求x等价于，求x所对应y的最小值，也就是收敛域ε极小
lr = tf.get_variable(name="lr", shape=[], dtype=tf.float32)
train_op = tf.train.AdamOptimizer(lr).minimize(y)


def calculate(lr_init, steps=10000):
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        for _ in range(steps):
            session.run(train_op, feed_dict={lr: lr_init})
        return session.run(x)


if __name__ == "__main__":
    result = calculate(0.001)
    print("result:", result)
    print("validation:", result * math.sin(result))
