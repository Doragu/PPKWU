from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form

        print(data.get("searched"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)