from flask import Flask

app = Flask(__name__)

@app.route("/percorso/")
def hello_world():
    return "<p>Hello, World!</p>"
    

@app.route("/modello/")
def modello_ml():
    return "<p>Ecco il modello servito !</p>"



@app.route("/modello/classificazione")
def modello_ml_cl():
    return "<p>Ecco il modello di classificazione servito !</p>"

@app.route("/modello/regressione")
def modello_ml_rg():
    return "<p>Ecco il modello di regressione servito !</p>"


if __name__ == "__main__":
    app.run()    