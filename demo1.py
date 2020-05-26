import tensorflow.compat.v1 as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# import tensorflow as tf
# hello = tf.constant('Hello tensorfolw')
# sess = tf.Session()
# print(sess.run(hello))
# print(tf.__version__)




#张量的形状
#创建占位op
# plt=tf.placeholder(shape=[None,2],dtype=tf.int32,name="plt")
# plt=tf.placeholder(shape=[2,3],dtype=tf.int32,name="plt")
# print(plt)
#静态改变张量形状set_shape 只能更改不确定阶上比如None
# plt.set_shape(shape=[1,3])
#动态改变张量形状reshape  想怎么改就怎么改，但是元素个数不能发生变化
# plt=tf.reshape(plt,shape=[3,2])
# plt=tf.reshape(plt,shape=[1,2])#错误的改法，元素个数发生变化
# plt=tf.reshape(plt,shape=[1,2,1,3,1])
# print(plt)


# with tf.Session() as ss:
#      # print(ss.run(plt,feed_dict={plt:[[1,2],[3,4]]}))
#      print(ss.run(plt,feed_dict={plt:[[1,2]]}))

#张量的创建
#创建一个符合随机正太分布的张量
# x=tf.random_normal(shape=[2,2],mean=0.0,stddev=1.0,dtype=tf.float32,name='x')
#
# print(x)

#
a=tf.constant(1,name="a",dtype=tf.float32)
# # print(a)
# a=tf.cast(a,dtype=tf.int64)
# print(a)
# with tf.Session() as ss:
#     print(ss.run(x))
#     print(ss.run(a))
b=tf.constant(1.5,name="b")
c=tf.add(a,b)
# print(a)
# print(b)
# print(c)
# con_j=tf.placeholder(dtype=tf.int32,shape=[2,2],name="con_j")
# print(con_j)
# with tf.Session() as ss:
#     print(ss.run(fetches=[a,b,c]))
#     print(ss.run(con_j,feed_dict={con_j:[[2,1],[3,4]]}))
with tf.Session() as ss:
    #序列化events文件
    tf.summary.FileWriter("./tmp",graph=ss.graph)
    print(ss.graph)
    print(a.graph)
    # print(ss.run(c.graph))
    print(ss.run(c))

# g=tf.Graph()
#
# with g.as_default():
#     con_g=tf.constant(5.0)
#     # print(con_g)
#
# with tf.Session(graph=g) as ss:
#     print(ss.graph)
#     print(tf.get_default_graph())
#     print(ss.run(con_g))