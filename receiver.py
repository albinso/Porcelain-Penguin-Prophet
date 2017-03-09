import RPi.GPIO as GPIO
from threading import Thread
import datetime

RECEIVED_SIGNAL = []
RECEIVE_PIN = 22

codes = ['1010111011101010101010101', '1010111011101010101010111']

last = 5
def record():
    beginning_time = datetime.now()
    cumulative_time = 0
	while True:
		signal = GPIO.input(RECEIVE_PIN)
		if signal != last:
			RECEIVED_SIGNAL.append(signal)
			last = signal
		cumulative_time = datetime.now() - beginning_time
		if cumulative_time > EMPTY_RATE:
			beginning_time = datetime.now()

def parse():
	pass

def main():
	thread = Thread(target=record, name='recorder')
	thread.start()
	time.sleep(10)
	print(RECEIVED_SIGNAL)

if __name__ == '__main__':
	main()

