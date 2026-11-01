from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Xin chao!</h1>
    <h2>Ung dung PaaS - Render</h2>
    <p>Ho va ten: Nguyen Hoang Thien</p>
    <p>Ung dung da duoc trien khai thanh cong len nen tang dam may.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)