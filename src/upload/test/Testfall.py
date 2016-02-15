import unittest
import Main


class TestAllgemein(unittest.TestCase):
    def test_empytCSV(self):
        with open('empty.csv', newline='') as csvfile:
            self.assertEqual(Main.csv_reader(csvfile), [])

    def test_noCSV(self):
            self.assertRaises(FileNotFoundError, open, '', newline='')

    def test_normalCSV_1row(self):
        with open('Datei1.csv', newline='') as csvfile:
            self.assertEqual(Main.csv_reader(csvfile), [['1', '1']])

    def test_normalCSV_2row(self):
        with open('Datei2.csv', newline='') as csvfile:
            self.assertEqual(Main.csv_reader(csvfile), [['1', '1'], ['2', '2']])

    def test_delimiter(self):
        with open('Datei3.csv', newline='') as csvfile:
            self.assertIsNot(Main.csv_reader(csvfile), [['1', '1']])

if __name__ == '__main__':
    unittest.main()