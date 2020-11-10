from flask import Flask

app = Flask(__name__)


@app.route('/calendar')
def generate_calendar():
    f = open("calendar.ics", "w")
    
    content = """BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//PPKWU//KCH//EN\nBEGIN:VTODO\nDTSTAMP:19980130T134500Z\nSEQUENCE:2\nDUE:19980415T235959\nSTATUS:NEEDS-ACTION\nSUMMARY:Submit Income Taxes\nEND:VTODO\nEND:VCALENDAR"""
    
    f.write(content)
    f.close()

    return content

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)  