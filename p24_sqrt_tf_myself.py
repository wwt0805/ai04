"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/22 9:56 上午
@Site    : tensorflow运行个人总结：
            1. 对于预算中的常量使用placeholder占位符进行定义, 比如lr、计算中的常数等；
            2. 对于运算中的变量使用get_variable进行定义（格式：名字，形状，类型，（初始化）），注意和pyTorch的Variable对比记忆；
            3. 选择合适的优化器，如GD，Adam等
            4. 根据程序逻辑构建计算图（可以是方程、网络）；
            5. 创建会话Session。再会话中主要进行两部操作：
                a. 对全局变量初始化，包括所有的variable
                b. run构建完成的图模型，返回所需要的相应结果
@File    : p24_sqrt_tf_myself.py
@Software: PyCharm
"""
# 计算 y = (x - a) ** 2, 即计算一个数的平方根
import tensorflow as tf
import logging
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
logging.basicConfig(level=logging.DEBUG)


a = tf.placeholder(tf.float32, [], "a")
lr = tf.placeholder(tf.float32, [], "lr")
# 得到正的平方根，对x初始化都要大于1，要得到负平方根只需要对x初始化全为负即可
x = tf.get_variable("x", [], tf.float32, initializer=tf.initializers.ones)
y = (x ** 2 - a) ** 2
opt = tf.train.GradientDescentOptimizer(learning_rate=lr)


def calculate(a_init, lr_init, epoches):
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())  # 不建议将初始化写入循环，否则每次循环执行都会初始化，不合理。
        for i in range(epoches):
            session.run(opt.minimize(y), feed_dict={a: a_init, lr: lr_init})
        return session.run(x)


if __name__ == "__main__":
    for i in range(1, 11):
        print("Positive square root of {} is {:.3f}".format(i, calculate(i, 0.01, 50)))






