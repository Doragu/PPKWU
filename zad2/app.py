from flask import Flask

app = Flask(__name__)

@app.route('/validate/<text>')
def revert_string(text):
    return text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True) 