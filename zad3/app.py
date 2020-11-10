from flask import Flask

app = Flask(__name__)



@app.route('/calendar')
def generate_calendar():
    return """BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//PPKWU//KCH//EN
    BEGIN:VTODO
    DTSTAMP:19980130T134500Z
    SEQUENCE:2
    DUE:19980415T235959
    STATUS:NEEDS-ACTION
    SUMMARY:Submit Income Taxes
    END:VTODO
    END:VCALENDAR"""

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)  