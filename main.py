from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QFontDialog, QColorDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from notepad import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionQuit.triggered.connect(self.quit)
        self.actionFont.triggered.connect(self.show_font)
        self.actionColor.triggered.connect(self.show_color)
        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste())
        self.actionCut.triggered.connect(lambda: self.textEdit.cut())
        self.actionUndo.triggered.connect(lambda: self.textEdit.undo())
        self.actionRedo.triggered.connect(lambda: self.textEdit.redo())
        self.actionBold.triggered.connect(self.bold_text)
        self.actionItalic.triggered.connect(lambda: self.textEdit.setFontItalic(not self.textEdit.fontItalic()))
        self.actionUnderline.triggered.connect(lambda: self.textEdit.setFontUnderline(not self.textEdit.fontUnderline()))
        self.actionAbout_app.triggered.connect(self.info_app)
        self.actionLeft.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.actionCenter.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.actionRight.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight))
        self.actionJustify.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify))


    def new_file(self):
        if self.textEdit.document().isModified():
            self.save_changes()
        self.textEdit.setText(str())
        

    def save_file(self):
        if self.textEdit.document().isModified():
            file = QFileDialog.getSaveFileName(self, "Save file")
            if file[1]:
                text = self.textEdit.toPlainText()
                with open(file[0], "w") as writer:
                    writer.write(text)
                QMessageBox.information(self, "Save file", "File saved successfully")
                self.textEdit.document().setModified(False)
                

    def print_file(self):
        pass

    
    def save_changes(self):
            message = QMessageBox.question(self, "save file", "Do you want to save changes ?")
            if message == QMessageBox.StandardButton.Yes:
                self.save_file()
        

    def open_file(self):
        if self.textEdit.document().isModified():
            self.save_changes()
        file = QFileDialog.getOpenFileName(self, "Open file")
        if file[1]:
            with open(file[0], "r") as reader:
                text = reader.read()
                self.textEdit.setText(text)
            
    
    def show_font(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.textEdit.setFont(font)
    

    def show_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    
    def quit(self):
        if self.textEdit.document().isModified():
            self.save_changes()
        self.close()

    
    def info_app(self):
        QMessageBox.information(self, "About app", "This is a simple notepad app designed with pyqt6")


    def bold_text(self):
        if self.textEdit.fontWeight() == 700:
            order = QFont().Weight.Normal
        else:
            order = QFont().Weight.Bold
        self.textEdit.setFontWeight(order)


app = QApplication(sys.argv)
root = Window()
sys.exit(app.exec())