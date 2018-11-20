
# coding: utf-8

# In[1]:


# encoding: utf-8


import os
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.decomposition import PCA
from sklearn import metrics
import tensorflow as tf


# In[2]:


LABELS_TXT = 'digits4000_digits_labels.txt'
VECS_TXT = 'digits4000_digits_vec.txt'
VEC_LENGTH = 784
CLASS_NUM = 10
BATCH_SIZE = 64


# In[3]:


labels_df = pd.read_csv(LABELS_TXT, header=None, names=['label'])
labels = labels_df['label']
vecs_df = pd.read_csv(VECS_TXT, sep='\t', header=None, names=['f_{}'.format(i) for i in range(VEC_LENGTH)])
vecs_df = vecs_df / 255.

# check
print('labels_df.shape:', labels_df.shape)
print('labels.shape:', labels.shape)
print('vecs_df.shape:', vecs_df.shape)


# In[4]:


def to_one_hot(y_, class_num):
    label_num = y_.shape[0]
    one_hot_vecs = np.zeros((label_num, class_num))
    for i in range(label_num):
        one_hot_vecs[i][y_[i]] = 1
    return one_hot_vecs


# In[5]:


X_train = vecs_df[0: 2000]
y_train = labels_df['label'][0: 2000]
X_test = vecs_df[2000: ]
y_test = labels_df['label'][2000: ]

# 乱序
X_train, y_train = shuffle(X_train, y_train)

# 重新索引
X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)

# check
# print('y_train:', y_train)

# 转 one-hot 向量
y_train = to_one_hot(y_train, CLASS_NUM)
y_test = to_one_hot(y_test, CLASS_NUM)

# check
# for x in y_train:
#     print(x)
    
# for x in y_test:
#     print(x)

# check
print('X_train type:', type(X_train))
print('X_test type:', type(X_test))
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train type:', type(y_train))
print('y_test type:', type(y_test))
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)


# In[6]:


start_idx = 0
def next_batch(batch_size=BATCH_SIZE):
    global start_idx
    idx = start_idx
    if idx + batch_size > X_train.shape[0]:
        start_idx = 0
        return X_train[idx: ], y_train[idx: ]
    else:
        start_idx += batch_size
        return X_train[idx: idx + batch_size], y_train[idx: idx + batch_size]


# In[ ]:


sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
x_image = tf.reshape(x, [-1, 28, 28, 1])

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

tf.global_variables_initializer().run()

for i in range(3000):
    
    batch_xs, batch_ys = next_batch(64)
    
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1.0})
        print('step {}, training accuracy {:4f}'.format(i, train_accuracy))
    
    train_step.run(feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 0.5})
print('test accuracy {:4f}'.format(accuracy.eval(feed_dict={x: X_test, y_: y_test, keep_prob: 1.0})))

