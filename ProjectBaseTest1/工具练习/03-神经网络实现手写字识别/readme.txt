
实验环境
python2.7
Xfce终端
Numpy, Sklearn, Scipy 模块（请确认电脑上安装有这些模块，如果没有请在命令行中 sudo pip 安装相应的模块）

什么是神经网络
神经网络由能够互相通信的节点构成，赫布理论解释了人体的神经网络是如何通过改变自身的结构和神经连接的强度来记忆某种模式的。而人工智能中的神经网络与此类似。请看下图，最左一列蓝色节点是输入节点，最右列节点是输出节点，中间节点是隐藏节点。该图结构是分层的，隐藏的部分有时候也会分为多个隐藏层。如果使用的层数非常多就会变成我们平常说的深度学习了。

如何使用神经网络
神经网络属于监督学习，那么多半就三件事，决定模型参数，通过数据集训练学习，训练好后就能到分类工具/识别系统用了。数据集可以分为2部分（训练集，验证集），也可以分为3部分（训练集，验证集，测试集），训练集可以看作平时做的习题集（可反复做），系统通过对比习题集的正确答案和自己的解答来不断学习改良自己。测试集可以看作是高考，同一份试卷只能考一次，测试集一般不会透露答案。那么验证集是什么呢？好比多个学生（类比用不同策略训练出的多个神经网络）要参加一个名额只有两三人的比赛，那么就得给他们一套他们没做过的卷子（验证集）来逐出成绩最好的几个人，有时也使用验证集决定模型参数。在本课程中数据集只划分训练集和验证集。

客户端（ocr.js）
服务器（server.py）
用户接口（ocr.html）
神经网络(ocr.py)
神经网络设计脚本(neural_network_design.py)

用户接口(ocr.html)是一个html页面，用户在canvas上写数字，之后点击选择训练或是预测。客户端(ocr.js)将收集到的手写数字组合成一个数组发送给服务器端(server.py)处理，服务器调用神经网络模块(ocr.py)，它会在初始化时通过已有的数据集训练一个神经网络，神经网络的信息会被保存在文件中，等之后再一次启动时使用。最后，神经网络设计脚本(neural_network_design.py)是用来测试不同隐藏节点数下的性能，决定隐藏节点数用的。



我们使用反向传播算法（Backpropagation）来训练神经网络
http://www.hankcs.com/ml/back-propagation-neural-network.html

第一步：初始化神经网络
一般将所有权值与偏置量置为(-1,1)范围内的随机数，在我们这个例子中，使用(-0.06,0.06)这个范围，输入层到隐藏层的权值存储在矩阵theta1中，偏置量存在input_layer_bias中，隐藏层到输出层则分别存在theta2与hidden_layer_bias中。

创建随机矩阵的代码如下，注意输出的矩阵是以size_out为行，size_in为列。可能你会想为什么不是size_in在左边。你可以这么想，一般都是待处理的输入放在右边，处理操作（矩阵）放在左边。
def _rand_initialize_weights(self, size_in, size_out):
    return [((x * 0.12) - 0.06) for x in np.random.rand(size_out, size_in)]

self.theta1 = self._rand_initialize_weights(400, num_hidden_nodes)
self.theta2 = self._rand_initialize_weights(num_hidden_nodes, 10)
self.input_layer_bias = self._rand_initialize_weights(1,                                                             num_hidden_nodes)
self.hidden_layer_bias = self._rand_initialize_weights(1, 10)


第二步：前向传播
前向传播就是输入数据通过一层一层计算到达输出层得到输出结果，输出层会有10个节点分别代表0~9，哪一个节点的输出值最大就作为我们的预测结果。还记得前面说的激发函数吗？一般用sigmoid函数作为激发函数。

# sigmoid激发函数
def _sigmoid_scalar(self, z):
    return 1 / (1 + math.e ** -z)


第三步：反向传播
第三步是训练的关键，它需要通过计算误差率然后系统根据误差改变网络的权值矩阵和偏置向量。通过训练数据的标签我们得到actual_vals用来和输出层相减得到误差率output_errors，输出层的误差只能用来改进上一层，想要改进上上一层就需要计算上一层的输出误差，公式原理还是请看反向传播神经网络极简入门。
actual_vals = [0] * 10 
actual_vals[data['label']] = 1
output_errors = np.mat(actual_vals).T - np.mat(y2)
hidden_errors = np.multiply(np.dot(np.mat(self.theta2).T, output_errors), 
                            self.sigmoid_prime(sum1))

其中sigmoid_prime的作用就是先sigmoid再求导数。

其中sigmoid_prime的作用就是先sigmoid再求导数。
self.theta1 += self.LEARNING_RATE * np.dot(np.mat(hidden_errors), 
                                           np.mat(data['y0']))
self.theta2 += self.LEARNING_RATE * np.dot(np.mat(output_errors), 
                                           np.mat(y1).T)
self.hidden_layer_bias += self.LEARNING_RATE * output_errors
self.input_layer_bias += self.LEARNING_RATE * hidden_errors

LEARNING_RATE是学习步进，这里我们设置成0.1，步子大虽然学得快，但也容易扭到，步子小得到的结果会更精准。
预测的代码就相当于前向传播：

def predict(self, test):
    y1 = np.dot(np.mat(self.theta1), np.mat(test).T)
    y1 =  y1 + np.mat(self.input_layer_bias) # Add the bias
    y1 = self.sigmoid(y1)

    y2 = np.dot(np.array(self.theta2), y1)
    y2 = np.add(y2, self.hidden_layer_bias) # Add the bias
    y2 = self.sigmoid(y2)

    results = y2.T.tolist()[0]
    return results.index(max(results))



http://aosabook.org/en/500L/optical-character-recognition-ocr.html
https://github.com/aosabook/500lines/tree/master/ocr
http://www.hankcs.com/ml/back-propagation-neural-network.html