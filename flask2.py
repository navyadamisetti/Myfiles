from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    var_1 = "Hello World !"
    var_2 = "Hello Navya !"
    var_3 = "Hello Satya !"
    array = range(0, 100)
    return render_template("index.html", vars=var_1, n = var_2, s = var_3, a = array)


if __name__ == "__main__":
    app.run(debug=True)
