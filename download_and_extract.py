import os
import argparse

def download_and_extract(kaggle_url : str, out_path):
    os.system("cp $HOME/Downloads/kaggle.json $HOME/.kaggle/kaggle.json")
    os.system('chmod 600 $HOME/.kaggle/kaggle.json')
    os.system("kaggle competitions download -c " + kaggle_url)
    os.makedirs(out_path, exist_ok = True)
    os.system('unzip ' + kaggle_url.split("/")[-1] + '.zip -d '+ out_path)
    os.system('rm '+kaggle_url.split("/")[-1]+'.zip')

if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kaggle_url", default="bhawks/pokemon-generation-one-22k", type = str, help= "The kaggle competiions dataset download syntax (kaggle cli format)")
    parser.add_argument("--out_path", default="dataset", type = str, help= "The output path in which the downloaded datasets contants will be stored")
    args = parser.parse_args()
    download_and_extract(args.kaggle_url, args.out_path)