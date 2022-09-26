from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
	return 'Hola Mundo!'

@app.route('/dojo')
def dojo():
	return "¡Dojo!"

@app.route('/say/<name>')
def hola(name):
	print(name)
	return "¡Hola, " + name + " !"

@app.route('/repeat/<int:num>/<string:palabra>')
def repeat(palabra,num):
	return f"{palabra*num}"

@app.errorhandler(404)
def page_not_found(e):
	return "¡Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":
	app.run(debug=True)