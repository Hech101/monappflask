from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # On récupère le prénom envoyé par le formulaire
        name = request.form.get("name")
        # Si l'utilisateur a saisi un nom, on affiche la page de salut
        if name:
            return render_template("index.html", name=name, greeted=True)
    # Sinon, on affiche simplement le formulaire
    return render_template("index.html", greeted=False)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=10000)
    
