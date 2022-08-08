from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# printing dimensions
print(train_images.ndim)

# showing images
digit = train_images[9]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
