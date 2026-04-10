from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    user_input = request.args.get("input")
    eval(user_input)  # ❌ Intentional vulnerability
    return "Hello GH-100 Admin Demo 🚀"
