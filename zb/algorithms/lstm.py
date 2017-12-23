# -*- coding: utf-8 -*-
"""
===================================================================================
LSTMs model

input   numpy.ndarray(1-D)

"""

import numpy as np
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.estimators.estimator import SKCompat
import matplotlib.pyplot as plt
learn = tf.contrib.learn


"""
========================================================================================
data preprocessing
"""

def timeseries_to_supervised(seq, timesteps=10):
    """transform seq to supervised datas"""
    X = []
    y = []
    for i in range(len(seq) - timesteps - 1):
        X.append([seq[i: i + timesteps]])
        y.append([seq[i + timesteps]])
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

# input data
import pandas as pd
f_csv = r"C:\DataWarehouse\sszt\2010_sszt_new.csv"
sszt_new = pd.read_csv(f_csv, index_col=[0], parse_dates=[0], encoding='gbk')
sszt_new = sszt_new.sort_index()

# split data & transform
new_value = sszt_new.values
X, y = timeseries_to_supervised(new_value.reshape(new_value.shape[0]), timesteps=1)
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)



"""
========================================================================================
create model
"""

# set parameters
HIDDEN_SIZE = 30    # 隐层神经元数量
NUM_LAYERS = 6     # 网络层数
TRAINING_STEPS = 3000
BATCH_SIZE = 6
KEEP_PROB = 0.5


def lstm_model(X, y):
    """define a lstm model"""
    def lstm_cell():
        if KEEP_PROB < 1:
            return tf.contrib.rnn.DropoutWrapper(
                tf.contrib.rnn.BasicLSTMCell(HIDDEN_SIZE, state_is_tuple=True),
                output_keep_prob=KEEP_PROB)
        else:
            return tf.contrib.rnn.BasicLSTMCell(HIDDEN_SIZE, state_is_tuple=True)

    cell = tf.contrib.rnn.MultiRNNCell([lstm_cell() for _ in range(NUM_LAYERS)])

    output, _ = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
    output = tf.reshape(output, [-1, HIDDEN_SIZE])

    # use fully connected layer to calculate predictions
    predictions = tf.contrib.layers.fully_connected(output, 1, None)
    predictions = tf.reshape(predictions, [-1])
    labels = tf.reshape(y, [-1])

    # define loss
    loss = tf.losses.mean_squared_error(predictions, labels)

    train_op = tf.contrib.layers.optimize_loss(loss, tf.contrib.framework.get_global_step(),
                                               optimizer="Adam", learning_rate=0.01)

    return predictions, loss, train_op


def create_regressor():
    regressor = SKCompat(learn.Estimator(model_fn=lstm_model, model_dir="Models/LSTMs1"))
    return regressor


def main():
    regressor = create_regressor()
    #
    # logdir = r"f:\log"
    # writer = tf.train.SummaryWriter(logdir, tf.get_dafault_graph())
    # writer.close()
    # print("tensorboard --logdir='%s'" % logdir)

    # fit model
    regressor.fit(train_X, train_y, batch_size=BATCH_SIZE,
                  steps=TRAINING_STEPS)

    # prediction
    predicted = [[pred] for pred in regressor.predict(test_X)]

    # calculate rmse
    rmse = np.sqrt(((predicted - test_y) ** 2).mean(axis=0))
    print("Root Mean Square Error is: %f" % rmse[0])


if __name__ == "__main__":
    main()

