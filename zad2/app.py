from flask import Flask
import json


app = Flask(__name__)
MIN_LENGTH = 8


def get_parameters_based_on_text(text):
    text_params = {
        "upper": 0,
        "lower": 0,
        "numbers": 0,
        "special": 0,
        "length": len(text)
    }

    for item in text:
        if item.islower():
            text_params["lower"] = text_params["lower"] + 1
        elif item.isupper():
            text_params["upper"] = text_params["upper"] + 1
        elif item.isnumeric():
            text_params["numbers"] = text_params["numbers"] + 1
        elif item.isalnum() == False:
            text_params["special"] = text_params["special"] + 1

    return text_params


def check_if_text_valid(text_params):
    if 0 not in text_params.values() and len(text_params["length"]) >= MIN_LENGTH:
        return True
        
    return False


@app.route('/validate/<text>')
def revert_string(text):
    text_params = get_parameters_based_on_text(text)
    text_params["is_valid"] = check_if_text_valid

    return json.dumps(text_params)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True) 