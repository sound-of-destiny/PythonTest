import tensorflow as tf
# 获得数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 输入图像数据占位符
x = tf.placeholder(tf.float32, [None, 784])

# 权值和偏差
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 使用softmax模型
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 代价函数占位符
y_ = tf.placeholder(tf.float32, [None, 10])

# 交叉熵评估代价
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# 使用梯度下降算法优化：学习速率为0.5
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Session
sess = tf.InteractiveSession()

# 初始化变量
tf.global_variables_initializer().run()

# 训练模型，训练1000次
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 计算正确率
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

