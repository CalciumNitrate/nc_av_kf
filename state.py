# state model definition 

from dataclass import dataclass, field 
import numpy as np 

@dataclass 
class State: 
    # [px, py, pz, vx, vy, vz, qw, qx, qy, qz, bgx, bgy, bgz, bax, bay, baz]
    x: np.ndarray = field(default_factory=lambda: np.zeros(16))

    def __post_init__(self):
        # orientation must start as a valid identity quaternion (qw=1)
        self.x[6] = 1.0

    # access the state array by name 
    @property
    def pos(self): return self.x[0:3]
    @pos.setter
    def pos(self, v): self.x[0:3] = v

    @property
    def vel(self): return self.x[3:6]
    @vel.setter
    def vel(self, v): self.x[3:6] = v

    @property
    def q(self): return self.x[6:10]
    @q.setter
    def q(self, v): self.x[6:10] = v

    @property
    def bg(self): return self.x[10:13] # gyro bias
    @bg.setter
    def bg(self, v): self.x[10:13] = v

    @property
    def ba(self): return self.x[13:16] # accel bias
    @ba.setter
    def ba(self, v): self.x[13:16] = v
