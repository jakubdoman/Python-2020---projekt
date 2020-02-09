from fuzzywuzzy import fuzz


def validate_input(stop, all_stop_names):
    """
    Funkcja sprawdza czy przystanek wystepuje na liście nazw,
    jeśli tak to go zwraca, jeśli nie to wyszukuje najbardziej podobny na liście i go zwraca.
    :param stop: przystanek, który będzie sprawdzany.
    :param all_stop_names: lista nazw wszystkich przystanków.
    :return: zweryfikowany przystanek.
    """
    if stop in all_stop_names:
        return stop
    else:
        list_with_ratio = get_list_with_ratio(stop, all_stop_names)
        index_of_best_candidate = list_with_ratio.index(max(list_with_ratio))

        return get_stop_with_nth_index(all_stop_names, index_of_best_candidate)


def get_list_with_ratio(stop, stops_list):
    """
    Funkcja liczy podobieństwo każdego przystanku z listy do podanego przystanku.
    :param stop: przystanek, do którego porównujemy przystanki.
    :param stops_list: lista nazw wszystkich przystanków.
    :return: lista zawierająca podobieństwo poszczególnych przystanków do parametru stop.
    """
    result_list = []
    for stop_from_list in stops_list:
        result_list.append(fuzz.ratio(stop, stop_from_list))

    return result_list


def get_stop_with_nth_index(stops, index):
    """
    Funkcja wyszukuje w liście element o podanym indeksie.
    :param stops: lista nazw wszystkich przystanków.
    :param index: numer przystanku na liście.
    :return: przystanek o podanym indeksie w liście.
    """
    x = 0
    for stop in stops:
        if x == index:
            return stop
        x += 1
