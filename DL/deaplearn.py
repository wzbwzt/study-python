# %%
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# %%
# 激活函数-阶跃函数


def jump(x):
    return np.array(x > 0, dtype=int)


x = np.arange(-6, 6, 0.1)
y = jump(x)
plt.plot(x, y)
plt.show()


# %%
# 激活函数-sigmoid 函数
def sigmoid(x):
    return 1/(1+np.exp(-x))


x = np.arange(-6, 6, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.show()


# %%
# 激活函数-ReLU(Rectified Linear Unit)(simple example)
def relu(x):
    return np.maximum(0, x)


x = np.arange(-6, 6, 0.1)
y = relu(x)
plt.plot(x, y)
plt.show()


# %%
# demo-3层神经网络
# A=XW+B
def init_network():
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.3], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])
    return network


def identity_func(x):
    return x


def forwork(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3)+b3
    out = identity_func(a3)
    return out


network = init_network()
x = np.array([1.0, 0.5])
out = forwork(network, x)
print(out)


# %%
# 机器学习的问题大致可以分为两个问题：分类问题，回归问题
# 激活函数(输出层)-softmax函数-多元分类问题
# 激活函数(神经网络中的隐秘层)-sigmoid函数-二元分类问题
# 激活函数(输出层)-恒等函数-回归问题

def softmax(x):
    ex = np.exp(x)
    sum = np.sum(ex)
    return ex/sum

# fix 数值溢出的问题


def softmax(x):
    x_max = np.max(x)
    fix_x = x-x_max
    ex = np.exp(fix_x)
    sum = np.sum(ex)
    return ex/sum
