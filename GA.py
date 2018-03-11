import numpy as np
import matplotlib.python as plt
import random as rd
import csv

def dataset():
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


class Individual:

        def __init__(self, degree):

            self.coefs =np.random.randint(degree, size =(range1,range2))
            self.fitness = -1
            pass

        def __str__(self):

            return 'String ' + str(self.coefs) + ' Fitness ' + str(self.fitness)

in_coefs = np.empty([degree])
degree = 2
range1 = -20
range2 = 20
population = 50
generations = 100
mutrate = = 0.1


def ga():

    individuals = init_individuals(population, degree)

    for generation in xrange(generations):

        print "Generetations: " + str(generation)

        individuals = fitness(individuals)
        individuals = selection(individuals)
        individuals = crossover(individuals)
        individuals = mutation(individuals)

        if #stop limit finish later
            exit(0)
def init_individuals(population, degree):

    return [Individual(degree) for in xrange(population)]


def fitness(individuals):



if __name__ == "__main__":
    main()

