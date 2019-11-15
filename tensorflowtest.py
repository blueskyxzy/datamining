#!/usr/bin/python 
# -*- coding: utf-8 -*-

import tensorflow as tf

a = tf.constant([1., 2., 3.], name="a")
b = tf.constant([4., 5., 6.], name="b")
c = tf.constant([0., 4., 2.], name="c")
add = a + b
mul = add * c
with tf.Session() as sess:
    # fetch  获取对应张量
    result = sess.run([a, b, c, add, mul])
    print("fetch :\n", result)

# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
# output = tf.multiply(input1, input2)
# with tf.Session() as session:
#     # 喂数据 feed_dict
#     result_feed = session.run(output, feed_dict={input1: [2.], input2: [3.]})
#     print("result:", result_feed)
