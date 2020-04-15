# 手写数字识别

这是一个基于[MNIST](http://yann.lecun.com/exdb/mnist/)数据集的分类任务模型，你可以在[这里](/zh/ml/demo/mnist/)尝试它的效果。

## MNIST 数据集

MNIST[^mnist]是一个手写体数字数据集，包含 55,000 个训练样本，5,000 个验证样本，及 10,000 个测试样本。每个样本都有一个内容为手写体数字的 28\*28 像素的灰度值图像，以及对应该数字的标签。以下是数据集中的一些样本。

[^mnist]: http://yann.lecun.com/exdb/mnist/

| ![Mnist Examples](../../assets/img/MnistExamples.png)  |
| :----------------------------------------------------: |
| _Sample images from MNIST test dataset_[^mnist_sample] |

[^mnist_sample]: Image By Josef Steppan - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=64810040

## LeNet-5

Yann LeCun, Leon Bottou, Yosuha Bengio and Patrick Haffner proposed a neural network architecture for handwritten and machine-printed character recognition in 1990's which they called LeNet-5[^lenet]. Though the architecture is straightforward and simple to understand, it's an important milestone for Convolutional Neural Network (CNN) and Image Classification. Before it was invented, character recognition had been done mostly by using feature engineering by hand, followed by a machine learning model to learn to classify hand engineered features. LeNet made hand engineering features redundant, because the network learns the best internal representation from raw images automatically.

[^lenet]: http://yann.lecun.com/exdb/lenet/
