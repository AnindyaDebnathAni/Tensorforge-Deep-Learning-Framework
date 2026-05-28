import numpy as np

#CORE LAYER INTERFACE

class Layer: #Base class for all the layers I am going to use in the network
    def __init__(self):
        
        self.input=None
        self.output=None
        self.trainable=False

    def forward_propagation(self, input_data, training=True):
        
        raise NotImplementedError

    def backward_propagation(self, output_gradient):
        
        raise NotImplementedError