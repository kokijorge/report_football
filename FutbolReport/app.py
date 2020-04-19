from flask import Flask,render_template,request ,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__ ,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/prueba1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#sesion
app.secret_key = 'mysecretkey'
ano ='2017'

@app.route('/')
def index():	
	return redirect('2016')

@app.route('/equipos/<string:id>')
def equipos(id):
	data = db.session.execute(" select * from tfg.staging_equipo where ano = :ano" , {"ano": id})
	equipos = [row for row in data]
	return render_template('equipos.html', equipos = equipos , temporada_seleccionada = id)

@app.route('/<int:id>')
def temporada(id):
	return render_template('base.tpl', temporada_seleccionada = id)

#http://localhost:8000/futbol_report/2016
#http://localhost:8000/futbol_report/estadios/2016
#http://localhost:8000/futbol_report/top/2016
#http://localhost:8000/futbol_report/equipos/2017
#http://localhost:8000/futbol_report/jugadores/barcelona/2017
#http://localhost:8000/futbol_report/entrenadores/2017




if __name__ == '__main__':
	app.run(port=8000,debug= True)