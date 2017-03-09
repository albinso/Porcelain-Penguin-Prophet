import RPi.GPIO as GPIO
from threading import Thread

RECEIVED_SIGNAL = []
RECEIVE_PIN = 22

def record():
	while True:
		RECEIVED_SIGNAL.append(GPIO.input(RECEIVE_PIN))

def main():
	thread = Thread(target=record, name='recorder')
	thread.start()
	time.sleep(10)
	print(RECEIVED_SIGNAL)

if __name__ == '__main__':
	main()

