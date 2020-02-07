from constant import DIRECTION_MAX_LENGTH, LINE_NUMBER_MAX_LENGTH, INDEX_MAX_LENGTH


def print_menu():
    print('1. Search tram connection')
    print('0. Exit')


def printing_results(dict_with_results):
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
    return value_to_print + ' ' * (const - len(value_to_print))


def get_time(time):
    minutes = time // 60
    seconds = time - minutes * 60
    return str(minutes) + 'min ' + str(seconds) + 's'


def _get_input_from_user():
    stop = input('Insert stop name: ')
    route_number = input('Insert line number (optional): ')
    direction = input('Insert direction (optional): ')
    return {"Stop": stop, "LineNumber": str(route_number), "Direction": direction}


def handle_user_input(state, chosen_option):
    if chosen_option == '0':
        state.change_state()
    else:
        return _get_input_from_user()
