from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ModelTableview(QAbstractTableModel):
    """
    Model speichert sich den Inhalt der Tabele
    @author Philipp Adler
    @version 2016-01-16
    """
    def __init__(self, test_data, parent=None):
        """
        Konstruktor erzeugt ein TableModel
        :param test_data: Liste der Daten
        :param parent: optionaler Parameter
        """
        super(ModelTableview, self).__init__(parent)
        self.__test_data = test_data

    def rowCount(self, parent):
        """
        Anzahl der Reihen die angezeigt werden sollen
        :return: Anzahl der Reihen
        """
        return len(self.__test_data)

    def columnCount(self, parent):
        """
        Anzahl der Spalten die angezeigt werden sollen
        :return: Anzahl der Spalten
        """
        return len(self.__test_data)

    def data(self,index,role):
        """
        Gibt den Wert der Datenzelle zurueck
        :param index: Index um welche Datenzelle es sich handelt
        :param role: Um welche Rolle es sich handelt
        :return: Inhalt der Zelle
        """
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__test_data[row][column]
            return value
