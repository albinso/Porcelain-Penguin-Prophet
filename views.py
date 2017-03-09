import Flask
from subprocess import call
import json

app = Flask(__name__)

@app.route('/light/on')
def light_on():
	data = {}
	js = json.dumps(data)
	code = '1010111011101010101010101'
	call(['python', 'raspy/RFTransmitter.py', code])
	return Response(js, status=200, mimetype='application/json')

@app.route('/light/off')
def light_off():
	data = {}
	js = json.dumps(data)
	code = '1010111011101010101010111'
	call(['python', 'raspy/RFTransmitter.py', code])
	return Response(js, status=200, mimetype='application/json')

def main():
	if len(sys.argv) > 1:
		# Check if argument 1 enables debug mode.
		app.run(debug=(sys.argv[1] == 'debug'), host='0.0.0.0')
	else:
		app.run(debug=False, host='0.0.0.0')

if __name__ == '__main__':
	main()