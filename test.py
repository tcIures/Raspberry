


from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/move_front', methods=['POST'])
def move_front(x=None, y=None):
    f = open('test.txt', 'a')
    f.write("front\n")
    f.close()
    return render_template('main.html')

@app.route('/move_back', methods=['POST'])
def move_back(x=None, y=None):
    f = open('test.txt', 'a')
    f.write("back\n")
    f.close()
    return render_template('main.html')

@app.route('/move_left', methods=['POST'])
def move_left(x=None, y=None):
    f = open('test.txt', 'a')
    f.write("left\n")
    f.close()
    return render_template('main.html')

@app.route('/move_right', methods=['POST'])
def move_right(x=None, y=None):
    f = open('test.txt', 'a')
    f.write("right\n")
    f.close()
    return render_template('main.html')

@app.route('/foo', methods=['POST'])
def foo(x=None, y=None):
    f = open('test.txt', 'a')
    f.write("test")
    f.close()
    return render_template('main.html')

@app.route('/')
def hello_world():
    print('Hello')
    print('ce plm')
    return render_template('main.html')



    


   