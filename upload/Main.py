import csv
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
#from CSV.src.upload import View, Model
import sys

"""
class Controller(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.myForm = View.Ui_Form()#holt sich die View
        self.myForm.setupUi(self)
        self.myForm.pushButton.setEnabled(True)#macht den Button klickbar
        self.myForm.pushButton.clicked.connect(self.filedialog)#Listener auf den Button

    def filedialog(self):
        message = QFileDialog()
        csv_path = message.getOpenFileName(self, "Open file", "", "CSV (*.csv);;")[0]
        if csv_path != '':
            with open(csv_path, newline='') as file:
                self.setTableView(csv_reader(file))

    def setTableView(self, list):
        self.dm = Model.ModelTableview(list)
        self.myForm.tableView.setModel(self.dm)
        self.myForm.tableView.verticalHeader().setDefaultSectionSize(15);
        self.myForm.tableView.horizontalHeader().setDefaultSectionSize(100);
"""
#----------------------------------------------------------------------
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

#----------------------------------------------------------------------
if __name__ == "__main__":
    """
    Main-Methode ruft den Controller auf
    """
    with open('Datei1.csv', newline='') as csvfile:
        csv_reader(csvfile, True)
    #app = QApplication(sys.argv)
    #c = Controller()
    #c.show()
    #sys.exit(app.exec_())
