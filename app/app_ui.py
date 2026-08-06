# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sourcesListWidget = QListWidget(self.groupBox)
        self.sourcesListWidget.setObjectName(u"sourcesListWidget")

        self.verticalLayout_2.addWidget(self.sourcesListWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addSourceButton = QPushButton(self.groupBox)
        self.addSourceButton.setObjectName(u"addSourceButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSourceButton.sizePolicy().hasHeightForWidth())
        self.addSourceButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.addSourceButton)

        self.removeSourceButton = QPushButton(self.groupBox)
        self.removeSourceButton.setObjectName(u"removeSourceButton")
        sizePolicy.setHeightForWidth(self.removeSourceButton.sizePolicy().hasHeightForWidth())
        self.removeSourceButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.removeSourceButton)

        self.clearSourceListButton = QPushButton(self.groupBox)
        self.clearSourceListButton.setObjectName(u"clearSourceListButton")
        sizePolicy.setHeightForWidth(self.clearSourceListButton.sizePolicy().hasHeightForWidth())
        self.clearSourceListButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.clearSourceListButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.duplicatesTreeWidget = QTreeWidget(self.groupBox_2)
        self.duplicatesTreeWidget.setObjectName(u"duplicatesTreeWidget")

        self.verticalLayout.addWidget(self.duplicatesTreeWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.isRecursiveSearchEnabledCheckBox = QCheckBox(self.centralwidget)
        self.isRecursiveSearchEnabledCheckBox.setObjectName(u"isRecursiveSearchEnabledCheckBox")

        self.verticalLayout_3.addWidget(self.isRecursiveSearchEnabledCheckBox)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.statusLabel)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.startButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Duplicated", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sources List", None))
        self.addSourceButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeSourceButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearSourceListButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Duplicates List", None))
        ___qtreewidgetitem = self.duplicatesTreeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Duplicates", None))
        self.isRecursiveSearchEnabledCheckBox.setText(QCoreApplication.translate("MainWindow", u"Recursive search", None))
        self.statusLabel.setText("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

