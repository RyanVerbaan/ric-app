from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def calculation(init_data):
    vrd_kan = init_data["vrd_kan"]
    vrd_pak = init_data["vrd_pak"]
    bst_kan = init_data["best_kan"]
    bst_pak = init_data["best_pak"]
    aantal_kan = 80 * (vrd_kan + bst_kan)
    aantal_pak = 120 * (vrd_pak + bst_pak)
    gem_verk_kan_za = init_data["gem_ver_kan_za"]
    gem_verk_kan_zo = init_data["gem_ver_kan_zo"]
    gem_verk_pak_za = init_data["gem_ver_pak_za"]
    gem_verk_pak_zo = init_data["gem_ver_pak_zo"]
    Huidige_vrd_kan = int(aantal_kan - gem_verk_kan_za - gem_verk_kan_zo)
    Huidige_vrd_pak = int(aantal_pak - gem_verk_pak_za - gem_verk_pak_zo)
    best_kan = int(4 - (Huidige_vrd_kan/80))
    best_pak = int(2 - (Huidige_vrd_pak/120))

    exit_data = {
        "Huidige_vrd_kan": Huidige_vrd_kan, 
        "Huidige_vrd_pak": Huidige_vrd_pak,
        "best_kan": best_kan,
        "best_pak": best_pak
    }

    return exit_data

def DoNothing():
    pass

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("Home.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        milk_data = {
            "vrd_kan": int(result["vrd_kan"]),
            "vrd_pak": int(result["vrd_pak"]),
            "best_kan": int(result["best_kan"]),
            "best_pak": int(result["best_pak"]),
            "gem_ver_kan_za": int(result["gem_ver_kan_za"]),
            "gem_ver_kan_zo": int(result["gem_ver_kan_zo"]),
            "gem_ver_pak_za": int(result["gem_ver_pak_za"]),
            "gem_ver_pak_zo": int(result["gem_ver_pak_zo"]),
        }
        updated_milk_data = calculation(milk_data)
        return render_template("Result.html",
                                input=milk_data,
                                result=updated_milk_data,
                                )


@app.route("/wonderland", methods=["POST", "GET"])
def wonderland():
    return render_template("Wonderland.html")


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port='8000', debug=True)
    app.run(debug=True)

