import csv
import tensorflow as tf

from sklearn.model_selection import train_test_split

# read input data from csv file: 4 columns of input data, and 1 label (authentic, fake)

with open("items.csv") as input_data:
    reader = csv.reader(input_data)
    next(reader)

    data = []
    
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

# separate data into training and testing sets: 40 to 50% for training, and 60 to 40% for testing

evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]

x_training, x_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

# the NN model with a dense hidden layer with 8 units, using a ReLU activation function
# the output layer has one unit with a Sigmoid activation function

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# model training

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_training, y_training, epochs=20)

# model evaluation

model.evaluate(x_testing, y_testing, verbose=2)