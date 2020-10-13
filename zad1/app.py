from flask import Flask

app = Flask(__name__)

@app.route('/')
def handle_empty_route():
    return "W celu uzyskania tekstu w odwrotnej kolejności wpisz adres URL w formacie /rev/<text> gdzie w miejscu <text> podajesz swój ciąg znaków."

@app.route('/rev')
def handle_incomplete_route():
    return "W celu uzyskania tekstu w odwrotnej kolejności wpisz adres URL w formacie /rev/<text> gdzie w miejscu <text> podajesz swój ciąg znaków."

@app.route('/rev/<text>')
def revert_string(text):
    return text[::-1]

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)