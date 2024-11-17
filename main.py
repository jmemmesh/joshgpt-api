from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_answer():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)