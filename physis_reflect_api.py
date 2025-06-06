
from flask import Flask, request, jsonify
from physis_gpt_module import physis_reflect

app = Flask(__name__)

@app.route("/reflect", methods=["POST"])
def reflect():
    data = request.get_json()
    code = data.get("code", "")
    result = physis_reflect(code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
