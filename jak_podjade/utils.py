from jak_podjade.constant import DIRECTION_MAX_LENGTH, LINE_NUMBER_MAX_LENGTH, INDEX_MAX_LENGTH


def print_menu():
    """
    Funkcja wypisuje na wyjście działania jakie może podjąć użytkownik.
    """
    print('1. Search tram connection')
    print('0. Exit')


def printing_results(dict_with_results):
    """
    Funkcja wypisuje wyniki wyszukiwania przyjazdów.
    :param dict_with_results: słownik zawierający wyniki wyszukiwania pojazdów.
    """
    print("\nSchedule:")
    print(section_to_print("Index", INDEX_MAX_LENGTH) +
          section_to_print("Line Nr", LINE_NUMBER_MAX_LENGTH) +
          section_to_print("Direction", DIRECTION_MAX_LENGTH) +
          str("Time"))

    if dict_with_results:
        for index, tram in dict_with_results.items():
            print(section_to_print(str(index), INDEX_MAX_LENGTH) +
                  section_to_print(tram["LineNumber"], LINE_NUMBER_MAX_LENGTH) +
                  section_to_print(tram["Direction"], DIRECTION_MAX_LENGTH) +
                  get_time(tram["Time"]))
    else:
        print("RESULTS NOT FOUND!")
    print("")


def section_to_print(value_to_print, const):
    """
    Funkcja przygotowuje do wypisania sekcje składającą się z wartości i spacji.
    :param value_to_print: wartość do wypisania, np. nazwa przystanku, numer linii.
    :param const: stałą zawierająca informacje o ilość miejsc przeznaczonych dla danej sekcji,
    np. sekcji przystaanku lub numeru linii.
    :return: zwraca wartość (np. przystanek lub numer linii) z odpowiednią ilością spacji.
    """
    return value_to_print + ' ' * (const - len(value_to_print))


def get_time(time):
    """
    Funkcja przetwarza podaną ilość sekund na odpowiedni format.
    :param time: liczba sekund do przyjazdu tramwaju.
    :return: Zwraca ilość minut i sekund do pryjazdu tramwaju.
    """
    minutes = time // 60
    seconds = time - minutes * 60
    return str(minutes) + 'min ' + str(seconds) + 's'


def _get_input_from_user():
    """
    Funkcja pobiera z wejścia przystanek, numer linii i kierunek i je zwraca.
    :return: słownik z pobranymi wartościami.
    """
    stop = input('Insert stop name: ')
    route_number = input('Insert line number (optional): ')
    direction = input('Insert direction (optional): ')
    return {"Stop": stop, "LineNumber": str(route_number), "Direction": direction}


def handle_user_input(state, chosen_option):
    """
    W zależności od inputu funkcja zmienia stan, bądź wywołuje wczytywanie wyszukiwanych wartości.
    :param state: obiekt klasy State.
    :param chosen_option: wybór użytkownika mający wartość 0 lub 1.
    :return: gdy chosen_option = 1 zwraca słownik z wczytanymi danymi.
    """
    if chosen_option == '0':
        state.change_state()
    else:
        return _get_input_from_user()
