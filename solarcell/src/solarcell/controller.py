import pyvisa

def list_devices_arduino():
    """
    Summary:
        Gives a list of connected devices to the PC.

    retruns:
        the list of devices connected to the PC.

    """

    rm =  pyvisa.ResourceManager("@py")
    ports = rm.list_resources()

    list_devices = ports

    return list_devices

class SolarCellMeasureDevice:
    def __init__(self):
        self.r0 = 1000
        self.r1 = 4.7
        self.r2 = 1000000
        self.r3 = 2000000

    


