import json
from collections import defaultdict


def create_dict_with_all_stops(response):
    """
    Funkcja wyciąga z responsu wszystkie przystanki i tworzy słownik.
    :param response: wynik zapytania API o listę przystanków.
    :return: słownik ze wszystkimi przystankami, w którym kluczem jest nazwa, a wartością id.
    """
    all_stops_dict = defaultdict(str)
    json_format = json.loads(response)
    json_values = json_format["stops"]
    for x in json_values:
        all_stops_dict[x["name"]] = x["shortName"]

    return all_stops_dict


def create_dict_with_results(response, user_input):
    """
    Funkcja filtruje response zawierający wszystkie przyjazdy na podstawie user_input
    i zwraca słownik z wynikami filtrowania.
    :param response: wynik zapytania API o przyjazdy na przystanek.
    :param user_input: słownik z przystankiem, numerem linii i kierunkiem.
    :return: zwraca słownik zawierający słowniki z poszczególnymi wynikami filtrowania.
    """
    results = defaultdict(dict)
    json_format = json.loads(response)
    json_values = json_format["actual"]
    json_values = filter_results(json_values, user_input)
    index = 1
    for x in json_values:
        results[index] = {"LineNumber": x["patternText"], "Direction": x["direction"], "Time": x["actualRelativeTime"]}
        index += 1

    return results


def filter_results(json_values, user_input):
    """
    Funkcja filtruje przyjazdy na dany przystanek po numerze linii i kierunku, i zwraca liste z wynikami filtrowania.
    :param json_values: lista słowników z wynikami zapytania o przyjazdy tramwajów na przystanek.
    :param user_input: słownik z przystankiem, numerem linii i kierunkiem.
    :return: zwraca listę ze słownikami spełniającymi kryteria.
    """
    list_with_filtered_results = []
    for value in json_values:
        if user_input["LineNumber"]:
            if user_input["LineNumber"] != value["patternText"]:
                continue

        if user_input["Direction"]:
            if user_input["Direction"] != value["direction"]:
                continue

        if value["actualRelativeTime"] > 0:
            list_with_filtered_results.append(value)

    return list_with_filtered_results
