import os
import numpy as np
import argparse
import warnings
import mlflow
import dvc.api
import numpy as np
import os
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator as generator

from model import CNN
class PokemonDataset:
    def __init__(self,data_path,phase = 'train', shape = (150, 150, 3)):
        self.dataset_path=data_path
        self.train_path=os.path.join(data_path,"train")
        self.test_path=os.path.join(data_path,"validation")
        self.num_classes=len(os.listdir(self.train_path))
        self.phase=phase
        self.shape = shape
        self.train_generator, self.val_generator = self._transform()




    def _transform(self, mode="categorical", batch=126):
        train_data_gen = generator(rescale = 1./255,
            rotation_range=20,
            shear_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')
        train_generator = train_data_gen.flow_from_directory(
            self.train_path,
            target_size=(self.shape[0],self.shape[1]),
            class_mode=mode,
            batch_size=batch)
        val_data_gen = generator(rescale = 1./255)
        val_generator = val_data_gen.flow_from_directory(self.test_path,
                                                   target_size=(self.shape[0],self.shape[1]),
                                                   class_mode = mode,
                                                   batch_size = batch)
        return train_generator, val_generator


class model_classifier:
    def __init__(self, epochs=120, lr=1e-3, batch=32, output_path = "results",dataset: PokemonDataset = PokemonDataset("dataset","train")):
        os.makedirs(output_path,exist_ok=True)
        self.epochs=epochs
        self.lr=lr
        self.batch_size=batch
        self.dataset=dataset
        self.model = CNN.build(self.dataset.shape,dataset.num_classes)
        self.opt = Adam(learning_rate=lr, decay=lr / epochs)
        self.checkpoint = ModelCheckpoint(os.path.join(output_path,"best_model.hdf5"), verbose=1, monitor='val_accuracy', save_best_only=True)

    def train(self, loss="categorical_crossentropy", metrics=["accuracy"]):
        self.model.compile(loss=loss,optimizer=self.opt,metrics=metrics)
        return self.model.fit(self.dataset.train_generator, epochs=self.epochs,validation_data=self.dataset.val_generator,verbose = 1, callbacks=[self.checkpoint])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_classes", default = 5, type = int, help = "The number of classes in the dataset")
    parser.add_argument("--batch_size", default = 16, type = int, help = "The batch size to be used when training")
    parser.add_argument("--epochs", default = 5, type = int , help = "The number of epochs to be used when training")
    parser.add_argument("--lr", default = 0.000001, type = float, help = "The learning rate to start with when training")
    parser.add_argument("--weight_decay", default = 0.01, type = float, help = "The weight decay to use for regularization")
    parser.add_argument("--pre_trained" , default = True, type = bool , help = "The number of epochs to be used when training")
    parser.add_argument("--data_path", type = str, help = "The path of the dataset in the repository")
    parser.add_argument("--model_path", default = "model", type = str, help = "The path to save the model")
    args = parser.parse_args()
    mlflow.tensorflow.autolog()
    m = model_classifier()
    m.train()




