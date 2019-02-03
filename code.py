import threading

import time

import ctrl

from time import sleep

from flask import Flask, render_template 


direction = "front"

app = Flask(__name__)

@app.route("/")
def hello_world():
    print('Hello')
    print('ce plm')
    return render_template('main.html')

@app.route('/move_front', methods=['POST'])
def move_front(x=None, y=None):
    global direction
    direction = "front"
    sleep(0.1)
    return render_template('main.html')

@app.route('/move_back', methods=['POST'])
def move_back(x=None, y=None):
    global direction
    direction = "back"
    return render_template('main.html')

@app.route('/move_left', methods=['POST'])
def move_left(x=None, y=None):
    global direction
    direction = "left"
    return render_template('main.html')

@app.route('/move_right', methods=['POST'])
def move_right(x=None, y=None):
    global direction
    direction = "right"
    return render_template('main.html')

if __name__ == "__main__":
	ctrl.setup()
	threading.Thread(target=app.run(host= '0.0.0.0')).start()	
	while True:
		if direction == "front":
			ctrl.fd()
		if direction == "back":
			ctrl.bk()
		if direction == "left":
			ctrl.lt()
		if direction == "right":
			ctrl.rt()
    
