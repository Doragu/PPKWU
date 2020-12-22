from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


class Company:
    def __init__(self, name, mail, address, phone_number, webpage):
        self.name = name
        self.mail = mail
        self.address = address
        self.phone_number = str(phone_number).replace(" ", "")
        self.webpage = webpage
        self.vcf = self.generate_vcf()
        self.save_vcf_to_file()


    def generate_vcf(self):
        return f"BEGIN:VCARD\nVERSION:4.0\nORG:{self.name}\nTEL;TYPE=work;VALUE=uri:tel:+48 {self.phone_number}\nEMAIL:{self.mail}\nADR;TYPE=WORK;LABEL=\"{self.address}\"\nURL:{self.webpage}\nEND:VCARD"


    def save_vcf_to_file(self):
        stripped_name = self.name.replace(" ", "")
        filename = f"{stripped_name}.vcf"
        path = f"generated_files/{filename}"

        f = open(path, "w", encoding="utf-8")
        f.write(self.vcf)
        f.close()


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


@app.route('/generate/<company_name>')
def generate_vcard(company_name):
    company_name = company_name.replace(" ", "")

    return send_file(f"generated_files/{company_name}.vcf", attachment_filename=f"{company_name}.vcf")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)