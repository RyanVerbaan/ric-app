from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("Home.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        pak = result['pak']
        return render_template("Result.html", result=result, pak=pak)

@app.route("/wonderland", methods=["POST", "GET"])
def wonderland():
    return render_template("Wonderland.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000', debug=True)
    #app.run(debug=True)

