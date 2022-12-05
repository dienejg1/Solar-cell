import pyvisa

rm =  pyvisa.ResourceManager("@py")
ports = rm.list_resources()

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

    def __init__(self, port):
        self.r0 = 1000
        self.r1 = 4.7
        self.r2 = 1000000
        self.r3 = 2000000

        self.port = port
        self.device = rm.open_resource(self.port, read_termination="\r\n", write_termination="\n")

    def get_u1(self):
        u1 = float(self.device.query(f'OUT:CH1?'))

        return u1

    def get_u2(self):
        u2 = float(self.device.query(f'OUT:CH2?'))

        return u2
    
    def set_u0(self, U):
        self.device.query(f'OUT:CH0 {U}')

    def get_u1_volt(self):
        u1_adc = float(self.device.query(f'OUT:CH1?'))
        u1 = u1_adc*(3.3/1023)

        return u1

    def get_u2_volt(self):
        u2_adc = float(self.device.query(f'OUT:CH2?'))
        u2 = u2_adc*(3.3/1023)

        return u2




    

    
    


