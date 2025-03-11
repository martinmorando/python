'''
	Not ready for development

	1. Install flask:  pip install flask
	2. Run:            python3 1-basics.py
	3. Visit:          http://127.0.0.1:5000/
'''
from flask import Flask # Import flask

app = Flask(__name__) # Initiate instance


'''
Specify route: decorator specifies what URL should trigger the function
below, home(). Always starts with /
'''
@app.route("/")
def home():
    return 'Hello friend, <a href="/profile/3">click here</a>'


# Accepts integer
@app.route("/profile/<int:id>")
def profile(id):  # Remember to pass the variable, it's not magic
	return f'<h1>Profile: {id}</h1><a href="/data/4.3">Click here</a>'


# Accepts float. Seems to fail when passing integers
@app.route("/data/<float:id>")
def data(id):
	return f'<h1>Data: {id}</h1><a href="/report/the-state-impoverishes-us-with-fiat-money">Click here</a>'


# Accepts strings and slashes
@app.route("/report/<path:report_slug>")
def iCanHaveAnyNameBecauseTheDecoratorDoesTheJob(report_slug):
	return f"<h1>Report: {report_slug}</h1>"


# Check the script is being run directly (not imported from another script)
if __name__ == '__main__':
	app.run() # Only for development