import numpy as np
import pandas as pd


def main():
    print("Hello world")
    df = read_data(10)
    df = process_data(df)
    print(df.info())
    print(df.head())


def read_data(files_needed=51):
    columns = ["Subject-id", "Activity code", "Timestamp", "x", "y", "z"]
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
        # print(dataset.shape)
        file_id += 1

    return dataset


def process_data(df):
    df['z'] = df['z'].map(lambda x: x.strip(';'))
    df = df.astype({"Subject-id": int, "Activity code": str, "Timestamp": int, "x": float, "y": float, "z": float})
    # We are considering only walking data
    df = df.drop
    return df


if __name__ == '__main__':
    main()
