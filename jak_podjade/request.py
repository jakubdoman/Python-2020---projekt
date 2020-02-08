import requests
from jak_podjade.Json import create_dict_with_all_stops, create_dict_with_results

request_for_stops = "http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"


def load_all_stops():
    request = requests.get(request_for_stops)
    return create_dict_with_all_stops(request.text)


def load_traffic_for_stop(user_input, stop_id):
    request = requests.get("http://www.ttss.krakow.pl/internetservice/services/passageInfo/stopPassages/stop?stop=" + stop_id + "&mode=departure&language=pl")
    return create_dict_with_results(request.text, user_input)
