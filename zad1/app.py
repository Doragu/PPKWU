from flask import Flask

app = Flask(__name__)

@app.route('/rev')
def revert_string():
    return ""

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)