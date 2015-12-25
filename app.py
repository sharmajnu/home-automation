import RPi.GPIO as GPIO
import time

from flask import Flask, request, json, Response

GPIO.setmode(GPIO.BCM)

switchValue = [False, False, False, False]
pinList = [2,3,4,17]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/light', methods=['GET', 'POST'])
def light():

        if request.method == 'POST':

                buttonNumber = int(request.args.get('button'))
                print 'POST Parameter: '
                print buttonNumber
                global switchValue
                GPIO.output(pinList[buttonNumber],switchValue[buttonNumber])
                switchValue[buttonNumber] = not switchValue[buttonNumber]

        return Response(json.dumps(switchValue),  mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


