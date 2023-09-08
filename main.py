# pip install flask
# pip install psycopg2
# pip install psycopg2-binary

from flask import Flask, render_template, request
import jinja2
import psycopg2

app = Flask(__name__)


def connect_to_db():
    """Create and return a connection to the database."""
    try:
        conn = psycopg2.connect(
            dbname="new_db",
            user="postgres",
            password="jsystems",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def oblicz_bmi(waga, wzrost):
    try:
        bmi = waga / ((wzrost / 100) ** 2)
        return round(bmi, 2)
    except:
        return -1

@app.route('/')   # GET jest domyslna metoda
def index():
    names = ['Filip', 'Marcin', 'Maciek', 'Krzysiek', 'Piotrek', 'Marcin', 'Andrzej']
    return render_template('index.html', names_list=names)


# @app.route('/details',  methods=['POST'])
# def details():
#     #selected_name = request.form['name']
#     names = ['Filip', 'Marcin', 'Maciek', 'Krzysiek', 'Piotrek', 'Marcin', 'Andrzej']
#     dic ={}
#     for i, el in enumerate(names):
#         dic[el] = i+1
#     return render_template('details.html', details=dic)

@app.route('/details',  methods=['POST'])
def details():
    selected_name = request.form['name']
    names = ['Filip', 'Marcin', 'Maciek', 'Krzysiek', 'Piotrek', 'Marcin', 'Andrzej']
    dic = {}
    for i, el in enumerate(names):
        dic[el] = i+1
    index = dic.get(selected_name, "Name not found")
    return render_template('details.html', details=index)


@app.route('/details2',  methods=['POST'])
def get_data():
    selected_name = request.form['name']
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name=%s", (selected_name,))
    user_details = cursor.fetchone()
    cursor.close()
    conn.close()
    if user_details:
        id, name, wzrost, waga, wiek = user_details
        bmi = oblicz_bmi(waga, wzrost)
    return render_template('details2.html', details=user_details, bmi=bmi)


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        imie = request.form['name']
        # inne dane do pobrania analogicznie
        # reszta kodu
    return render_template('add.html')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app.run(host='127.0.0.1', port=5000)
    #app.run(host='localhost', port=5000)


