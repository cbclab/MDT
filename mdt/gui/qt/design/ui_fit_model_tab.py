# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fit_model_tab.ui'
#
# Created: Wed Jul 13 15:26:38 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FitModelTabContent(object):
    def setupUi(self, FitModelTabContent):
        FitModelTabContent.setObjectName("FitModelTabContent")
        FitModelTabContent.resize(1047, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(FitModelTabContent)
        self.verticalLayout.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(FitModelTabContent)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selectMask = QtWidgets.QPushButton(FitModelTabContent)
        self.selectMask.setObjectName("selectMask")
        self.horizontalLayout_3.addWidget(self.selectMask)
        self.selectedMask = QtWidgets.QLineEdit(FitModelTabContent)
        self.selectedMask.setText("")
        self.selectedMask.setObjectName("selectedMask")
        self.horizontalLayout_3.addWidget(self.selectedMask)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.selectProtocol = QtWidgets.QPushButton(FitModelTabContent)
        self.selectProtocol.setObjectName("selectProtocol")
        self.horizontalLayout_6.addWidget(self.selectProtocol)
        self.selectedProtocol = QtWidgets.QLineEdit(FitModelTabContent)
        self.selectedProtocol.setText("")
        self.selectedProtocol.setObjectName("selectedProtocol")
        self.horizontalLayout_6.addWidget(self.selectedProtocol)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(FitModelTabContent)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(FitModelTabContent)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(FitModelTabContent)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectDWI = QtWidgets.QPushButton(FitModelTabContent)
        self.selectDWI.setObjectName("selectDWI")
        self.horizontalLayout_2.addWidget(self.selectDWI)
        self.selectedDWI = QtWidgets.QLineEdit(FitModelTabContent)
        self.selectedDWI.setText("")
        self.selectedDWI.setObjectName("selectedDWI")
        self.horizontalLayout_2.addWidget(self.selectedDWI)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(FitModelTabContent)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(FitModelTabContent)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)
        self.modelSelection = QtWidgets.QComboBox(FitModelTabContent)
        self.modelSelection.setObjectName("modelSelection")
        self.gridLayout.addWidget(self.modelSelection, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(FitModelTabContent)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.selectOutputFolder = QtWidgets.QPushButton(FitModelTabContent)
        self.selectOutputFolder.setObjectName("selectOutputFolder")
        self.horizontalLayout_7.addWidget(self.selectOutputFolder)
        self.selectedOutputFolder = QtWidgets.QLineEdit(FitModelTabContent)
        self.selectedOutputFolder.setText("")
        self.selectedOutputFolder.setObjectName("selectedOutputFolder")
        self.horizontalLayout_7.addWidget(self.selectedOutputFolder)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(FitModelTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(FitModelTabContent)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtWidgets.QPushButton(FitModelTabContent)
        self.runButton.setEnabled(False)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(FitModelTabContent)
        QtCore.QMetaObject.connectSlotsByName(FitModelTabContent)
        FitModelTabContent.setTabOrder(self.selectDWI, self.selectedDWI)
        FitModelTabContent.setTabOrder(self.selectedDWI, self.runButton)

    def retranslateUi(self, FitModelTabContent):
        _translate = QtCore.QCoreApplication.translate
        FitModelTabContent.setWindowTitle(_translate("FitModelTabContent", "Form"))
        self.label.setText(_translate("FitModelTabContent", "Fit model"))
        self.label_2.setText(_translate("FitModelTabContent", "Optimize a model to your data."))
        self.label_14.setText(_translate("FitModelTabContent", "(Defaults to \"output/<mask_name>\" in the DWI directory)"))
        self.selectMask.setText(_translate("FitModelTabContent", "Browse"))
        self.selectProtocol.setText(_translate("FitModelTabContent", "Browse"))
        self.label_12.setText(_translate("FitModelTabContent", "Select model:"))
        self.label_11.setText(_translate("FitModelTabContent", "(Select your protocol file, see tab \"Generate protocol file\")"))
        self.label_3.setText(_translate("FitModelTabContent", "Select brain mask:"))
        self.label_4.setText(_translate("FitModelTabContent", "(Select your preprocessed 4d diffusion weighted volume)"))
        self.selectDWI.setText(_translate("FitModelTabContent", "Browse"))
        self.label_6.setText(_translate("FitModelTabContent", "Select DWI:"))
        self.label_5.setText(_translate("FitModelTabContent", "(Select your brain mask, see tab \"Generate brain mask\")"))
        self.label_13.setText(_translate("FitModelTabContent", "Select output folder:"))
        self.label_10.setText(_translate("FitModelTabContent", "Select protocol file:"))
        self.selectOutputFolder.setText(_translate("FitModelTabContent", "Browse"))
        self.label_15.setText(_translate("FitModelTabContent", "(Please select a model)"))
        self.runButton.setText(_translate("FitModelTabContent", "Run"))

