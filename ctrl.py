import RPi.GPIO as gpio

def setup():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(27, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)

	gpio.output(17, gpio.LOW)
	gpio.output(27, gpio.LOW)
	gpio.output(22, gpio.LOW)
	gpio.output(23, gpio.LOW)

def stop():
	gpio.output(17, gpio.LOW)
	gpio.output(27, gpio.LOW)
	gpio.output(22, gpio.LOW)
	gpio.output(23, gpio.LOW)

def bk():
	gpio.output(17, gpio.HIGH)
	gpio.output(27, gpio.LOW)
	gpio.output(22, gpio.LOW)
	gpio.output(23, gpio.HIGH)

def fd():
	gpio.output(17, gpio.LOW)
	gpio.output(27, gpio.HIGH)
	gpio.output(22, gpio.HIGH)
	gpio.output(23, gpio.LOW)

def rt():
	gpio.output(17, gpio.HIGH)
	gpio.output(27, gpio.HIGH)
	gpio.output(22, gpio.LOW)
	gpio.output(23, gpio.LOW)

def lt():
	gpio.output(17, gpio.LOW)
	gpio.output(27, gpio.LOW)
	gpio.output(22, gpio.HIGH)
	gpio.output(23, gpio.HIGH)


def kill():
	gpio.cleanup()

setup()
