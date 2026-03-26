from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"<h1>Hello from Python!</h1><p>Running live on Kubernetes Pod: {hostname}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)