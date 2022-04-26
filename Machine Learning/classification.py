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