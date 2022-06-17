import flask as fl
import datetime as dt

app = fl.Flask(__name__)

def calculation(init_data):
    vrd_kan = init_data["vrd_kan"]
    vrd_pak = init_data["vrd_pak"]
    bst_kan = init_data["best_kan"]
    bst_pak = init_data["best_pak"]
    if(vrd_kan >= 10 and vrd_pak >= 10): #If input NOT in ric
        aantal_kan = 80 *  bst_kan + vrd_kan
        aantal_pak = 160 * bst_pak + vrd_pak

    else: #if input in RIC
        aantal_kan = 80 * (vrd_kan + bst_kan)
        aantal_pak = 160 * (vrd_pak + bst_pak)
    gem_verk_kan_za = init_data["gem_ver_kan_va"]
    gem_verk_kan_zo = init_data["gem_ver_kan_mo"]
    gem_verk_pak_za = init_data["gem_ver_pak_va"]
    gem_verk_pak_zo = init_data["gem_ver_pak_mo"]
    Huidige_vrd_kan = int(aantal_kan - gem_verk_kan_za - gem_verk_kan_zo)
    Huidige_vrd_pak = int(aantal_pak - gem_verk_pak_za - gem_verk_pak_zo)
    best_kan = int(3 - (Huidige_vrd_kan/80))
    best_pak = int(3 - (Huidige_vrd_pak/160))

    exit_data = {
        "Huidige_vrd_kan": Huidige_vrd_kan, 
        "Huidige_vrd_pak": Huidige_vrd_pak,
        "best_kan": best_kan,
        "best_pak": best_pak
    }
    return exit_data

@app.route("/")
def home():
    return fl.render_template("Homepage.html")

@app.route("/help")
def foryou():
    return fl.render_template("Helppage.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if fl.request.method == "POST":
        result = fl.request.form
        milk_data = {
            "vrd_kan": float(result["vrd_kan"]),
            "vrd_pak": float(result["vrd_pak"]),
            "best_kan": int(result["best_kan"]),
            "best_pak": int(result["best_pak"]),
            "gem_ver_kan_va": int(result["gem_ver_kan_va"]),
            "gem_ver_kan_mo": int(result["gem_ver_kan_mo"]),
            "gem_ver_pak_va": int(result["gem_ver_pak_va"]),
            "gem_ver_pak_mo": int(result["gem_ver_pak_mo"]),
        }
        updated_milk_data = calculation(milk_data)
        return fl.render_template("Resultpage.html", input=milk_data, result=updated_milk_data)


@app.route("/wonderland")
def wonderland():
    return fl.render_template("Wonderland.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000', debug=True)