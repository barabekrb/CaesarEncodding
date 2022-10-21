# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_caesar.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 263)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cod_le = QLineEdit(self.centralwidget)
        self.cod_le.setObjectName(u"cod_le")
        self.cod_le.setGeometry(QRect(120, 80, 151, 51))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 90, 111, 31))
        self.Coder_pb = QPushButton(self.centralwidget)
        self.Coder_pb.setObjectName(u"Coder_pb")
        self.Coder_pb.setGeometry(QRect(320, 90, 131, 25))
        self.Decoder_pb = QPushButton(self.centralwidget)
        self.Decoder_pb.setObjectName(u"Decoder_pb")
        self.Decoder_pb.setGeometry(QRect(320, 160, 131, 25))
        self.text_le = QLineEdit(self.centralwidget)
        self.text_le.setObjectName(u"text_le")
        self.text_le.setGeometry(QRect(120, 10, 151, 51))
        self.decod_le = QLineEdit(self.centralwidget)
        self.decod_le.setObjectName(u"decod_le")
        self.decod_le.setGeometry(QRect(120, 150, 151, 51))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 20, 111, 31))
        self.key_ed = QLineEdit(self.centralwidget)
        self.key_ed.setObjectName(u"key_ed")
        self.key_ed.setGeometry(QRect(390, 10, 113, 25))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(330, 10, 51, 31))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 160, 111, 31))
        self.eng_rb = QRadioButton(self.centralwidget)
        self.eng_rb.setObjectName(u"eng_rb")
        self.eng_rb.setGeometry(QRect(330, 50, 51, 23))
        self.rus_rb = QRadioButton(self.centralwidget)
        self.rus_rb.setObjectName(u"rus_rb")
        self.rus_rb.setGeometry(QRect(400, 50, 51, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 524, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    


    def lang_er(self):
        msg = QMessageBox()
        msg.setText("Вы не выбрали язык шифровки!!!")
        x = msg.exec_()

    def key_er(self):
        msg = QMessageBox()
        msg.setText("Ключ должен быть целым числом!!!")
        x = msg.exec_()

    def dif_lang(self):
        msg = QMessageBox()
        msg.setText("Языки сообщения и кодировки не совпадают!!!")
        x = msg.exec_()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430", None))
        self.Coder_pb.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Decoder_pb.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430", None))
        self.eng_rb.setText(QCoreApplication.translate("MainWindow", u"eng", None))
        self.rus_rb.setText(QCoreApplication.translate("MainWindow", u"rus", None))
    # retranslateUi

