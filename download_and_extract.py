import os
import mlflow
import argparse

def download_and_extract(kaggle_url,dataset_name, out_path):
    os.system('cp $HOME/Downloads/kaggle.json $HOME/.kaggle')
    os.system('chmod 600 $HOME/.kaggle/kaggle.json')
    os.system(kaggle_url)
    os.makedirs(out_path, exist_ok = True)
    os.system('unzip '+ dataset_name+'.zip -d '+ out_path)
    os.system('rm '+ dataset_name+'.zip ')

if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kaggle_url", default='kaggle datasets download -d "bhawks/pokemon-generation-one-22k"', type = str, help= "The kaggle competiions dataset download syntax (kaggle cli format)")
    parser.add_argument("--out_path", default="dataset", type = str, help= "The output path in which the downloaded datasets contants will be stored")
    parser.add_argument("--dataset_name", default="pokemon-generation-one-22k", type=str,help="Dataset id in kaggle to download")
    args = parser.parse_args()
    download_and_extract(args.kaggle_url, args.dataset_name, args.out_path)