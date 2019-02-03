from flask import Flask, render_template 

direction = "front"

app = Flask(__name__)

class WebServer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global direction     #made global here
        app.run()

        
            

class Printer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global direction
        while true:
            f = open('test.txt', 'a')
            f.write(direction)
            f.close()

@app.route('/move_front', methods=['POST'])
def move_front(x=None, y=None):
    direction = "front"
    return render_template('main.html')

@app.route('/move_back', methods=['POST'])
def move_back(x=None, y=None):
    direction = "back"
    return render_template('main.html')

@app.route('/move_left', methods=['POST'])
def move_left(x=None, y=None):
    direction = "left"
    return render_template('main.html')

@app.route('/move_right', methods=['POST'])
def move_right(x=None, y=None):
    direction = "right"
    return render_template('main.html')

@app.route('/foo', methods=['POST'])
def foo(x=None, y=None):
    
    return render_template('main.html')

@app.route('/')
def hello_world():
    print('Hello')
    print('ce plm')
    return render_template('main.html')

            

