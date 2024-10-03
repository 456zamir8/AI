'''AIM: Feed Forward Back propagation Neural Network 
● Implement the Feed Forward Back propagation algorithm to train a neural network 
● Use a given dataset to train the neural network for a specific task'''


import numpy as np 

class NeuralNetwork(): 
    def __init__(self): 
        np.random.seed() 
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1 

    def sigmoid(self, x): 
        return 1 / (1 + np.exp(-x)) 

    def sigmoid_derivative(self, x): 
        return x * (1 - x) 

    def train(self, training_inputs, training_outputs, training_iterations): 
        for iteration in range(training_iterations): 
            output = self.think(training_inputs) 
            error = training_outputs - output 
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output)) 
            self.synaptic_weights += adjustments 

    def think(self, inputs): 
        inputs = inputs.astype(float) 
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights)) 
        return output 

if __name__ == "__main__": 
    # Initializing the neural network
    neural_network = NeuralNetwork() 
    print("Beginning Randomly Generated Weights: ") 
    print(neural_network.synaptic_weights) 
    
    # Training data consisting of 4 examples -- 3 input values and 1 output 
    training_inputs = np.array([[0, 0, 1], 
                                 [1, 1, 1], 
                                 [1, 0, 1], 
                                 [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T 
    
    # Training the network
    neural_network.train(training_inputs, training_outputs, 15000) 
    print("Ending Weights After Training: ") 
    print(neural_network.synaptic_weights) 
    
    user_input_one = int(input("User Input One: ")) 
    user_input_two = int(input("User Input Two: ")) 
    user_input_three = int(input("User Input Three: ")) 
    
    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three) 
    print("New Output data: ") 
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
