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
    
    
    
#DENSE LAYER+ REGULARIZATION

class Dense(Layer):
    
    def __init__(self, input_size, output_size, weight_l1=0.0, weight_l2=0.0):
        
        super().__init__()
        self.trainable=True
    
        