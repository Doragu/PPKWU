# Mobilny Kalendarz WEEIA

  Uruchamianie aplikacji następuje po wpisaniu `python app.py` po wcześniejszym pobraniu wszystkich dodatkowych bibliotek z pliku requirements.txt.

  Aplikacja aktualnie po uruchomieniu serwowana jest lokalnie na adresie `http://127.0.0.1:8888/`, tak więc przykładowo używamy jej:
  `http://127.0.0.1:8888/<endpoint>`

  Gdzie w miejscu `<endpoint>` podajemy jeden z podanych niżej endpointów.

## Endpointy

* `GET /calendar/<year>/<month>`

  Tworzy plik kalendarza w formacie .ics w miejscu uruchomienia aplikacji oraz zwraca ten plik na miesiąc podany w polu `<month>` i rok podany w polu `<year>` wzorowany na kalendarzu ze strony [http://www.weeia.p.lodz.pl/](http://www.weeia.p.lodz.pl/).

  #### Odpowiedź:

  Plik .ics o nazwie `<month>.ics` z zawartością.

  #### Przykłady użycia:
  - Link:
  `/calendar/2020/10`

    Zwraca [plik](https://github.com/Doragu/PPKWU/blob/ZADANIE3/zad3/generated_files/calendar_10_2020.ics) o zawartości:
  ```
  BEGIN:VCALENDAR
  VERSION:2.0
  PRODID:-//PPKWU/ZAD3//EN
  BEGIN:VEVENT
  DTSTART:2020101T000000
  DTEND:2020101T235959
  SUMMARY:Akcja Integracja Online
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:2020108T000000
  DTEND:2020108T235959
  SUMMARY:Wielka Integracja WIP
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:2020109T000000
  DTEND:2020109T235959
  SUMMARY:Wielka Integracja WIP
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20201010T000000
  DTEND:20201010T235959
  SUMMARY:Wielka Integracja WIP
  END:VEVENT
  END:VCALENDAR
  ```

  - Link:
  `/calendar/2020/03`

    Zwraca [plik](https://github.com/Doragu/PPKWU/blob/ZADANIE3/zad3/generated_files/calendar_03_2020.ics) o zawartości:
  ```
  BEGIN:VCALENDAR
  VERSION:2.0
  PRODID:-//PPKWU/ZAD3//EN
  BEGIN:VEVENT
  DTSTART:2020039T000000
  DTEND:2020039T235959
  SUMMARY:First Step to Fields Medal
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200313T000000
  DTEND:20200313T235959
  SUMMARY:FinaÅ konkursu InfoSukces
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200316T000000
  DTEND:20200316T235959
  SUMMARY:Matura próbna Matematyka podstawowa
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200317T000000
  DTEND:20200317T235959
  SUMMARY:Matura próbna Matematyka rozszerzona
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200318T000000
  DTEND:20200318T235959
  SUMMARY:Matura próbna Fizyka rozszerzona
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200319T000000
  DTEND:20200319T235959
  SUMMARY:Matura próbna Chemia rozszerzona
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200323T000000
  DTEND:20200323T235959
  SUMMARY:FinaÅ konkursu FascynujÄca Fizyka - poziom podstawowy
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200325T000000
  DTEND:20200325T235959
  SUMMARY:FinaÅ konkursu FascynujÄca Fizyka - poziom ponadpodstawowy
  END:VEVENT
  BEGIN:VEVENT
  DTSTART:20200327T000000
  DTEND:20200327T235959
  SUMMARY:FinaÅ konkursu PiÄkne doÅwiadczenie, FascynujÄce WyjaÅnienie
  END:VEVENT
  END:VCALENDAR
  ```
