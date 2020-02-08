import unittest
from jak_podjade.request import load_traffic_for_stop, load_all_stops


class RequestTest(unittest.TestCase):
    def test_load_all_stops(self):
        # given
        expected_result = {'Os.Piastów': '378', 'Lubicz': '126', 'Czerwone Maki P+R': '3038', 'Chmieleniec': '2691', 'Kampus UJ': '2690', 'Borek Fałęcki': '747', 'Borek Fałęcki I': '824', 'Solvay': '746', 'Sanktuarium Bożego Miłosierdzia': '615', 'Kurdwanów': '744', 'Kurdwanów P+R': '3176', 'Łagiewniki ZUS': '2821', 'Biprostal': '84', 'Salwator': '311', 'Ruczaj': '589', 'Norymberska': '2688', 'Reymana': '320', 'Filharmonia': '322', 'Korona': '571', 'Grota-Roweckiego': '2687', 'Lipińskiego': '2686', 'Borsucza': '612', 'Kobierzyńska': '584', 'Brożka': '613', 'Słomiana': '577', 'Rzemieślnicza': '611', 'PT': '614', 'Łagiewniki': '922', 'Rondo Matecznego': '610', 'Smolki': '572', 'Cracovia': '318', 'Muzeum Narodowe': '3141', 'Kapelanka': '576', 'Most Grunwaldzki': '574', 'Centrum Kongresowe ICE': '3039', 'Rondo Grunwaldzkie': '3338', 'Szwedzka': '575', 'Komorowskiego': '313', 'Park Jordana': '960', 'Oleandry': '823', 'Jubilat': '319', 'Uniwersytet Jagielloński': '321', 'Orzeszkowej': '361', 'Stradom': '359', 'Muzeum Inżynierii Miejskiej': '2726', 'Plac Wolnica': '360', 'Dajwór': '915', 'Św.Wawrzyńca': '2742', 'Wawel': '325', 'Plac Wszystkich Świętych': '1360', 'Poczta Główna': '357', 'Św.Gertrudy': '2741', 'Starowiślna': '358', 'Miodowa': '362', 'Hala Targowa': '363', 'Wesele': '133', 'Cichy Kącik': '87', 'Głowackiego': '1049', 'Bronowice': '89', 'Uniwersytet Pedagogiczny': '88', 'Bronowice Małe': '135', 'Balicka Wiadukt': '134', 'Bronowice Wiadukt': '136', 'Bratysławska': '61', 'Batorego': '78', 'Teatr Bagatela': '77', 'Plac Inwalidów': '79', 'Urzędnicza': '83', 'Politechnika': '73', 'Stary Kleparz': '3032', 'Basztowa LOT': '75', 'Pędzichów': '72', 'Dworzec Główny': '131', 'Teatr Słowackiego': '3242', 'Dworzec Główny Zachód': '2608', 'Dworzec Główny Tunel': '1173', 'Dworzec Towarowy': '70', 'Nowy Kleparz': '71', 'Krowodrza Górka': '63', 'Prądnicka': '69', 'Szpital Narutowicza': '3036', 'Witosa': '718', 'Nowosądecka': '715', 'Bieżanowska': '630', 'Piaski Nowe': '716', 'Dauna': '632', 'Wlotowa': '634', 'Prokocim Szpital': '682', 'Prokocim': '637', 'Teligi': '681', 'Nowy Prokocim': '2582', 'Ćwiklińskiej': '679', 'Nowy Bieżanów': '2580', 'Nowy Bieżanów P+R': '3175', 'Fabryczna': '368', 'Powstańców Wielkopolskich': '568', 'Podgórze SKA': '3158', 'Cmentarz Podgórski': '621', 'Kabel': '624', 'Dworcowa': '623', 'Dworzec Płaszów Estakada': '2870', 'Gromadzka': '560', 'Lipska': '561', 'Limanowskiego': '569', 'Plac Bohaterów Getta': '570', 'Zabłocie': '1154', 'Klimeckiego': '946', 'Rondo Grzegórzeckie': '365', 'Kordylewskiego': '2536', 'Teatr Variété': '2859', 'Francesco Nullo': '367', 'Dąbie': '370', 'Kuklińskiego': '567', 'Ofiar Dąbia': '369', 'Mały Płaszów': '1263', 'Mały Płaszów P+R': '3310', 'Rzebika': '1262', 'Cystersów': '129', 'Rondo Mogilskie': '125', 'Rakowicka': '128', 'Uniwersytet Ekonomiczny': '127', 'Cmentarz Rakowicki': '124', 'Wieczysta': '114', 'TAURON Arena Kraków Wieczysta': '3040', 'Białucha': '130', 'Kraków Plaza': '959', 'Plaza': '3033', 'Lema': '2537', 'Kraków Arena Al. Pokoju': '2803', 'TAURON Arena Kraków Al. Pokoju': '2871', 'M1 Al. Pokoju': '930', 'Nowohucka': '372', 'Rondo 308. Dywizjonu': '3041', 'Muzeum Lotnictwa': '2811', 'AWF': '113', 'Stella-Sawickiego': '112', 'Centralna': '409', 'Czyżyny': '407', 'Rondo Czyżyńskie': '408', 'Bieńczycka': '867', 'Mistrzejowice': '375', 'Os.Złotego Wieku': '377', 'Miśnieńska': '2538', 'Dunikowskiego': '388', 'DH Wanda': '392', 'Rondo Piastowskie': '383', 'Kleeberga': '382', 'Piasta Kołodzieja': '379', 'Rondo Hipokratesa': '2539', 'Plac Centralny im. R.Reagana': '2744', 'Os.Kolorowe': '413', 'Rondo Kocmyrzowskie im. Ks. Gorzelanego': '2745', 'Os.Zgody': '418', 'Klasztorna': '429', 'Os.Na Skarpie': '424', 'Suche Stawy': '2548', 'Struga': '423', 'Teatr Ludowy': '420', 'Cienista': '3037', 'Kocmyrzowska': '401', 'Wańkowicza': '2543', 'Wiadukty': '434', 'Cmentarz Grębałów Zachód': '2549', 'Jarzębiny': '2685', 'Darwina': '435', 'Agencja Kraków Wschód': '462', 'Walcownia': '463', 'Bardosa': '449', 'Kopiec Wandy': '450', 'Brama nr 4': '451', 'Fort Mogiła': '1051', 'Kombinat': '459', 'Jeżynowa': '452', 'Brama nr 5': '453', 'Meksyk': '454', 'Wzgórza Krzesławickie': '442', 'PH': '466', 'Zajezdnia Nowa Huta': '465', 'Elektromontaż': '464', 'Mrozowa': '460', 'Blokowa': '461', 'Pleszów': '458', 'Koksochemia': '457'}

        # when
        result = load_all_stops()

        # then
        self.assertEqual(result, expected_result)

    def test_load_traffic_for_stop_with_wrong_line_number_for_particular_stop(self):
        # given
        user_input = {'Stop': 'Słomiana', 'LineNumber': '1', 'Direction': ''}
        stop_id = '577'
        expected_result = {}

        # when
        result = load_traffic_for_stop(user_input, stop_id)

        # then
        self.assertEqual(result, expected_result)

    def test_load_traffic_for_stop_with_not_connected_stop_and_direction(self):
        # given
        user_input = {'Stop': 'Rzemieślnicza', 'LineNumber': '', 'Direction': 'Os. Piastów'}
        stop_id = '611'
        expected_result = {}

        # when
        result = load_traffic_for_stop(user_input, stop_id)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
