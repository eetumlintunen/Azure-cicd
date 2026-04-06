from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Testataan automaatio! T: Eetu"

if __name__ == "__main__":
    app.run()
