from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app= Flask(__name__)

CORS(app)

@app.route("/data/", methods=["GET"])
def setName():
    data = {
        "name": "Oliver",
        "items": [
            "Onions",
            "Garlic",
            "Celery",
            "Balsamic Vinegar",
            "TEST",
            "Hi Ash!",
            "another one"
        ]
    }
    #abort(404)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)