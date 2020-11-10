# Mobilny Kalendarz WEEIA

  Aplikacja aktualnie po uruchomieniu serwowana jest lokalnie na adresie `http://127.0.0.1:8888/`, tak więc przykładowo używamy jej:
  `http://127.0.0.1:8888/<endpoint>`

  Gdzie w miejscu `<endpoint>` podajemy jeden z podanych niżej endpointów.

## Endpointy

* `GET /calendar/<year>/<month>`

  Tworzy plik kalendarza o formacie .ics w miejscu uruchomienia aplikacji oraz zwraca treść tego pliku na miesiąc podany w polu `<month>` i rok podany w polu `<year>` wzorowany na kalendarzu ze strony [http://www.weeia.p.lodz.pl/](http://www.weeia.p.lodz.pl/).

  #### Odpowiedź:

  NARAZIE PUSTA

  #### Przykłady użycia:
  Link:
  `/calendar/2020/10`

  Zwraca:
  
  NARAZIE PUSTE

  Link:
  `/calendar/2020/03`

  Zwraca:
  
  NARAZIE PUSTE
