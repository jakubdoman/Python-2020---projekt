import unittest
from jak_podjade.utils import section_to_print, get_time


class UtilsTest(unittest.TestCase):
    def test_section_to_print(self):
        # given
        value_to_print = 'Stop'
        const = 10

        # when
        result = section_to_print(value_to_print, const)

        # then
        self.assertEqual(result, "Stop      ")

    def test_get_time(self):
        # given
        time = 133

        # when
        result = get_time(time)

        # then
        self.assertEqual(result, '2min 13s')


if __name__ == '__main__':
    unittest.main()
