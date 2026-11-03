import numpy as np

"""

class Layer_Dense:

    def __init__(self):
        pass

    def forward(self):
        pass
        
"""
# think what attributes and function `a layer` in a neural network should have?
# a layer in neural network is a set or group of neurons
# all the neurons in a layer will get the same inputs from the previous layer
# each neuron should have it's own weight for each input fed to it.
# and a bias
# initializing a layer = initializing weights a bias for each neuron of the layer
# and it perform a opeation i.e forward pass meaning 
# forward pass = a(z); where a = activation function and z = X @ W + b
# now define the functions

class Layer_Dense:

    def __init__(self, n_inputs, n_neurons):
        rng = np.random.default_rng(seed=42)
        self.weights = rng.standard_normal(size=(n_inputs, n_neurons)) # shape of the weight matrix is defined in such a way that no tranpose operation needed while performing matrix product between inputs and weights
        self.biases = np.zeros(shape=(1,n_neurons))

    def forward(self, inputs):
        output = inputs @ self.weights + self.biases

