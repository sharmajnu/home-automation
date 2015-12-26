import RPi.GPIO as GPIO
import time

from flask import Flask, request, json, Response, send_from_directory

GPIO.setmode(GPIO.BCM)

switchValue = [False, False, False, False]
pinList = [2,3,4,17]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

app = Flask(__name__, static_url_path='/home/pi/code/python/home-automation/home-automation')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  print 'Serving static file'
  print path
  return send_from_directory('', path)


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
    app.run(debug=False, host='0.0.0.0')


