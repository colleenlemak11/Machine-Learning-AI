import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier

# classification models
#
# 1: Perceptron, 
# 2: Support Vector Machines
# 3: k-Neighbors(k=1)

TRAINING_SET_SIZE = 0.4

classification_models = [Perceptron(), svm.SVC(), KNeighborsClassifier(n_neighbors=1)]
models = ["Perceptron", "Support Vector Machines", "k-Neighbors(1)"]

# read input data from csv file: 4 columns of input data, and 1 label (authentic, fake)

with open("items.csv") as input_data:
    reader = csv.reader(input_data)
    next(reader)

    data = []
    
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "authentic" if row[4] == "0" else "fake"
        })

# run models

for index in range(len(classification_models)):
    # separate data into training and testing sets: 40 to 50% for training, and 60 to 40% for testing

    train_data_size = int(TRAINING_SET_SIZE * len(data))

    # mix input data randomly

    random.shuffle(data)

    # testing and training data sets

    testing = data[:train_data_size]
    training = data[train_data_size:]

    # train model using the training set

    x_training = [row["evidence"] for row in training]
    y_training = [row["label"] for row in training]

    # the model
    
    model = classification_models[index]
    model.fit(x_training, y_training)

    # make predictions using the testing set

    x_testing = [row["evidence"] for row in testing]
    y_testing = [row["label"] for row in testing]

    predictions = model.predict(x_testing)

    # evaluate the model performance

    correct_predictions = (y_testing == predictions).sum()
    incorrect_predictions = (y_testing != predictions).sum()
    total_predictions = len(predictions)

    # prediction performance

    print ("")
    print (models[index], "\n")    
    print ("Correct   ", correct_predictions)
    print ("Incorrect ", incorrect_predictions)
    print ("Accuracy  ", (100 * correct_predictions / total_predictions))