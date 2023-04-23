import os
import argparse
import random
from shutil import copyfile, rmtree
from tqdm import tqdm

def split_data(source,dest, coef):
    pokemons = os.listdir(source)
    train = os.path.join(dest,"train")
    val = os.path.join(dest,"validation")
    os.makedirs(train, exist_ok=True)
    os.makedirs(val, exist_ok=True)
    for pokemon in tqdm(pokemons):
        # Random sampling
        pokedir = os.path.join(source, pokemon)
        samples = os.listdir(pokedir)
        samples = random.sample(samples, len(samples))

        # train val split
        train_pok = samples[:int(len(samples) * (1 - coef))]
        val_pok = samples[int(len(samples) * (1 - coef)):]

        # copying to training and val directories
        train_directory = os.path.join(train, pokemon)
        test_directory = os.path.join(val, pokemon)
        os.mkdir(train_directory)
        os.mkdir(test_directory)
        for t, v in zip(train_pok, val_pok):
            copyfile(os.path.join(source, pokemon, t), os.path.join(train_directory, t))
            copyfile(os.path.join(source, pokemon, v), os.path.join(test_directory, v))
        rmtree(pokedir)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="dataset/PokemonData/", type=str,
                        help="the path where the downloaded dataset is stored")
    parser.add_argument("--dest_path", default="dataset/split/", type=str,
                        help="the path where the split dataset will be stored")
    parser.add_argument("--coef", default=0.8, type=str, help="split coeficent")
    args = parser.parse_args()
    split_data(args.data_path,args.dest_path, args.coef)
