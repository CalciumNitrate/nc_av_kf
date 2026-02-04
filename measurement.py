# measurement model definition 

from dataclass import dataclass, field 
from enum import Enum, auto
import numpy as np 

class SensorType(Enum):
    GPS = auto()       # [x, y, z]
    BNO_QUAT = auto()  # [qw, qx, qy, qz]

@dataclass
class Measurement:
    sensor_type: SensorType
    z: np.ndarray       
    R: np.ndarray       
    timestamp: float