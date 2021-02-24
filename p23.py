"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/21 2:10 下午
@Site    : 
@File    : p23.py
@Software: PyCharm
"""
import tensorflow as tf


c1 = tf.constant([[2, 3], [1, 4], [5, -1]])
print(c1)

v1 = tf.get_variable('aaa', [4, 5], tf.float32, tf.initializers.ones)
print(v1)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    print(session.run([c1, v1]))