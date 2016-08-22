
import tensorflow as tf
import Image

im = Image.open("../Image/bower-logo.png")

print im.format, im.size, im.mode

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.mul(a, b)

sess = tf.Session()

print sess.run(y, feed_dict={a: 3, b: 3})


