# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_results_tab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewResultsTabContent(object):
    def setupUi(self, ViewResultsTabContent):
        ViewResultsTabContent.setObjectName("ViewResultsTabContent")
        ViewResultsTabContent.resize(938, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(ViewResultsTabContent)
        self.verticalLayout.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(ViewResultsTabContent)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(ViewResultsTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(ViewResultsTabContent)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deselectAllButton = QtWidgets.QPushButton(ViewResultsTabContent)
        self.deselectAllButton.setObjectName("deselectAllButton")
        self.horizontalLayout_3.addWidget(self.deselectAllButton)
        self.invertSelectionButton = QtWidgets.QPushButton(ViewResultsTabContent)
        self.invertSelectionButton.setObjectName("invertSelectionButton")
        self.horizontalLayout_3.addWidget(self.invertSelectionButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ViewResultsTabContent)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.selectMaps = QtWidgets.QListWidget(ViewResultsTabContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.selectMaps.sizePolicy().hasHeightForWidth())
        self.selectMaps.setSizePolicy(sizePolicy)
        self.selectMaps.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.selectMaps.setObjectName("selectMaps")
        self.gridLayout.addWidget(self.selectMaps, 2, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(ViewResultsTabContent)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(ViewResultsTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectFolderButton = QtWidgets.QPushButton(ViewResultsTabContent)
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.horizontalLayout_2.addWidget(self.selectFolderButton)
        self.selectedFolderText = QtWidgets.QLineEdit(ViewResultsTabContent)
        self.selectedFolderText.setText("")
        self.selectedFolderText.setObjectName("selectedFolderText")
        self.horizontalLayout_2.addWidget(self.selectedFolderText)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(ViewResultsTabContent)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(ViewResultsTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(ViewResultsTabContent)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(ViewResultsTabContent)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)
        self.initialDimensionChooser = QtWidgets.QSpinBox(ViewResultsTabContent)
        self.initialDimensionChooser.setMaximum(2)
        self.initialDimensionChooser.setProperty("value", 2)
        self.initialDimensionChooser.setObjectName("initialDimensionChooser")
        self.horizontalLayout_4.addWidget(self.initialDimensionChooser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(ViewResultsTabContent)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_10)
        self.initialSliceChooser = QtWidgets.QSpinBox(ViewResultsTabContent)
        self.initialSliceChooser.setObjectName("initialSliceChooser")
        self.horizontalLayout_4.addWidget(self.initialSliceChooser)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(ViewResultsTabContent)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.maximumIndexLabel = QtWidgets.QLabel(ViewResultsTabContent)
        self.maximumIndexLabel.setObjectName("maximumIndexLabel")
        self.horizontalLayout_5.addWidget(self.maximumIndexLabel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(ViewResultsTabContent)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewButton = QtWidgets.QPushButton(ViewResultsTabContent)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2.raise_()
        self.line.raise_()

        self.retranslateUi(ViewResultsTabContent)
        QtCore.QMetaObject.connectSlotsByName(ViewResultsTabContent)
        ViewResultsTabContent.setTabOrder(self.selectFolderButton, self.selectedFolderText)
        ViewResultsTabContent.setTabOrder(self.selectedFolderText, self.selectMaps)
        ViewResultsTabContent.setTabOrder(self.selectMaps, self.deselectAllButton)
        ViewResultsTabContent.setTabOrder(self.deselectAllButton, self.invertSelectionButton)
        ViewResultsTabContent.setTabOrder(self.invertSelectionButton, self.initialDimensionChooser)
        ViewResultsTabContent.setTabOrder(self.initialDimensionChooser, self.initialSliceChooser)
        ViewResultsTabContent.setTabOrder(self.initialSliceChooser, self.viewButton)

    def retranslateUi(self, ViewResultsTabContent):
        _translate = QtCore.QCoreApplication.translate
        ViewResultsTabContent.setWindowTitle(_translate("ViewResultsTabContent", "Form"))
        self.label.setText(_translate("ViewResultsTabContent", "View results"))
        self.label_2.setText(_translate("ViewResultsTabContent", "View a selection of maps in the given folder."))
        self.deselectAllButton.setText(_translate("ViewResultsTabContent", "Deselect all"))
        self.invertSelectionButton.setText(_translate("ViewResultsTabContent", "Invert selection"))
        self.label_3.setText(_translate("ViewResultsTabContent", "Select maps:"))
        self.label_5.setText(_translate("ViewResultsTabContent", "(Select the maps you would like to display)"))
        self.selectFolderButton.setText(_translate("ViewResultsTabContent", "Browse"))
        self.label_6.setText(_translate("ViewResultsTabContent", "Select input folder:"))
        self.label_4.setText(_translate("ViewResultsTabContent", "(Choose a directory with .nii(.gz) files)"))
        self.label_7.setText(_translate("ViewResultsTabContent", "Initial dimension:"))
        self.label_9.setText(_translate("ViewResultsTabContent", "Initial slice:"))
        self.label_8.setText(_translate("ViewResultsTabContent", "/ "))
        self.maximumIndexLabel.setText(_translate("ViewResultsTabContent", "x"))
        self.viewButton.setText(_translate("ViewResultsTabContent", "View"))

