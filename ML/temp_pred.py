import tensorflow as tf               
import matplotlib.pyplot as plt     
import pandas as pd                 
import numpy as np                 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


#Normalization
def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)

#Find min max
def FindMinMax(data):
    Mindata = np.min(data, 0)
    Maxdata = np.max(data, 0)
    return Mindata, Maxdata

#Normalization solver 
def MinMaxReturn(val, Min, Max):
    return val * (Max - Min + 1e-7) + Min

#Model (LSTM)
def Model(x, y,  seq_length, iterations):
    ''' Main model '''
    dataX, dataY = [], []
    for i in range(0, seq_length - 1):
        size = i + seq_length
        _x = x[i : size] 
        _y = y[size : size + predict_length] 
        dataX.append(_x)
        dataY.append(_y)
    dataX = np.array(dataX)
    dataY = np.array(dataY)
    
    # train/test split
    train_size = int(len(dataY) * 0.8)
    trainX  = np.array(dataX[ : train_size])
    testX   = np.array(dataX[train_size : ])
    trainY  = np.array(dataY[ : train_size]) 
    testY   = np.array(dataY[train_size : ]) 
     
    # input place holders
    X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
    Y = tf.placeholder(tf.float32, [None, 1])

    cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_dim, 
                                        state_is_tuple = True, 
                                        activation = tf.tanh)
    def lstm_cell():
        ''' Use LSTM model '''
        cell = tf.contrib.rnn.BasicLSTMCell(hidden_dim, state_is_tuple=True) 
        return cell
    
    cell = tf.contrib.rnn.BasicLSTMCell(
        num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
    outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype = tf.float32)
    Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, 
                                               activation_fn = None)
    
    # cost/loss
    loss = tf.reduce_sum(tf.square(Y_pred - Y))  # sum of the squares
    # optimizer
    optimizer = tf.train.RMSPropOptimizer(learning_rate)
    train = optimizer.minimize(loss)
    
    # RMSE
    targets = tf.placeholder(tf.float32, [None, 1])
    predictions = tf.placeholder(tf.float32, [None, 1])
    rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))
    
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        # Training step    
        for i in range(iterations):
            _  ,cost = sess.run([train ,loss], 
                                 feed_dict={X: trainX, Y: trainY})
            if (i+1) % (iterations/20) == 0:
                print("[step: {}] loss: {}".format(i+1, cost))
        #train_predict = sess.run(Y_pred, feed_dict={X: trainX})
        test_predict = sess.run(Y_pred, feed_dict={X: testX})
        rmse_val = sess.run(rmse, feed_dict={
                        targets: testY, predictions: test_predict})
        print("RMSE: {}".format(rmse_val))

    return testY, test_predict


#Plot
def _draw(r1, r2):
    """ Draw RNN Train Result """
    plt.plot(r1)
    plt.plot(r2)
    plt.xlabel("Time Period")
    plt.ylabel("Temperature")
    line1, = plt.plot(r1, label='Test Y')
    line2, = plt.plot(r2, label='Predicted Y')
    plt.legend([line1, line2], ['Test Y', 'Predicted Y'])
    plt.show()



if __name__=="__main__":

    temp_2022 = pd.read_csv("temp_2022.csv", encoding="cp949")
    temp_2021 = pd.read_csv("temp_2021.csv", encoding="cp949")
    temp_2020 = pd.read_csv("temp_2020.csv", encoding="cp949")  

    #concat dataframe
    temp_data = pd.concat([temp_2020, temp_2021, temp_2022])

    #remove 지점(232), 지점명(천안)  columns
    temp_data = temp_data.drop(['지점','지점명'],axis=1)

    #check NA
    temp_data.isna().sum()

    #replace NA to 0
    temp_data = temp_data.fillna(0)


    variables = ["일시", "기온", "풍속", 
                 "습도", "해면기압"]

    # Define Hyperparameter
    seq_length = 10
    predict_length = 1
    learning_rate = 0.0005
    iterations = 2000
    data_dim = 4
    hidden_dim = 4
    output_dim = 1

    
    time = temp_data[variables[0]]
    temp = temp_data[variables[1]]   
    windV = temp_data[variables[2]]  
    huminity = temp_data[variables[3]]
    pressure = temp_data[variables[4]]
    

    Mintemp, Maxtemp = FindMinMax(temp)

    temp = MinMaxScaler(temp)
    windV = MinMaxScaler(windV)
    huminity = MinMaxScaler(huminity)
    pressure = MinMaxScaler(pressure)
    
    
    x = np.array([temp, windV, 
                  huminity, pressure])
    x = x.transpose()
    y = np.array(temp)
    
    testY, test_predict = Model(x, y,  seq_length, iterations)
    _draw(MinMaxReturn(testY, Mintemp, Maxtemp), 
          MinMaxReturn(test_predict, Mintemp, Maxtemp))






