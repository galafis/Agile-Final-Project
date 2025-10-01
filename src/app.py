from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(message="Hello, Agile World!")

@app.route("/status")
def status():
    return jsonify(status="OK", version="1.0.0")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

