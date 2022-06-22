from PyQt5 import QtCore, QtGui, QtWidgets

class UID(object): # UI dialog obj.
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 750)
        self.imgLabel_1 = QtWidgets.QLabel(Dialog)
        self.imgLabel_1.setGeometry(QtCore.QRect(10, 100, 980, 640))
        self.imgLabel_1.setAutoFillBackground(False)
        self.imgLabel_1.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel_1.setLineWidth(2)
        self.imgLabel_1.setScaledContents(True)
        self.imgLabel_1.setObjectName("imgLabel_1")

        self.START = QtWidgets.QPushButton(Dialog)
        self.START.setGeometry(QtCore.QRect(225, 20, 100, 60))
        self.START.setObjectName("START")

        self.PAUSE = QtWidgets.QPushButton(Dialog)
        self.PAUSE.setGeometry(QtCore.QRect(350, 20, 100, 60))
        self.PAUSE.setObjectName("PAUSE")

        self.RESUME = QtWidgets.QPushButton(Dialog)
        self.RESUME.setGeometry(QtCore.QRect(475, 20, 100, 60))
        self.RESUME.setObjectName("RESUME")

        self.CLOSE = QtWidgets.QPushButton(Dialog)
        self.CLOSE.setGeometry(QtCore.QRect(600, 20, 100, 60))
        self.CLOSE.setObjectName("CLOSE")

        font = QtGui.QFont()
        font.setPointSize(9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.imgLabel_1.setText(_translate("Dialog", "TextLabel"))
        self.START.setText(_translate("Dialog", "Start"))
        self.PAUSE.setText(_translate("Dialog", "Pause"))
        self.RESUME.setText(_translate("Dialog", "Resume"))
        self.CLOSE.setText(_translate("Dialog", "Close"))
