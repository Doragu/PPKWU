from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


class Company:
    def __init__(self, name, mail, address, phone_number, webpage):
        self.name = name
        self.mail = mail
        self.address = address
        self.phone_number = phone_number
        self.webpage = webpage
        self.vcf = self.generate_vcf()
        print(self.vcf + "\n")

    def generate_vcf(self):
        return f"BEGIN:VCARD\nVERSION:4.0\nORG:{self.name}\nEMAIL:{self.mail}\nADR;TYPE=WORK;LABEL=\"{self.address}\"\nURL:{self.webpage}\nEND:VCARD"


def get_values_from_scrapper(html):
    soup = BeautifulSoup(html, 'html.parser')
    companies = []

    for item in soup.find_all('li', class_="company-item"):
        temp_soup = BeautifulSoup(str(item), 'html.parser')
        


        try:

            company = Company(temp_soup.find("a", class_="company-name").get_text().strip(),
                                    temp_soup.find("a", class_="icon-envelope")["data-company-email"],
                                    temp_soup.find("div", class_="address").get_text().strip(),
                                    temp_soup.find("a", class_="icon-telephone")["title"],
                                    temp_soup.find("a", class_="icon-website")["href"])



            companies.append(company)
    
        except:
            pass
    return companies


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form

        searchedValue = data.get("searched")
        request_URI = f"https://panoramafirm.pl/szukaj?k={searchedValue}&l="
        
        get_values_from_scrapper(requests.get(request_URI).text)

    return render_template("index.html", companies = get_values_from_scrapper(requests.get(request_URI).text))


@app.route('/generate')
def generate_vcard():
    return "None"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)