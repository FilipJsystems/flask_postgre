# pip install flask
# pip install psycopg2
# pip install psycopg2-binary

from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route('/')   # GET jest domyslna metoda
def index():
    try:
        print(1/0)
    except:
        print('nie udalo sie podzielic')
    return render_template('index.html')

@app.route('/details')   #, methods=['POST'])
def details():
    names = ['Filip', 'Marcin', 'Maciek', 'Krzysiek', 'Piotrek', 'Marcin', 'Andrzej']
    return render_template('index.html', details=names)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app.run(host='127.0.0.1', port=5000)
    #app.run(host='localhost', port=5000)


