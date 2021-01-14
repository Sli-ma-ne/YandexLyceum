import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.rid)
        self.run()
    
    def run(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        

        result = cur.execute(f'''SELECT * FROM coffee''').fetchall()

        result = [list(map(str, list(i))) for i in result]
        self.result = result
        
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
            self.tableWidget.setItem(
                i, j + 1, QTableWidgetItem('0'))            
        self.tableWidget.resizeColumnsToContents()
                
        con.close()
        
    def add(self):
        self.second_form = SecondForm(self, -1)
        self.second_form.show()

        
    def rid(self):
        if self.tableWidget.currentRow() != -1:
            self.second_form = SecondForm(self, self.result[self.tableWidget.currentRow()][0])
            self.second_form.show()            


class SecondForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.n = args[1]
        print(self.n)
        uic.loadUi('addEditCoffeeForm.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        
    def run(self):
        
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        if self.n == -1:
            cur.execute(f'''INSERT INTO coffee([название сорта], [степень обжарки], [молотый/в зернах], [описание вкуса], цена, [объем упаковки]) 
            VALUES('{self.lineEdit.text()}', '{self.comboBox.currentText()}', '{self.comboBox_2.currentText()}', 
            '{self.lineEdit_2.text()}', '{self.spinBox.text()}', '{self.spinBox_2.text()}')''')
        else:
            cur.execute(f'''UPDATE coffee 
            SET [название сорта] = '{self.lineEdit.text()}', [степень обжарки] = '{self.comboBox.currentText()}', [молотый/в зернах] = '{self.comboBox_2.currentText()}', 
            [описание вкуса] = '{self.lineEdit_2.text()}', цена = '{self.spinBox.text()}', [объем упаковки] = '{self.spinBox_2.text()}'
            WHERE ID = {self.n}''')            
            
        con.commit()
        con.close()
        self.close()
        ex.run()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())