import matplotlib.pyplot as plt
import numpy as np
import csv

def main():
    # open and read the dataset
    with open('iris-preprocessed.csv') as csvfile:
        dataset_reader = csv.reader(csvfile)
        labels = []
        features = []
        for row in dataset_reader:
            labels.append([int(row[0])]) # add label
            features.append([float(row[1]), float(row[2])]) # add features

    # convert into a numpy array (not necessary for displaying but might be useful later)
    X = np.array(features)
    y = np.array(labels)

    # determine indicies of examples for both classes    
    zero_idxs = np.nonzero(y == 0)[0]
    one_idxs = np.nonzero(y == 1)[0]

    # display the plot
    plt.plot(X[zero_idxs,0], X[zero_idxs,1], 'g.')
    plt.plot(X[one_idxs,0], X[one_idxs,1], 'm.')
    plt.waitforbuttonpress(0)


if __name__ == "__main__":
    main()