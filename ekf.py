# contains implementation of EKF 

import numpy as np 
from scipy.integrate import jacobian

# import model definitions 
from state import State
from control import Control 
from measurement import Measurement 

class EKF():
    def __init__(self, initial_state: State, initial_cov: np.ndarray):
        self.state = initial_state 
        self.cov = initial_cov 
        
    def predict(self, u: Control):
        
        pass

    def update(self, z: Measurement):
        pass

    def record(self, timestamp):
        ''' Saves the current state to history '''
        entry = np.concatenate(([timestamp], self.state.x.copy()))
        self.history.append(entry)

    def get_history_as_array(self):
        return np.array(self.history)
        
        