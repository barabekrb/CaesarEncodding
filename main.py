from base64 import decode
import sys

from py import code
import CaesarCoder
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_caesar import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Coder_pb.clicked.connect(self.coding)
        self.ui.Decoder_pb.clicked.connect(self.decoding)
    
    def coding(self):
        text_in = self.ui.text_le.text().lower()
        key = self.ui.key_ed.text()
        try:
            key = int(self.ui.key_ed.text())
        except ValueError:
            self.ui.key_er()
        if self.ui.rus_rb.isChecked():
            lang = self.ui.rus_rb.text()
        elif self.ui.eng_rb.isChecked():
            lang = self.ui.eng_rb.text()
        else: self.ui.lang_er()
        
        code_text = CaesarCoder.CaesarCoder.Coder(text_in, key, lang)
        decode_text = CaesarCoder.CaesarCoder.Decoder(code_text, key, lang)
        if (decode_text!=text_in):
            self.ui.dif_lang()
        else:
            self.ui.cod_le.setText(code_text)

    def decoding(self):
        de_text = self.ui.cod_le.text().lower()
        try:
            key = int(self.ui.key_ed.text())
        except ValueError:
            self.ui.key_er()
        if self.ui.rus_rb.isChecked():
            lang = self.ui.rus_rb.text()
        elif self.ui.eng_rb.isChecked():
            lang = self.ui.eng_rb.text()
        else: self.ui.lang_er()
        
        encoder_text = CaesarCoder.CaesarCoder.Decoder(de_text, key, lang)
        first_text = CaesarCoder.CaesarCoder.Coder(encoder_text, key, lang)
        if (first_text!=de_text):
            self.ui.dif_lang()
        else:
            self.ui.decod_le.setText(encoder_text)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
