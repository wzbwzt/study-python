import numpy as np
import matplotlib.pyplot as plt

# 激活函数-阶跃函数


def jump(x):
    return np.array(x > 0, dtype=int)


# 激活函数-sigmoid 函数
def sigmoid(x):
    return 1/(1+np.exp(-x))


# 激活函数-ReLU(Rectified Linear Unit)(simple example)
def relu(x):
    return np.maximum(0, x)


# 机器学习的问题大致可以分为两个问题：分类问题，回归问题
# 激活函数(输出层)-softmax函数-多元分类问题
# 激活函数(神经网络中的隐秘层)-sigmoid函数-二元分类问题
# 激活函数(输出层)-恒等函数-回归问题


def softmax(x):
    # fix 数值溢出的问题
    x_max = np.max(x)
    fix_x = x-x_max
    ex = np.exp(fix_x)
    sum = np.sum(ex)
    return ex/sum


# 损失函数(loss function)-均方误差(mean_squared_error)
def mean_squared_error(y, t):
    """
    y:神经网络的输出
    t:监督数据(one_hot 表示)
    """
    return 0.5 * np.sum((y-t)**2)


# 损失函数(loss function)-交叉熵误差(cross entropy error)
def cross_entropy_error(y, t):
    delta = 1e-7  # 防止y[i]=0
    return -np.sum(t*np.log(y+delta))


# mini-batch 版的交叉熵误差
def cross_entropy_error(y, t, one_hot=True):
    """
    y:神经网络的输出
    t:监督数据
    one_hot: t是否是one_hot表示
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    if one_hot:
        return -np.sum(t*np.log(y+1e-7))/batch_size
    else:
        return -np.sum(np.log(y[np.arange(batch_size), t]+1e-7))/batch_size


# 数值微分（numerical differentiation）:通过数值方式近似求解函数的导数的过程
def numerical_diff(f, x):
    """
    f:执行函数
    x:f的参数
    """
    return (f(x + 1e-4)-f(x-1e-4))/2*(1e-4)


# 梯度(gradient):由函数全部变量的偏导数汇总而成的向量称为梯度
def _numerical_gradient_no_batch(f, x):
    grad = np.zeros_like(x)
    h = 1e-4
    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp+h
        fxh1 = f(x)

        x[i] = tmp-h
        fxh2 = f(x)

        grad[i] = (fxh1-fxh2)/(2*h)
        x[i] = tmp
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad


# 梯度下降法
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []
    for i in range(step_num):
        x_history.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr*grad
    return x, np.array(x_history)
