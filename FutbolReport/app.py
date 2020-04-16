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
def Index():
	return app.send_static_file('index.html')

@app.route('/equipos')
def Jugadores():
	data = db.session.execute(" select * from tfg.staging_equipo where ano = :ano" , {"ano": ano})
	equipos = [row for row in data]
	return render_template('equipos.html', equipos = equipos)

if __name__ == '__main__':
	app.run(port=8000,debug= True)