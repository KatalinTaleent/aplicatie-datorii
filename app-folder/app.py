from flask import Flask

app = Flask(__name__)

@app.route("/")

def titlu():
    return "Aplicație pentru datorii" 

if __name__ == "main":
    app.run()