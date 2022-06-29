import tca9535
from tca9535 import Pin
from periphery import GPIO
import serial

class ExpansionBoard:
	def __init__(self):
		self.tca9535 = tca9535.TCA9535()
		self.tca9535.set_polarity(0x00, 0x00) 
		self.tca9535.config_ports(0xff, 0xff) #all inputs
		self.tca9535.pin_mode(Pin.P1_3, tca9535.Mode.OUTPUT) #led output

		self.gpio_door = GPIO("/dev/gpiochip0", 1, "out")

		self.gpio_door_ramp = GPIO("/dev/gpiochip0", 2, "out")

		self.gpio_siren = GPIO("/dev/gpiochip0", 3, "out")

		self.gpio_door_bell = GPIO("/dev/gpiochip0", 4, "out")
		
		self.gpio_exander_int = GPIO("/dev/gpiochip0", 5, "in")

		self.ser = serial.Serial('/dev/ttyTHS0')
		self.ser.baudrate = 38400
		self.ser.timeout = 1

	def Serial_Write(self, bytes):
		self.ser.write(bytes)

	def Serial_Read(self):
		return self.ser.read()

	def turn_on_siren_relay(self):
		self.gpio_siren.write(True)

	def turn_off_siren_relay(self):
		self.gpio_siren.write(False)

	def turn_on_door_relay(self):
		self.gpio_door.write(True)

	def turn_off_door_relay(self):
		self.gpio_door.write(False)

	def turn_on_door_ramp_relay(self):
		return self.gpio_door_ramp.write(True)

	def turn_off_door_ramp_relay(self):
		return self.gpio_door_ramp.write(False)

	def turn_on_doorbell_relay(self):
		return self.gpio_door_bell.write(True)

	def turn_off_doorbell_relay(self):
		return self.gpio_door_bell.write(False)

	def expander_int_status(self):
		return self.gpio_exander_int.read()

	def aux_do_status(self): # no connected
		return self.tca9535.read_pin(Pin.P0_1)

	def aux_di_status(self): # no connected
		return self.tca9535.read_pin(Pin.P0_2)

	def door_sensor_nc_status(self):
		return self.tca9535.read_pin(Pin.P0_3)

	def door_sensor_no_status(self):
		return self.tca9535.read_pin(Pin.P0_4)

	def motion1_status(self):
		return self.tca9535.read_pin(Pin.P0_5)

	def motion2_status(self):
		return self.tca9535.read_pin(Pin.P0_6)

	def exit_button_no_status(self):
		return self.tca9535.read_pin(Pin.P0_7)

	def exit_button_nc_status(self):
		return self.tca9535.read_pin(Pin.P1_0)

	def trigger_no_status(self):
		return self.tca9535.read_pin(Pin.P1_1)

	def trigger_nc_status(self):
		return self.tca9535.read_pin(Pin.P1_2)

	def acc_int1_status(self):
		return self.tca9535.read_pin(Pin.P1_4)

	def acc_int2_status(self):
		return self.tca9535.read_pin(Pin.P1_5)

	def turn_on_led_relay(self):
		self.tca9535.write_pin(Pin.P1_3, 1)

	def turn_off_led_relay(self):
		self.tca9535.write_pin(Pin.P1_3, 0)
