import numpy as np
from rpal.utils.devices import ForceSensor
from rpal.utils.data_utils import Hz


if __name__ == "__main__":

    # rs_cap = RealsenseCapture()
    fs = ForceSensor()

    hz = Hz(print_hz=True)

    while True:
        # pcd = rs_cap.read()
        Fxyz = fs.read()
        if Fxyz is not None:
            Frms = np.sqrt(np.sum(Fxyz**2))
            print(Fxyz)
            hz.clock()
