from flask import Flask

app = Flask(__name__)

@app.route('/calendar')
def generate_calendar():
    return "TEST"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)  