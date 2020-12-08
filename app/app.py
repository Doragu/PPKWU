from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form

        searchedValue = data.get("searched")
        request_URI = f"https://panoramafirm.pl/szukaj?k={searchedValue}&l="

        print(requests.get(request_URI).text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)