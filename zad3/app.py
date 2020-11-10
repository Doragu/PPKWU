from flask import Flask
import requests

app = Flask(__name__)

@app.route('/calendar')
def generate_calendar():
    f = open("calendar.ics", "w")
    
    content = """BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//PPKWU/ZAD3//EN\nBEGIN:VEVENT\nDTSTART:20201105T170000Z\nDTEND:20201105T180000Z\nSUMMARY:TEST\nEND:VEVENT\nEND:VCALENDAR"""
    
    f.write(content)
    f.close()

    return content

@app.route('/calendar/<year>/<month>')
def generate_WEEIA_calendar(year, month):
    request_URI = f"http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={year}&miesiac={month}&lang=1"

    return requests.get(request_URI).text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)  