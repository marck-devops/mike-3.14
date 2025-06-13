from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This DevOps journey is amazing and I'm having fun learning this with Adnan Fakhar. We just finished learning Terraforms and it blew my mind; it was really fun. (AWS)"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)