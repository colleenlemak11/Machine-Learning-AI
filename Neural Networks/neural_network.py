from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self, total_inputs, training_inputs, training_outputs, total_iterations=5000):
        # input weights are random values in range [-2, 2]
        
        self.__weights = 3 * random.random((total_inputs, 1)) - 1
        self.__training_inputs = training_inputs
        self.__training_outputs = training_outputs
        self.__total_iterations = total_iterations
    
    def __sigmoid(self, x):
        # the sigmoid function normalizes the weights between 0 and 1
        
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        # the derivative of the sigmoid function is a gradient, it indicates the confidence of the current weights
        
        return x * (1 - x)

    @property
    def weights(self):
        return self.__weights

    def train(self):
        # the network is trained by trial and error, adjusting the weights each iteration
        
        for iteration in range(self.__total_iterations):
            
            output = self.predict(self.__training_inputs)
            
            # calculate the error as the difference between the desired output and the predicted output

            error = self.__training_outputs - output

            # adjust the weights: the error is multiplied by the input and by the gradient of the sigmoid function to adjust the weights

            self.__weights = self.__weights + dot(self.__training_inputs.T, error * self.__sigmoid_derivative(output))
        
    def predict(self, inputs):
        # neural network prediction

        return self.__sigmoid(dot(inputs, self.__weights))


if __name__ == "__main__":
    verbose = True
    
    NETWORK_INPUTS    = 4
    MAX_ITERATIONS    = 10000
    TRAINING_SET_SIZE = 0.5

    # input data for training
    
    data = array([[0,0,0,0,0],
                  [0,0,0,1,0],
                  [0,0,1,0,1],
                  [0,0,1,1,1],
                  [0,1,0,0,0],
                  [0,1,0,1,0],
                  [0,1,1,0,1],
                  [0,1,1,1,1],
                  [1,0,0,0,0],
                  [1,0,0,1,0],
                  [1,0,1,0,1],
                  [1,0,1,1,1],
                  [1,1,0,0,0],
                  [1,1,0,1,0],
                  [1,1,1,0,1],
                  [1,1,1,1,1]])

    training_data_size = int(TRAINING_SET_SIZE * len(data))

    # mix input data randomly

    random.shuffle(data)

    # training and testing data sets

    training_data = data[training_data_size:]
    testing_data = data[:training_data_size]

    if verbose:
        print ("training data \n\n", training_data, "\n")
        print ("testing  data \n\n", testing_data, "\n")

    x_training = []
    
    for r in range(0, len(training_data)):
        x_training.append([training_data[r][c] for c in range(0, NETWORK_INPUTS)])

    y_training = []

    for r in range(0, len(training_data)):
        y_training.append([training_data[r][NETWORK_INPUTS]])

    training_inputs = array(x_training)
    training_outputs = array(y_training)   

    x_testing = []

    for r in range(0, len(testing_data)):
        x_testing.append([testing_data[r][c] for c in range(0, NETWORK_INPUTS)])
    
    # training data set as an array

    x_training = array(x_training)
    y_training = array(y_training)   

    # neural network with 4 inputs, training is repeated MAX_ITERATIONS times to adjust weights
    
    nn = NeuralNetwork(NETWORK_INPUTS, x_training, y_training, MAX_ITERATIONS)

    print ("weights before training \n\n", nn.weights, "\n")

    nn.train()

    print ("weights after training \n\n", nn.weights, "\n")

    # testing neural network predictions
    
    print ("testing \n")

    for r in range(0, len(x_testing) // 2):
        print (x_testing[r], "is", nn.predict(array(x_testing[r]))[0])