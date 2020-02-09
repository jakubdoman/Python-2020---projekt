from jak_podjade.state import State
from jak_podjade.utils import print_menu, handle_user_input, printing_results
from jak_podjade.request import load_traffic_for_stop, load_all_stops
from jak_podjade.constant import TRAM_NUMBERS
from jak_podjade.validation import validate_input

state = State(False)
all_stops = load_all_stops()

"""
Główna pętla aplikacji zarządzająca jej wykonaniem.
Odpowiada za wywołanie najważniejszych funkcji.
"""
while not state.should_exit:
    print_menu()
    option = input('Choose: ')
    user_input_map = handle_user_input(state, option)
    if user_input_map is not None:
        if not user_input_map["Stop"]:
            print("You have to select stop! Try again!\n")
            continue

        user_input_map["Stop"] = validate_input(user_input_map["Stop"], all_stops.keys())

        if user_input_map["LineNumber"] and user_input_map["LineNumber"] not in TRAM_NUMBERS:
            print("Wrong line number! Try again!\n")
            continue

        if user_input_map["Direction"]:
            user_input_map["Direction"] = validate_input(user_input_map["Direction"], all_stops.keys())

        print(user_input_map)

        result_lines = load_traffic_for_stop(user_input_map, all_stops[user_input_map["Stop"]])
        printing_results(result_lines)
