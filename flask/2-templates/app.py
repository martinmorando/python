'''
	Basic usage of templates.

	- The templates are saved in the folder "templates"
'''
from flask import Flask, render_template # Import render_template

app = Flask(__name__)

@app.route("/")
def index():
	# Render the index.html template with a variable for the page title
	return render_template("index.html", page_title="Home")

@app.route("/user/<int:user_id>")
def user(user_id):
	# Render the user.html template with variable for the page title and user ID
	# Variables are separated by a comma (template_variable = python_variable)
	return render_template("user.html", page_title="User", user_id=user_id)

if __name__ == '__main__':
	app.run()