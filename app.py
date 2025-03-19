from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This DevOps journey is amazing and I'm having fun learning this with Adnan Fakhar (AWS)"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)