from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_calendar_events(html):
    soup = BeautifulSoup(html, 'html.parser')

    for item in soup.find_all('a'):
        if "class" in item.attrs and "active" in item["class"]:
            print(item)

    
    return []

@app.route('/calendar/<year>/<month>')
def generate_WEEIA_calendar(year, month):
    cal_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//PPKWU/ZAD3//EN\n"

    request_URI = f"http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={year}&miesiac={month}&lang=1"
    
    for event in get_calendar_events(requests.get(request_URI).text):
        pass

    cal_content += "END:VCALENDAR"

    return cal_content

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)  