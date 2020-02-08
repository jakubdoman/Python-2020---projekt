import unittest
from jak_podjade.Json import filter_results, create_dict_with_all_stops, create_dict_with_results


class JsonTest(unittest.TestCase):
    json_values = [{'actualRelativeTime': -28, 'actualTime': '19:32', 'direction': 'Bronowice Małe',
                    'mixedTime': '0 %UNIT_MIN%', 'passageid': '-1188950301254937674', 'patternText': '8',
                    'plannedTime': '19:32', 'routeId': '8059228650286875431', 'status': 'PREDICTED',
                    'tripId': '8059232507167657488', 'vehicleId': '-1188950296948414093'},
                   {'actualRelativeTime': 152, 'actualTime': '19:35', 'direction': 'Os.Piastów',
                    'mixedTime': '2 %UNIT_MIN%', 'passageid': '-1188950301254934834', 'patternText': '52',
                    'plannedTime': '19:35', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                    'tripId': '8059232507171085835', 'vehicleId': '-1188950296948413325'},
                   {'actualRelativeTime': 272, 'direction': 'Borek Fałęcki', 'mixedTime': '19:37',
                    'passageid': '-1188950301254949237', 'patternText': '22', 'plannedTime': '19:37',
                    'routeId': '8059228650286874670', 'status': 'PLANNED', 'tripId': '8059232507167682058'},
                   {'actualRelativeTime': 692, 'actualTime': '19:44', 'direction': 'Kopiec Wandy',
                    'mixedTime': '11 %UNIT_MIN%', 'passageid': '-1188950301254930823', 'patternText': '22',
                    'plannedTime': '19:44', 'routeId': '8059228650286874670', 'status': 'PREDICTED',
                    'tripId': '8059232507168206349', 'vehicleId': '-1188950296948400570'},
                   {'actualRelativeTime': 752, 'actualTime': '19:45', 'direction': 'Czerwone Maki P+R',
                    'mixedTime': '12 %UNIT_MIN%', 'passageid': '-1188950301254949688', 'patternText': '52',
                    'plannedTime': '19:42', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                    'tripId': '8059232507170110990', 'vehicleId': '-1188950296948416950'},
                   {'actualRelativeTime': 872, 'actualTime': '19:47', 'direction': 'Borek Fałęcki',
                    'mixedTime': '14 %UNIT_MIN%', 'passageid': '-1188950301254939507', 'patternText': '8',
                    'plannedTime': '19:47', 'routeId': '8059228650286875431', 'status': 'PREDICTED',
                    'tripId': '8059232507169173009', 'vehicleId': '-1188950296948415583'},
                   {'actualRelativeTime': 932, 'actualTime': '19:48', 'direction': 'Krowodrza Górka',
                    'mixedTime': '15 %UNIT_MIN%', 'passageid': '-1188950301254927499', 'patternText': '18',
                    'plannedTime': '19:48', 'routeId': '8059228650286874693', 'status': 'PREDICTED',
                    'tripId': '8059232507168194064', 'vehicleId': '-1188950296948418628'},
                   {'actualRelativeTime': 992, 'actualTime': '19:49', 'direction': 'Czerwone Maki P+R',
                    'mixedTime': '16 %UNIT_MIN%', 'passageid': '-1188950301254937736', 'patternText': '18',
                    'plannedTime': '19:49', 'routeId': '8059228650286874693', 'status': 'PREDICTED',
                    'tripId': '8059232507168656913', 'vehicleId': '-1188950296948414077'},
                   {'actualRelativeTime': 1172, 'actualTime': '19:52', 'direction': 'Bronowice Małe',
                    'mixedTime': '19 %UNIT_MIN%', 'passageid': '-1188950301254926300', 'patternText': '8',
                    'plannedTime': '19:52', 'routeId': '8059228650286875431', 'status': 'PREDICTED',
                    'tripId': '8059232507171040784', 'vehicleId': '-1188950296948415653'},
                   {'actualRelativeTime': 1352, 'actualTime': '19:55', 'direction': 'Os.Piastów',
                    'mixedTime': '22 %UNIT_MIN%', 'passageid': '-1188950301254923551', 'patternText': '52',
                    'plannedTime': '19:55', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                    'tripId': '8059232507167694351', 'vehicleId': '-1188950296948414920'}]

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

    def test_create_dict_with_results_from_response_with_minus_time(self):
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

    def test_create_dict_with_results_from_response_without_minus_time(self):
        # given
        response = '{' \
                   '"actual": [' \
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

    def test_filter_results_with_only_line_number(self):
        # given
        user_input = {'Stop': 'Słomiana', 'LineNumber': '52', 'Direction': ''}
        expected_result = [{'actualRelativeTime': 152, 'actualTime': '19:35', 'direction': 'Os.Piastów',
                            'mixedTime': '2 %UNIT_MIN%', 'passageid': '-1188950301254934834', 'patternText': '52',
                            'plannedTime': '19:35', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507171085835', 'vehicleId': '-1188950296948413325'},
                           {'actualRelativeTime': 752, 'actualTime': '19:45', 'direction': 'Czerwone Maki P+R',
                            'mixedTime': '12 %UNIT_MIN%', 'passageid': '-1188950301254949688', 'patternText': '52',
                            'plannedTime': '19:42', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507170110990', 'vehicleId': '-1188950296948416950'},
                           {'actualRelativeTime': 1352, 'actualTime': '19:55', 'direction': 'Os.Piastów',
                            'mixedTime': '22 %UNIT_MIN%', 'passageid': '-1188950301254923551', 'patternText': '52',
                            'plannedTime': '19:55', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507167694351', 'vehicleId': '-1188950296948414920'}]

        # when
        result = filter_results(self.json_values, user_input)

        # then
        self.assertEqual(result, expected_result)

    def test_filter_results_with_only_direction(self):
        # given
        user_input = {'Stop': 'Słomiana', 'LineNumber': '', 'Direction': 'Czerwone Maki P+R'}
        expected_result = [{'actualRelativeTime': 752, 'actualTime': '19:45', 'direction': 'Czerwone Maki P+R',
                            'mixedTime': '12 %UNIT_MIN%', 'passageid': '-1188950301254949688', 'patternText': '52',
                            'plannedTime': '19:42', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507170110990', 'vehicleId': '-1188950296948416950'},
                           {'actualRelativeTime': 992, 'actualTime': '19:49', 'direction': 'Czerwone Maki P+R',
                            'mixedTime': '16 %UNIT_MIN%', 'passageid': '-1188950301254937736', 'patternText': '18',
                            'plannedTime': '19:49', 'routeId': '8059228650286874693', 'status': 'PREDICTED',
                            'tripId': '8059232507168656913', 'vehicleId': '-1188950296948414077'}]

        # when
        result = filter_results(self.json_values, user_input)

        # then
        self.assertEqual(result, expected_result)

    def test_filter_results_with_line_number_and_direction(self):
        # given
        user_input = {'Stop': 'Słomiana', 'LineNumber': '52', 'Direction': 'Os.Piastów'}
        expected_result = [{'actualRelativeTime': 152, 'actualTime': '19:35', 'direction': 'Os.Piastów',
                            'mixedTime': '2 %UNIT_MIN%', 'passageid': '-1188950301254934834', 'patternText': '52',
                            'plannedTime': '19:35', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507171085835', 'vehicleId': '-1188950296948413325'},
                           {'actualRelativeTime': 1352, 'actualTime': '19:55', 'direction': 'Os.Piastów',
                            'mixedTime': '22 %UNIT_MIN%', 'passageid': '-1188950301254923551', 'patternText': '52',
                            'plannedTime': '19:55', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507167694351', 'vehicleId': '-1188950296948414920'}]

        # when
        result = filter_results(self.json_values, user_input)

        # then
        self.assertEqual(result, expected_result)

    def test_filter_results_without_line_number_and_direction(self):
        # given
        user_input = {'Stop': 'Słomiana', 'LineNumber': '', 'Direction': ''}
        expected_result = [{'actualRelativeTime': 152, 'actualTime': '19:35', 'direction': 'Os.Piastów',
                            'mixedTime': '2 %UNIT_MIN%', 'passageid': '-1188950301254934834', 'patternText': '52',
                            'plannedTime': '19:35', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507171085835', 'vehicleId': '-1188950296948413325'},
                           {'actualRelativeTime': 272, 'direction': 'Borek Fałęcki', 'mixedTime': '19:37',
                            'passageid': '-1188950301254949237', 'patternText': '22', 'plannedTime': '19:37',
                            'routeId': '8059228650286874670', 'status': 'PLANNED', 'tripId': '8059232507167682058'},
                           {'actualRelativeTime': 692, 'actualTime': '19:44', 'direction': 'Kopiec Wandy',
                            'mixedTime': '11 %UNIT_MIN%', 'passageid': '-1188950301254930823', 'patternText': '22',
                            'plannedTime': '19:44', 'routeId': '8059228650286874670', 'status': 'PREDICTED',
                            'tripId': '8059232507168206349', 'vehicleId': '-1188950296948400570'},
                           {'actualRelativeTime': 752, 'actualTime': '19:45', 'direction': 'Czerwone Maki P+R',
                            'mixedTime': '12 %UNIT_MIN%', 'passageid': '-1188950301254949688', 'patternText': '52',
                            'plannedTime': '19:42', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507170110990', 'vehicleId': '-1188950296948416950'},
                           {'actualRelativeTime': 872, 'actualTime': '19:47', 'direction': 'Borek Fałęcki',
                            'mixedTime': '14 %UNIT_MIN%', 'passageid': '-1188950301254939507', 'patternText': '8',
                            'plannedTime': '19:47', 'routeId': '8059228650286875431', 'status': 'PREDICTED',
                            'tripId': '8059232507169173009', 'vehicleId': '-1188950296948415583'},
                           {'actualRelativeTime': 932, 'actualTime': '19:48', 'direction': 'Krowodrza Górka',
                            'mixedTime': '15 %UNIT_MIN%', 'passageid': '-1188950301254927499', 'patternText': '18',
                            'plannedTime': '19:48', 'routeId': '8059228650286874693', 'status': 'PREDICTED',
                            'tripId': '8059232507168194064', 'vehicleId': '-1188950296948418628'},
                           {'actualRelativeTime': 992, 'actualTime': '19:49', 'direction': 'Czerwone Maki P+R',
                            'mixedTime': '16 %UNIT_MIN%', 'passageid': '-1188950301254937736', 'patternText': '18',
                            'plannedTime': '19:49', 'routeId': '8059228650286874693', 'status': 'PREDICTED',
                            'tripId': '8059232507168656913', 'vehicleId': '-1188950296948414077'},
                           {'actualRelativeTime': 1172, 'actualTime': '19:52', 'direction': 'Bronowice Małe',
                            'mixedTime': '19 %UNIT_MIN%', 'passageid': '-1188950301254926300', 'patternText': '8',
                            'plannedTime': '19:52', 'routeId': '8059228650286875431', 'status': 'PREDICTED',
                            'tripId': '8059232507171040784', 'vehicleId': '-1188950296948415653'},
                           {'actualRelativeTime': 1352, 'actualTime': '19:55', 'direction': 'Os.Piastów',
                            'mixedTime': '22 %UNIT_MIN%', 'passageid': '-1188950301254923551', 'patternText': '52',
                            'plannedTime': '19:55', 'routeId': '8059228650286874694', 'status': 'PREDICTED',
                            'tripId': '8059232507167694351', 'vehicleId': '-1188950296948414920'}]

        # when
        result = filter_results(self.json_values, user_input)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
