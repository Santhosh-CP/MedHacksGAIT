import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.io as sio
import os
from sklearn.neighbors import KNeighborsClassifier

def main():
    print("Hello world")
    df = read_data_individuals()
    df = process_data(df)
    print(df.info())
    print(df.head())
    # read_data_parkinson()
    print("End")


def read_data_individuals(files_needed=51):
    columns = ["Subject-id", "Activity-code", "Timestamp", "x", "y", "z"]
    folder_name = "wisdm-dataset/raw/watch/accel/"
    dataset = np.array([[]])
    # print(dataset.shape)
    # print(dataset)
    file_id = 1600  # file IDs are from 1600 to 1650
    while file_id < (1600 + files_needed):
        filename = folder_name + "data_" + str(file_id) + "_accel_watch.txt"
        if file_id == 1600:
            dataset = pd.read_csv(filename, sep=",")
            dataset.columns = columns
        df = pd.read_csv(filename, sep=',')
        df.columns = columns
        dataset = dataset.append(df, ignore_index=False, verify_integrity=False, sort=None)
        print(dataset.shape)
        file_id += 1

    return dataset


def process_data(df):
    df['z'] = df['z'].map(lambda x: x.strip(';'))
    df = df.astype({"Subject-id": int, "Activity-code": str, "Timestamp": int, "x": float, "y": float, "z": float})
    # We are considering only walking data
    # Walking Data has Activity-code 'A'
    df = df[df["Activity-code"] == "A"]
    return df


def MachineLearning(df):
    knn = KNeighborsClassifier(n_neighbors = 3)
    #x, y =


def read_data_parkinson():
    folder_name = "parkinson_data/dataset"
    file_list = os.listdir(folder_name)

    for file in file_list:
        df = sio.loadmat(folder_name + "/" + file)

    print(df.keys())
    print(df['dataset_9Raffaele'])
    print(df['dataset_9Raffaele'])


if __name__ == '__main__':
    main()
