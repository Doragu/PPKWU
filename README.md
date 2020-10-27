# String API

  Aplikacja aktualnie po uruchomieniu serwowana jest lokalnie na adresie `http://127.0.0.1:8888/`, tak więc przykładowo używamy jej:
  `http://127.0.0.1:8888/<endpoint>`

  Gdzie w miejscu `<endpoint>` podajemy jeden z podanych niżej endpointów.

## Endpointy

* `GET /validate/<text>`

  Zwraca informacje o tekście przekazanym w miejscu `<text>`.

  #### Odpowiedź:

  Odpowiedź jest podawana w formacie JSON z poniższymi polami.

  `"upper"`: ilość małych liter w podanym tekście

  `"lower"`: ilość dużych liter w podanym tekście

  `"numbers"`: ilość cyfr w podanym tekście

  `"special"`: ilość znaków specjalnych w podanym tekście

  `"length"`: długość podanego teksu

  `"is_valid"`: informacja `true` albo `false` czy tekst jest prawidłowy

  Tekst jest uznawany za prawidłowy jeśli:
  * posiada co najmniej jeden z każdego rodzaju podanych rodzaju znaków
  * jego długość wynosi 8 lub więcej

  #### Przykłady użycia:
  Link:
  `/validate/1aaB$aaA`

  Zwraca:
  `{
      "upper": 2,
      "lower": 4,
      "numbers": 1,
      "special": 1,
      "length": 8,
      "is_valid": false
  }`

  Link:
  `/bA321@dsad`

  Zwraca:
  `{
      "upper": 1,
      "lower": 5,
      "numbers": 3,
      "special": 1,
      "length": 10,
      "is_valid": true
  }`
