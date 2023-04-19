from flask import Flask, request, render_template
from flask import jsonify, make_response
from flask_socketio import SocketIO
from main import Estudiante, Lector
from BD_user import buscar_persona

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
socketio = SocketIO(app)

base_datos = Lector()
estudiante1 = Estudiante("Elian",67872)
estudiante2 = Estudiante("Willy",65488)
estudiante3 = Estudiante("Dluz",65147)
estudiante4 = Estudiante("David",60244)
base_datos.addEstudiante(estudiante1)
base_datos.addEstudiante(estudiante2)
base_datos.addEstudiante(estudiante3)
base_datos.addEstudiante(estudiante4)

app.jinja_env.globals.update(zip=zip)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    numero_tarjeta = request.form['numero']
    verf = buscar_persona(numero_tarjeta)
    if verf:
        return f'Bienvenido {verf}'
    else:
        return 'Error'
    
if __name__ == '__main__':
    app.run(debug=True, port=800)

