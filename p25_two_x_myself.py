"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/22 2:00 下午
@Site    :  1. 对于预算中的常量使用placeholder占位符进行定义, 比如lr、计算中的常数等；
            2. 对于运算中的变量使用get_variable进行定义（格式：名字，形状，类型，（初始化）），注意和Variable对比记忆；
            3. 选择合适的优化器，如GD，Adam等
            4. 根据程序逻辑构建计算图（可以是方程、网络）；
            5. 创建会话Session。再会话中主要进行两部操作：
                a. 对全局变量初始化，包括所有的variable
                b. run构建完成的图模型，返回所需要的相应结果
@File    : p25_two_x_myself.py
@Software: PyCharm
"""
import tensorflow as tf
import warnings
import numpy as np
import matplotlib.pyplot as plt
import logging
import time
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO)


# 计算 y = (x1 - 3) ** 2 + (x2 + 1) ** 2 + x3 ** 2 的最小值，以及取得最小值时的x1、x2、x3
a = tf.placeholder(tf.float32, [], "a")
b = tf.placeholder(tf.float32, [], "b")
c = tf.placeholder(tf.float32, [], "c")
x1 = tf.get_variable("x1", [], tf.float32)
x2 = tf.get_variable("x2", [], tf.float32)
x3 = tf.get_variable("x3", [], tf.float32)
lr = tf.get_variable("lr", [], tf.float32)
y = (x1 + a) ** 2 + (x2 + b) ** 2 + (x3 * c) ** 2


def calculate(a_init, b_init, c_init, lr_init, epoches):
    """

    :param a_init: a的初始值
    :param b_init: b的初始值
    :param c_init: c的初始值
    :param lr_init: 学习率的初始值
    :param epoches: 迭代轮次
    :return: 返回值为求解的x1,x2,x3列表
    """
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        train_op = tf.train.GradientDescentOptimizer(learning_rate=lr)
        total_loss = []
        for i in range(epoches):
            session.run(train_op.minimize(y), feed_dict={a: a_init, b: b_init, c: c_init, lr: lr_init})
            # true_value = [3, -1, 0]相当于真实标签，可以用来计算loss
            loss = ((session.run(x1) - 3) ** 2 + (session.run(x2) - (-1)) ** 2 + session.run(x3) ** 2) / 3
            total_loss.append(loss)
            if i % 20 == 0:
                print("{} iters --> loss:{} --> result:{}".format(i, loss, session.run([x1, x2, x3])))
            if len(total_loss) >= 2 and abs((total_loss[-1] - total_loss[-2]) / total_loss[-2]) < 0.1:   # 连续两次迭代变化率小于10%
                logging.info("Satisfy the change rate")
                if total_loss[-1] < 1e-5:   # 损失收敛值ε
                    logging.info("Satisfy the loss request")
                    break
        draw_graph(total_loss, len(total_loss))
        return session.run([x1, x2, x3])


def draw_graph(loss, iter):
    plt.figure(figsize=(10, 8))
    plt.subplot(1, 2, 1)
    plt.plot(np.arange(iter), loss)
    plt.ylim(0)
    plt.xlim(0)
    plt.title("Global Loss")
    plt.grid(True)
    plt.subplot(1, 2, 2)
    plt.plot(np.arange(iter - 50, iter), loss[-50:])
    plt.ylim(0)
    plt.grid(True)
    plt.title("The last 50 iteration loss")
    plt.show()


if __name__ == "__main__":
    start = time.time()
    print("True values are: [3, -1, 0]; Calculation is: ", calculate(-3, 1, 2, 0.01, 300))
    end = time.time()
    print("Running time: {}".format(end - start))
