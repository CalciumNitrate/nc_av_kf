# control model definition 

from dataclass import dataclass, field 
import numpy as np 

@dataclass
class Control:
    accel: np.ndarray  # Raw [ax, ay, az] from BNO085
    gyro: np.ndarray   # Raw [wx, wy, wz] from BNO085
    dt: float          # Time since last prediction step
