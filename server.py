import json, sqlite3
from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
from model import get_gemini_response

app = Flask(__name__)
app.secret_key = "youmakemypistonicky"


@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/chat/gemini", methods=["GET"])
def Geminichat():
    return render_template('gemini.html')


@app.route("/api/v1/get-response/gemini", methods=["POST"])
def get_response_gemini():
    if request.method == "POST":
        requestData = request.get_json(force=True)

        text = requestData["text"]
        response = get_gemini_response(text)
        return jsonify({"response": response})
    else:
        return jsonify({"response": "Invalid request method"})


if __name__ == "__main__":
    app.run(debug=True)
