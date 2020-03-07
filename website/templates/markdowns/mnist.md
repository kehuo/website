

# Handwritten Digit Recognition

This is a classification project trained on [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. You can try it [here]({{ url_for('ml_api.demo') }}).

## MNIST Dataset[^mnist]

[^mnist]: http://yann.lecun.com/exdb/mnist/

MNIST is a dataset of handwritten digits, including 55,000 training samples, 5,000 validation samples, and 10,000 test samples. Each sample has a labeled gray value 28*28 pixel handwritten digit image, as examples shown below.

<center><img
        style="border-radius: 0.3125em;    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);"
        src="{{ url_for('static',filename='images/MnistExamples.png') }}" width=594 height=361> <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;    display: inline-block;    color: #999;    padding: 2px;">
        Sample images from MNIST test dataset[^mnist_sample]
    </div>
</center>

[^mnist_sample]: Image By Josef Steppan - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=64810040

## LeNet-5[^lenet]

[^lenet]: http://yann.lecun.com/exdb/lenet/

Yann LeCun, Leon Bottou, Yosuha Bengio and Patrick Haffner proposed a neural network architecture for handwritten and machine-printed character recognition in 1990's which they called LeNet-5. Though the architecture is straightforward and simple to understand, it's an important milestone for Convolutional Neural Network (CNN) and Image Classification. Before it was invented, character recognition had been done mostly by using feature engineering by hand, followed by a machine learning model to learn to classify hand engineered features. LeNet made hand engineering features redundant, because the network learns the best internal representation from raw images automatically.

