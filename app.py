from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Congratulations"

if __name__ == "__main__":
    #app.run(host="127.0.0.1", port=8080, debug=True)
    app.debug = True
    app.run()