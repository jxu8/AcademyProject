from flask import Flask
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/add/<x>/<y>')


def add_numbers(x, y):
		if x.isdigit() and y.isdigit():
			return "The sum is " + str(int(x) + int(y))
		else:
			return "<h1>Error</h1>"

@app.route('/subtract/<x>/<y>')
def subtract_numbers(x,y):
	if x.isdigit() and y.isdigit():
		return "The difference is " + str(int(x) - int(y))
	else:
		return "<h1>Error</h1>"

@app.route('/multiply/<x>/<y>')
def multiple_numbers(x,y):
	if x.isdigit() and y.isdigit():
		return "The product is " + str(int(x)*int(y))
	else:
		return "<h1>Error</h1>"

@app.route('/divide/<x>/<y>')
def divide_number(x,y):
	if x.isdigit() and y.isdigit():
		return "The differnce is " + str(int(x)/int(y))
	else:
		return "<h1>Error</h1>"

if __name__ == "__main__":
	app.run()