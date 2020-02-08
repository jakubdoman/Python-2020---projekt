import json
from collections import defaultdict


def create_dict_with_all_stops(response):
    all_stops_dict = defaultdict(str)
    json_format = json.loads(response)
    json_values = json_format["stops"]
    for x in json_values:
        all_stops_dict[x["name"]] = x["shortName"]

    return all_stops_dict


def create_dict_with_results(response, user_input):
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
