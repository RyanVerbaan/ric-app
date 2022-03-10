from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("index.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port='5000', debug=True)
    app.run(debug=True)