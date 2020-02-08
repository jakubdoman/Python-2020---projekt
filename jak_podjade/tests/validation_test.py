import unittest
from jak_podjade.validation import validate_input, get_list_with_ratio, get_stop_with_nth_index


class ValidationTest(unittest.TestCase):
    def test_validate_input_with_wrong_stop_name(self):
        # given
        stop = 'slomiana'
        all_stop_names = ['Kobierzyńska', 'Brożka', 'Słomiana', 'Rzemieślnicza']
        expected_result = 'Słomiana'

        # when
        result = validate_input(stop, all_stop_names)

        # then
        self.assertEqual(result, expected_result)

    def test_validate_input_with_correct_stop_name(self):
        # given
        stop = 'Słomiana'
        all_stop_names = ['Brożka', 'Słomiana', 'Rzemieślnicza']
        expected_result = 'Słomiana'

        # when
        result = validate_input(stop, all_stop_names)

        # then
        self.assertEqual(result, expected_result)

    def test_get_list_with_ratio(self):
        # given
        stop = 'brozka'
        stops_list = ['Os.Piastów', 'Lubicz', 'Czerwone Maki P+R', 'Chmieleniec', 'Kampus UJ', 'Borek Fałęcki', 'Borek Fałęcki I', 'Solvay', 'Sanktuarium Bożego Miłosierdzia', 'Kurdwanów', 'Kurdwanów P+R', 'Łagiewniki ZUS', 'Biprostal', 'Salwator', 'Ruczaj', 'Norymberska', 'Reymana', 'Filharmonia', 'Korona', 'Grota-Roweckiego', 'Lipińskiego', 'Borsucza', 'Kobierzyńska', 'Brożka']
        expected_result = [12, 33, 26, 0, 13, 32, 29, 33, 22, 27, 21, 10, 40, 14, 33, 47, 15, 35, 50, 27, 12, 43, 56, 67]

        # when
        result = get_list_with_ratio(stop, stops_list)

        # then
        self.assertEqual(result, expected_result)

    def test_get_stop_with_nth_index(self):
        # given
        stops = ['Os.Piastów', 'Lubicz', 'Czerwone Maki P+R', 'Chmieleniec', 'Kampus UJ', 'Borek Fałęcki']
        index = 2
        expected_result = 'Czerwone Maki P+R'

        # when
        result = get_stop_with_nth_index(stops, index)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
