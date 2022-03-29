import pandas as pd
import numpy as np


def load_data(filename):
    data = pd.read_csv(filename, sep=";")
    return data


def split_data(data, ratio):
    np.random.seed(0)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def main():
    data = load_data("./data/whites.csv")
    train_data, test_data = split_data(data, 0.3)

    train_data.to_csv("data/train.csv", sep=";", index=False)
    test_data.to_csv("data/test.csv", sep=";",  index=False)


if __name__ == "__main__":
    main()
