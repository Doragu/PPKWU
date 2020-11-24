from flask import Flask, send_file
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

class Event:
    date = 0
    name = ""

def get_calendar_events(html):
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.prettify())
    events = []

    for item in soup.find_all('a'):
        if "class" in item.attrs and "active" in item["class"]:
            temp = Event()
            temp.date = item.get_text()
            events.append(temp)


    i = 0
    for item in soup.find_all('div'):
        if "class" in item.attrs and "InnerBox" in item["class"]:
            events[i].name = item.get_text()
            i += 1

    return events

def save_file(content, month, year):
    filename = f"calendar_{month}_{year}.ics"
    path = f"generated_files/{filename}"

    f = open(path, "w", encoding="utf-8")
    f.write(content)
    f.close()

    return filename, path

@app.route('/calendar/<year>/<month>')
def generate_WEEIA_calendar(year, month):
    cal_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//PPKWU/ZAD3//EN\n"

    request_URI = f"http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={year}&miesiac={month}&lang=1"
    
    for event in get_calendar_events(requests.get(request_URI).text):
        cal_content += "BEGIN:VEVENT\n"
        cal_content += f"DTSTART:{year}{month}{event.date}T000000Z\n"
        cal_content += f"DTEND:{year}{month}{event.date}T235959Z\n"
        cal_content += f"SUMMARY:{event.name}\n"
        cal_content += "END:VEVENT\n"
        
    cal_content += "END:VCALENDAR"

    filename, path = save_file(cal_content, month, year)

    print(filename)
    print(path)
    return send_file(path)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)  