from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/')
def root():
	return render_template('form1.html')

@my_app.route("/response/", methods = ["POST"])
def resp():
	return render_template("response1.html", user = request.form["username"], info = request.method)
	
	
if __name__ == '__main__':
	my_app.debug = True
	my_app.run()