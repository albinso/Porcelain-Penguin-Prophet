import RPi.GPIO as GPIO
from threading import Thread
import datetime
import time

RECEIVED_SIGNAL = []
RECEIVE_PIN = 22
EMPTY_RATE = datetime.timedelta(minutes=1)
codes = ['1010111011101010101010101', '1010111011101010101010111']

last = 5
def record():
    last = 5
    beginning_time = datetime.datetime.now()
    cumulative_time = 0
    while True:
		signal = GPIO.input(RECEIVE_PIN)
		if signal != last:
			RECEIVED_SIGNAL.append(signal)
			last = signal
		cumulative_time = datetime.datetime.now() - beginning_time
		if cumulative_time > EMPTY_RATE:
			beginning_time = datetime.datetime.now()

def parse():
	pass

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RECEIVE_PIN, GPIO.IN)
	thread = Thread(target=record, name='recorder')
	thread.start()
	time.sleep(10)
	print(RECEIVED_SIGNAL)

if __name__ == '__main__':
	main()

