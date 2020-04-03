from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html')

@app.route('/scan')
def scanpage():
	return render_template('scan.html')

@app.route('/fridge')
def foodAvailable():
	return render_template('fridge.html')

@app.route('/notifications')
def notifations():
	return render_template('notifications.html')

@app.route('/consumption')
def history():
	return render_template('consumption.html')

if __name__ == '__main__':
	app.run()