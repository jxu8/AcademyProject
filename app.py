from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
@app.route('/<name>')
def index(name=None):
    	group_list = ['James', 'Jason', 'Alex', 'Sungbin']
    	my_group = {'James': 68, "Jason": 70, "Alex":75, "Sungbin": 70}
	return render_template("index.html", name=name, group=my_group)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/hello')
def hello():
		return "HI ACADEMY"

@app.route('/hello/example')
def hello_example():
	return"<h1>Example</h1>"

@app.route('/echo/<message>')
def echo(message):
	return "This is a dynamic message: " + message

if __name__ == "__main__":
	app.run()
