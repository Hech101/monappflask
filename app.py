import os
import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "sandoura_secret"  # Obligatoire pour utiliser session

@app.route("/", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            session["name"] = name
            session["secret"] = random.randint(1, 20)  # Génère le nombre à deviner
            return render_template("game.html", name=name, message="Devine le nombre !")
    return render_template("accueil.html")

@app.route("/jeu", methods=["POST"])
def jeu():
    guess = request.form.get("guess")
    name = session.get("name")
    secret = session.get("secret")

    if guess:
        guess = int(guess)

        if guess == secret:
            message = "Bravo ! 🎉 Tu as trouvé le nombre !"
            return render_template("game.html", name=name, message=message, success=True)

        elif guess < secret:
            message = "Trop petit ! Essaie encore."
        else:
            message = "Trop grand ! Essaie encore."

        return render_template("game.html", name=name, message=message)

    return render_template("game.html", name=name, message="Entre un nombre.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
