import numpy as np

#1
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"
data = np.genfromtxt(url)

np.random.shuffle(data)

attr = data[:, :-1]
clas = data[:, -1]

train_size = int(0.8 * len(attr))
attr_train = attr[:train_size, :]
clas_train = clas[:train_size]

attr_test = attr[train_size:, :]
clas_test = clas[train_size:]

#

#2
input_size = attr_train.shape[1]
hidden_size = input_size
output_size = 3
lr = 0.01
epochs = 50

w_input_hidden1 = np.random.randn(input_size, hidden_size) * 0.01
bias1 = np.zeros((1, hidden_size))

w_hidden1_hidden2 = np.random.randn(hidden_size, hidden_size) * 0.01
bias2 = np.zeros((1, hidden_size))

w_hidden2_output = np.random.randn(hidden_size, output_size) * 0.01
bias3 = np.zeros((1, output_size))
#

#3
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

def error(ytrue, yprediction):
    return ytrue - yprediction

#4
def forward(x, w_input_hidden1, bias1, w_hidden1_hidden2, bias2, w_hidden2_output, bias3):
    hidden1_input = np.dot(x, w_input_hidden1) + bias1
    hidden1_output = sigmoid(hidden1_input)

    hidden2_input = np.dot(hidden1_output, w_hidden1_hidden2) + bias2
    hidden2_output = relu(hidden2_input)

    output_input = np.dot(hidden2_output, w_hidden2_output) + bias3
    output_output = softmax(output_input)

    return hidden1_output, hidden2_output, output_output