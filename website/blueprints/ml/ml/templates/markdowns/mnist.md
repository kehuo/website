

# Handwritten Digit Recognition

This is a classification project trained on [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. You can try it [here]({{ url_for('ml_api.mnist_canvas') }}).

## MNIST Dataset

MNIST is a dataset of handwritten digits, including 55,000 training samples, 5,000 validation samples, and 10,000 test samples. Each sample has a labeled gray value 28*28 pixel handwritten digit image, as examples shown below.

<center><img
        style="border-radius: 0.3125em;    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);"
        src="{{ url_for('.static',filename='image/MnistExamples.png') }}" width=594 height=361> <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;    display: inline-block;    color: #999;    padding: 2px;">
        Sample images from MNIST test dataset[^1]
    </div>
</center>

[^1]: Image By Josef Steppan - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=64810040