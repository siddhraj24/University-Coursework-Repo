## LeNet-5 CNN Implementation on MNIST Dataset using PyTorch

## Description:
This project involves the implementation of the LeNet-5 Convolutional Neural Network (CNN) using PyTorch on the Modified National Institute of Standards and Technology (MNIST) dataset. The MNIST dataset comprises 60,000 grayscale images of handwritten single numbers ranging from 0 to 9. The goal of the project is to correctly classify the given images into one of ten groups representing integer values ranging from 0 to 9.

## LeNet-5 CNN Architecture:
The LeNet-5 CNN architecture consists of seven layers. Two subsampling layers, three convolutional layers, and two fully connected layers make up the layer composition. The input layer accepts 32x32 images, which are then passed on to the next layer. The LeNet-5 then employs an average pooling or sub-sampling layer with a filter size of 22 and a stride of two. The image size will be decreased to 14x14x6 as a result. Following that is a second convolutional layer with 16 feature maps of size 5×5 and stride of 1. Only 10 of the 16 feature maps in this layer are linked to the previous layer's 6 feature maps. The fourth layer is another average pooling layer with a filter size of 2×2 and a stride of 2. This layer is identical to the second layer (S2) except that it has 16 feature mappings, resulting in a 5x5x16 output. The fifth layer is a fully linked convolutional layer with 120 feature maps of size 1×1. Each of the 120 units is linked to all 400 nodes (5x5x16) in the fourth layer. The sixth layer is a fully linked layer with 84 units, followed by a fully connected output layer with 10 potential values corresponding to the digits 0 to 9.

## Implementation and Results:
The model was trained using PyTorch on 60,000 images. After training, the model predicted 59,678 correct images with a 99.46% accuracy. The model also predicted 9,847 correct images out of 10,000 testing images, achieving 98.47% accuracy in testing data. The dataset was divided into 15 epochs, and the model was trained using a learning rate of 0.001. The code displays the training and validation loss for each epoch.

## References:
The following references were used for the implementation of the LeNet-5 CNN on the MNIST dataset using PyTorch:
- Implementing Yann LeCun's LeNet-5 in PyTorch (https://towardsdatascience.com/implementing-yann-lecuns-lenet-5-in-pytorch-5e05a0911320)
- LeNet with TensorFlow (https://medium.com/analytics-vidhya/lenet-with-tensorflow-a35da0d503df)
- Writing LeNet5 from scratch in Python (https://blog.paperspace.com/writing-lenet5-from-scratch-in-python/)
- How to Develop a Convolutional Neural Network From Scratch for MNIST Handwritten Digit Classification (https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/#:~:text=The%20MNIST%20dataset%20is%20an,digits%20between%200%20and%209/)

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






