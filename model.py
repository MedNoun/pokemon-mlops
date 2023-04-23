from keras.layers import BatchNormalization
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense


class CNN:
    @staticmethod
    def build(inputShape=(150,150,3), classes=151):
        # initialize the model along with the input shape to be
        model = Sequential()
        # "channels last" and the channels dimension itself
        chanDim = -1

        # CONV => RELU => POOL
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(3, 3)))
        model.add(Dropout(0.25))

        # (CONV => RELU) * 2 => POOL
        # model.add(Conv2D(64, (3, 3), padding="same"))
        # model.add(Activation("relu"))
        # model.add(BatchNormalization(axis=chanDim))
        # model.add(Conv2D(64, (3, 3), padding="same"))
        # model.add(Activation("relu"))
        # model.add(BatchNormalization(axis=chanDim))
        # model.add(MaxPooling2D(pool_size=(2, 2)))
        # model.add(Dropout(0.25))

        # # (CONV => RELU) * 2 => POOL
        # model.add(Conv2D(128, (3, 3), padding="same"))
        # model.add(Activation("relu"))
        # model.add(BatchNormalization(axis=chanDim))
        # model.add(Conv2D(128, (3, 3), padding="same"))
        # model.add(Activation("relu"))
        # model.add(BatchNormalization(axis=chanDim))
        # model.add(MaxPooling2D(pool_size=(2, 2)))
        # model.add(Dropout(0.25))

        # first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(256))  # 1024
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.3))  # 0.5

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model