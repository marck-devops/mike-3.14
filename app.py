from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "The DevOps journey is amazing and I'm having fun learning this with Adnan Fakhar"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)