# Mobilny vCard
  
  Aplikacja służy do wyszukiwania firm korzystając z API strony [https://panoramafirm.pl/](https://panoramafirm.pl/) oraz do generowania plików .vcf (vCard) na podstawie znalezionych firm.

  Uruchamianie aplikacji następuje po wpisaniu `python app.py` po wcześniejszym pobraniu wszystkich dodatkowych bibliotek z pliku requirements.txt.

  Aplikacja aktualnie po uruchomieniu serwowana jest lokalnie na adresie `http://127.0.0.1:8888/`, tak więc przykładowo używamy jej:
  `http://127.0.0.1:8888/<endpoint>`

  Gdzie w miejscu `<endpoint>` podajemy jeden z podanych niżej endpointów.

## Endpointy

* `GET /`

  Generuje stronę HTML na której znajuje się pojedyńczy formularz służący do wyszukiwania firm. Po wpisaniu wyszukiwanej wartości wypisana zostaje lista znalezionych firm oraz obok każdej z nich link do wygenerowania pliku .vcf.
  
  #### Przykłady użycia:
  - Link:
  `http://localhost:8888/`
  
  Generuje stronę o [wyglądzie](https://doragu.github.io/PPKWU/example.PNG) i [zawartości](https://raw.githubusercontent.com/Doragu/PPKWU/ZADANIE4/app/index.html).

* `POST /search`

  Służy do obsługi formularza na stronie, nie zalecany do użytku manualnego. W celu użycia poprzez api wymagane jest podanie pola "searched" w Form Data wraz z wyszukiwaną wartością. Generuje stronę ze znalezionymi firmami. Wyszukiwane są tylko te firmy znajdujące się na pierwszej stronie wyszukiwarki na ich stronie.
  
  vCard uzupełniony jest o pola: nazwa firmy, adres email, adres firmy, numer telefonu, strona www firmy. Jeśli któryś z tych elementów nie jest uzupełniony na stronie panoramafirm.pl, firma ta nie zostanie wyświetlona.
  
  #### Przykład użycia:
  - Link:
  `http://localhost:8888/search`
  
  Po wpisaniu w polu formualrza "fryzjerzy" generuje taką [stronę](https://doragu.github.io/PPKWU/index.html).
  
* `GET /generate/<nazwa firmy>`

  Wysyła plik .vcf dla firmy podanej w polu `<nazwa firmy>` wg nazwy podanej na stronie panoramafirm.pl. Dla działania tego endpointu wymagane jest wcześniejsze znalezienie podanej firmy poprzez podany powyżej endpoint `POST /search`, gdyż to po jego wywołaniu generowane są gotowe pliki.
  
  vCard uzupełniony jest o pola: nazwa firmy, adres email, adres firmy, numer telefonu, strona www firmy. Jeśli któryś z tych elementów nie jest uzupełniony na stronie panoramafirm.pl, vCard dla tej firmy nie zostanie wygenerowany.
  
  #### Przykład użycia:
  - Link:
  `http://localhost:8888/generate/Akademia Piękna Sylwia Wójcik`
  
  Wyśle [plik](http://doragu.github.io/PPKWU/generated_files/AkademiaPi%C4%99knaSylwiaW%C3%B3jcik.vcf) o zawartości:
  ```
  BEGIN:VCARD
  VERSION:4.0
  ORG:Akademia Piękna Sylwia Wójcik
  TEL;TYPE=work;VALUE=uri:tel:+48 516106264
  EMAIL:sylwia.wojcik21@gmail.com
  ADR;TYPE=WORK;LABEL="ul. Moniuszki 16, 05-200 Wołomin"
  URL:https://www.fryzjer-kobylka.pl/
  END:VCARD
  ```
