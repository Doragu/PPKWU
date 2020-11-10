from flask import Flask

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
    return year

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)  