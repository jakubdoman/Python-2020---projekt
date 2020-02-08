import requests
from jak_podjade.Json import create_dict_with_all_stops, create_dict_with_results

request_for_stops = "http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"


def load_all_stops():
    """
    Funkcja wysyła zapytanie o nazwy wszystkich przystanków i zwraca słownik z nimi.
    :return: słownik ze wszystkimi przystankami, w którym kluczem jest nazwa, a wartością id.
    """
    request = requests.get(request_for_stops)
    return create_dict_with_all_stops(request.text)


def load_traffic_for_stop(user_input, stop_id):
    """
    Funkcja wysyła zapytanie o przyjazdy na przystanek
    i zwraca słownik z poszukiwanymi przyjazdami.
    :param user_input: słownik z przystankiem, numerem linii i kierunkiem.
    :param stop_id: id przystanku potrzebne do zapytania.
    :return: zwraca słownik zawierający poszukiwane przyjazdy na przystanek.
    """
    request = requests.get("http://www.ttss.krakow.pl/internetservice/services/passageInfo/stopPassages/stop?stop=" + stop_id + "&mode=departure&language=pl")
    return create_dict_with_results(request.text, user_input)
