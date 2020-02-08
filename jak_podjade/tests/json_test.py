import unittest
from jak_podjade.Json import filter_results, create_dict_with_all_stops, create_dict_with_results


class JsonTest(unittest.TestCase):
    def test_create_dict_with_all_stops(self):
        # given
        response = '{"stops": [{' \
                   '"category": "tram",' \
                   '"id": "8059230041856278766",' \
                   '"latitude": 180367133,' \
                   '"longitude": 72043450,' \
                   '"name": "Os.Piastów",' \
                   '"shortName": "378"' \
                   '},' \
                   '{' \
                   '"category": "tram",' \
                   '"id": "8059230041856278732",' \
                   '"latitude": 180234831,' \
                   '"longitude": 71825984,' \
                   '"name": "Lubicz",' \
                   '"shortName": "126"' \
                   '}]}'
        expected_result = {'Os.Piastów': '378', 'Lubicz': '126'}

        # when
        result = create_dict_with_all_stops(str(response))

        # then
        self.assertEqual(result, expected_result)

    def test_create_dict_with_results(self):
        # given
        response = '{' \
                   '"actual": [' \
                   '{' \
                   '"actualRelativeTime": -42,' \
                   '"actualTime": "13:07",' \
                   '"direction": "Kopiec Wandy",' \
                   '"mixedTime": "0 %UNIT_MIN%",' \
                   '"passageid": "-1188950301255150542",' \
                   '"patternText": "22",' \
                   '"plannedTime": "13:04",' \
                   '"routeId": "8059228650286874670",' \
                   '"status": "STOPPING",' \
                   '"tripId": "8059232507169185289",' \
                   '"vehicleId": "-1188950296948415004"' \
                   '},' \
                   '{' \
                   '"actualRelativeTime": 258,' \
                   '"direction": "Czerwone Maki P+R",' \
                   '"mixedTime": "13:12",' \
                   '"passageid": "-1188950301255162718",' \
                   '"patternText": "52",' \
                   '"plannedTime": "13:12",' \
                   '"routeId": "8059228650286874694",' \
                   '"status": "PLANNED",' \
                   '"tripId": "8059232507169193476"' \
                   '},' \
                   '{' \
                   '"actualRelativeTime": 438,' \
                   '"actualTime": "13:15",' \
                   '"direction": "Os.Piastów",' \
                   '"mixedTime": "7 %UNIT_MIN%",' \
                   '"passageid": "-1188950301255145288",' \
                   '"patternText": "52",' \
                   '"plannedTime": "13:12",' \
                   '"routeId": "8059228650286874694",' \
                   '"status": "PREDICTED",' \
                   '"tripId": "8059232507168222725",' \
                   '"vehicleId": "-1188950296948414994"' \
                   '}' \
                   ']' \
                   '}'
        user_input = {'Stop': 'Słomiana', 'LineNumber': '52', 'Direction': 'Czerwone Maki P+R'}
        expected_result = {
            1: {'LineNumber': '52', 'Direction': 'Czerwone Maki P+R', 'Time': 258}
        }

        # when
        result = create_dict_with_results(response, user_input)

        # then
        self.assert_(result, expected_result)


if __name__ == '__main__':
    unittest.main()
