try:
    from machine import I2C
except ImportError:
    raise ImportError("Can't find the micropython machine.I2C class: "
                      "perhaps you don't need this adapter?")


class SMBus(I2C):
    """ Provides an 'SMBus' module for micropython which behaves similarly
        to the linux version.
 
	Use it like you would the machine.I2C class: 
	
	    import usmbus.SMBus 
	
	    device = SMBus(1, pins=('G15','G10'), baudrate=100000)

	    device.read_byte_data(addr, register)
	    ... etc	
	"""


    def read_byte_data(self, addr, register):
        """ Read a single byte from register of device at addr
            Returns a single byte """
        return self.readfrom_mem(addr, register, 1)[0]

    def read_i2c_block_data(self, addr, register, length):
        """ Read a block of length from register of device at addr
            Returns a bytes object filled with whatever was read """
        return self.readfrom_mem(addr, register, length)

    def write_byte_data(self, addr, register, data):
        """ Write a single byte of data to register of device at addr
            Returns None """
        return self.writeto_mem(addr, register, data)

    def write_i2c_block_data(self, addr, register, data):
        """ Write multiple bytes of data to register of device at addr
            Returns None """
        return self.writeto_mem(addr, register, data)
