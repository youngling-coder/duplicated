# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sourcesListWidget = QtWidgets.QListWidget(self.groupBox)
        self.sourcesListWidget.setObjectName("sourcesListWidget")
        self.verticalLayout_2.addWidget(self.sourcesListWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.addSourceButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.addSourceButton.sizePolicy().hasHeightForWidth()
        )
        self.addSourceButton.setSizePolicy(sizePolicy)
        self.addSourceButton.setObjectName("addSourceButton")
        self.horizontalLayout.addWidget(self.addSourceButton)
        self.removeSourceButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.removeSourceButton.sizePolicy().hasHeightForWidth()
        )
        self.removeSourceButton.setSizePolicy(sizePolicy)
        self.removeSourceButton.setObjectName("removeSourceButton")
        self.horizontalLayout.addWidget(self.removeSourceButton)
        self.clearSourceListButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clearSourceListButton.sizePolicy().hasHeightForWidth()
        )
        self.clearSourceListButton.setSizePolicy(sizePolicy)
        self.clearSourceListButton.setObjectName("clearSourceListButton")
        self.horizontalLayout.addWidget(self.clearSourceListButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.duplicatesTreeWidget = QtWidgets.QTreeWidget(self.groupBox_2)
        self.duplicatesTreeWidget.setObjectName("duplicatesTreeWidget")
        self.verticalLayout.addWidget(self.duplicatesTreeWidget)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.isRecursiveSearchEnabledCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.isRecursiveSearchEnabledCheckBox.setObjectName(
            "isRecursiveSearchEnabledCheckBox"
        )
        self.verticalLayout_3.addWidget(self.isRecursiveSearchEnabledCheckBox)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setText("")
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_2.addWidget(self.statusLabel)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Duplicated"))
        self.groupBox.setTitle(_translate("MainWindow", "Sources List"))
        self.addSourceButton.setText(_translate("MainWindow", "Add"))
        self.removeSourceButton.setText(_translate("MainWindow", "Remove"))
        self.clearSourceListButton.setText(_translate("MainWindow", "Clear"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Duplicates List"))
        self.duplicatesTreeWidget.headerItem().setText(
            0, _translate("MainWindow", "Duplicates")
        )
        self.isRecursiveSearchEnabledCheckBox.setText(
            _translate("MainWindow", "Recursive search")
        )
        self.startButton.setText(_translate("MainWindow", "Start"))
