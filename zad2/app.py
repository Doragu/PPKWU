from flask import Flask
import json

app = Flask(__name__)

text_params = {
    "upper": 0,
    "lower": 0,
    "numbers": 0,
    "special": 0
}

@app.route('/validate/<text>')
def revert_string(text):
    for item in text:
        if item.islower():
            text_params["lower"] = text_params["lower"] + 1
        elif item.isupper():
            text_params["upper"] = text_params["upper"] + 1

    return json.dumps(text_params)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True) 