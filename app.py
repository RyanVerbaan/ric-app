from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Congratulations"

if __name__ == "__main__":
    app.debug = True
    app.run()