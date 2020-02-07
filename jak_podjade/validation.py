from fuzzywuzzy import fuzz


def validate_input(stop, all_stop_names):
    if stop in all_stop_names:
        return stop
    else:
        list_with_ratio = get_list_with_ratio(stop, all_stop_names)
        index_of_best_candidate = list_with_ratio.index(max(list_with_ratio))

        return get_stop_with_nth_index(all_stop_names, index_of_best_candidate)


def get_list_with_ratio(stop, stops_list):
    result_list = []
    for stop_from_list in stops_list:
        result_list.append(fuzz.ratio(stop, stop_from_list))

    return result_list


def get_stop_with_nth_index(stops, index):
    x = 0
    for stop in stops:
        if x == index:
            return stop
        x += 1
