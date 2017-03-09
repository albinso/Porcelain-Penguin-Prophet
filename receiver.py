import RPi.GPIO as GPIO
from threading import Thread
import datetime
import time

RECEIVED_SIGNAL = []
RECEIVE_PIN = 22
EMPTY_RATE = datetime.timedelta(seconds=5)
codes = ['1010111011101010101010101', '1010111011101010101010111']
THRESHOLD = 7
TOP = 20
last = 5
def record():
    last = 5
    beginning_time = datetime.datetime.now()
    cumulative_time = 0
    while True:
		signal = GPIO.input(RECEIVE_PIN)
		RECEIVED_SIGNAL.append(signal)
		cumulative_time = datetime.datetime.now() - beginning_time
		if cumulative_time > EMPTY_RATE:
			beginning_time = datetime.datetime.now()
			break

def parse(code):
	print(code)
	ones = split_into_ones(str(code))
	print(ones)
	out = []
	for group in ones:
		out.append(interpret_ones(ones))
	return out


def split_into_ones(code):
	return code.split(r'0')

def interpret_ones(code):
	if len(code) > THRESHOLD:
		return 0
	return 1

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RECEIVE_PIN, GPIO.IN)
	record()
	print(parse(RECEIVED_SIGNAL))

if __name__ == '__main__':
	main()

