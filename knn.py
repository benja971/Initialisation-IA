import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    data = pd.read_csv(filename, sep=";")
    return data


def getDist(elem1, elem2):
    s = 0

    for key in elem1:
        s += (elem1[key] - elem2[key])**2

    return s


def knn(train_dict, test_dict, i, k):
    nearest = []

    test_elem = test_dict[i]

    for n, train_elem in train_dict.items():
        d = getDist(test_elem, train_elem)

        if (len(nearest) < k):
            nearest.append((n, d))
        else:


def main():
    train_data = load_data("./data/train.csv")
    test_data = load_data("./data/test.csv")

    train_data.quality -= 1
    test_data.quality -= 1

    train_dict = train_data.to_dict('index')
    test_dict = test_data.to_dict('index')

    knn(train_dict, test_dict, 2, 5)


if __name__ == "__main__":
    main()
