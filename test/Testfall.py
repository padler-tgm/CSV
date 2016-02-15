import unittest
import csv

def csv_reader(file_obj, test = False):
    """
    Liest das uebergebene CSV-File
    :param das File welches verarbeitet wird
    :return den Inhalt des CSV-Files als Liste [[],[]]
    """
    if(test):
        reader = csv.reader(file_obj, delimiter=';')
        for row in reader:
            print(', '.join(row))
    reader = csv.reader(file_obj, delimiter=';')
    return list(reader)


class TestAllgemein(unittest.TestCase):
    def test_empytCSV(self):
        with open('empty.csv', newline='') as csvfile:
            self.assertEqual(csv_reader(csvfile), [])

    def test_noCSV(self):
            self.assertRaises(FileNotFoundError, open, '', newline='')

    def test_normalCSV_1row(self):
        with open('Datei1.csv', newline='') as csvfile:
            self.assertEqual(csv_reader(csvfile), [['1', '1']])

    def test_normalCSV_2row(self):
        with open("Datei.csv", newline='') as csvfile:
            self.assertEqual(csv_reader(csvfile), [['1', '1'], ['2', '2']])

    def test_delimiter(self):
        with open('Datei3.csv', newline='') as csvfile:
            self.assertIsNot(csv_reader(csvfile), [['1', '1']])

if __name__ == '__main__':
    unittest.main()