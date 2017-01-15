from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/navya")
def say_hello_to_navya():
    return "Hello Navya"


@app.route("/<name>/")
def say_hello(name):
    return "Hello %s" % (name)


@app.route("/satya")
def say_hello_to_satya():
    return "<html><center><h1>Satya</h1></center></html>"

# templates , index.html
@app.route("/test/")
def render_template_test():
    return render_template("index.html")


app.run()
