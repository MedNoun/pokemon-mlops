import os
import argparse
import random
from shutil import copyfile


def split_data(source, train, val, coef):
  pokemons = os.listdir(source)
  for pokemon in pokemons:
    #Random sampling
    samples = os.listdir(source + pokemon)
    samples = random.sample(samples,len(samples))
    
    #train val split
    train_pok = samples[:int(len(samples)*(1-coef))]
    val_pok = samples[int(len(samples)*(1-coef)):]

    #copying to training and val directories
    train_directory = os.path.join(train,pokemon)
    test_directory = os.path.join(val,pokemon)
    os.mkdir(train_directory)
    os.mkdir(test_directory)
    for t, v in zip(train_pok,val_pok):
      copyfile( os.path.join(source,pokemon,t) ,os.path.join(train_directory,t))
      copyfile( os.path.join(source,pokemon,v) ,os.path.join(test_directory,v))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default = "dataset", type = str, help= "the path where the downloaded dataset is stored")
    args = parser.parse_args()
    split_data(args.data_path)
