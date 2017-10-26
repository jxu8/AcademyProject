from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return "Hello World!"

@app.route('/hello')
def hello():
		return "HI ACADEMY"

@app.route('/hello/example')
def hello_example():
	return"<h1>Example</h1>"

@app.route('/echo/<message>')
def echo(message):
	return "This is a dynamic message: " + message

@app.route('/me')
@app.route('/me/<name>')
def render_me(name=None):
	group_list = ["James", "Jason", "Alex", "Sungbin"]
	my_group = {'James': 68, "Jason": 70, "Alex":75, "Sungbin": 70}
	return render_template("me.html", name=name, names=group_list)

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == "__main__":
	app.run()
