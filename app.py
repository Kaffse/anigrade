from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
	return render_template("index.jade")

@app.route('/dragndrop')
def dragndrop():
	return render_template("dragndrop.jade")

if __name__ == "__main__":
	app.debug = True
	app.run()
