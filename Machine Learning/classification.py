import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# classification models
#
# 1: Perceptron
# 2: Logistic Regression
# 3: Support Vector Machines
# 4: k-Neighbors(k=1)
# 5: k-Neighbors(k=6)
# 6: Gaussian Naive-Bayes

TRAINING_SET_SIZE = 0.5

classification_models = [Perceptron(), LogisticRegression(solver='liblinear'), svm.SVC(), KNeighborsClassifier(n_neighbors=1), KNeighborsClassifier(n_neighbors=6), GaussianNB()]
models = ["Perceptron", "Logistic Regression", "Support Vector Machines", "k-Neighbors(1)", "k-Neighbors(6)", "Gaussian Naive-Bayes"]
    
# read data in from file: 13 columns of input data, and 1 label

with open("heart disease.csv") as input_data:
    reader = csv.reader(input_data)
    next(reader)

    data = []
    
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:13]],
            "label": row[13]
        })
     
# run models   
for index in range(len(classification_models)):
    # separate input data into training and testing sets: 40 to 60% for training
    
    train_data_size = int(TRAINING_SET_SIZE * len(data))
    
    # mix input data randomly
    
    random.shuffle(data)
    
    # testing and training data sets
    
    testing = data[:train_data_size]
    training = data[train_data_size:]
    
    # train model using the training set
    
    x_training = [row["evidence"] for row in training]
    y_training = [row["label"] for row in training]
    
    model = classification_models[index]
    model.fit(x_training, y_training)
    
    # make predicitions using the testing set
    
    x_testing = [row["evidence"] for row in testing]
    y_testing = [row["label"] for row in testing]
    
    predictions = model.predict(x_testing)
    
    # evaluate the model performance
    
    correct_predictions = (y_testing == predictions).sum()
    incorrect_predictions = (y_testing != predictions).sum()
    total_predictions = len(predictions)
    
    # prediction performance
    
    print("")
    print(models[index], "\n")
    
    print("Correct  ", correct_predictions)
    print("Incorrect  ", incorrect_predictions)
    print("Accuracy  ", (100 * correct_predictions / total_predictions))
    
    