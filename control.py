# control model definition 

from dataclass import dataclass, field 
import numpy as np 

@dataclass
class Control:
    accel: np.ndarray  # [ax, ay, az] from BNO085
    gyro: np.ndarray   # [wx, wy, wz] from BNO085
    dt: float          # time since last prediction step
