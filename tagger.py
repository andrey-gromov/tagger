# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tagger.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1730, 1250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_setup = QtWidgets.QWidget()
        self.tab_setup.setObjectName("tab_setup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_setup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 634, 156))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_sessionDirectory = QtWidgets.QLineEdit(self.groupBox)
        self.line_sessionDirectory.setObjectName("line_sessionDirectory")
        self.gridLayout.addWidget(self.line_sessionDirectory, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.button_sessionDirectory = QtWidgets.QPushButton(self.groupBox)
        self.button_sessionDirectory.setObjectName("button_sessionDirectory")
        self.gridLayout.addWidget(self.button_sessionDirectory, 2, 2, 1, 1)
        self.line_sessionName = QtWidgets.QLineEdit(self.groupBox)
        self.line_sessionName.setObjectName("line_sessionName")
        self.gridLayout.addWidget(self.line_sessionName, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_setup, "")
        self.tab_tagging = QtWidgets.QWidget()
        self.tab_tagging.setObjectName("tab_tagging")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_tagging)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layout_tagging = QtWidgets.QHBoxLayout()
        self.layout_tagging.setObjectName("layout_tagging")
        self.layout_taggingControls = QtWidgets.QVBoxLayout()
        self.layout_taggingControls.setObjectName("layout_taggingControls")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_tagging)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.layout_tagsButtons = QtWidgets.QHBoxLayout()
        self.layout_tagsButtons.setObjectName("layout_tagsButtons")
        self.button_addTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_addTag.setObjectName("button_addTag")
        self.layout_tagsButtons.addWidget(self.button_addTag)
        self.button_editTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_editTag.setObjectName("button_editTag")
        self.layout_tagsButtons.addWidget(self.button_editTag)
        self.button_removeTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_removeTag.setObjectName("button_removeTag")
        self.layout_tagsButtons.addWidget(self.button_removeTag)
        self.verticalLayout_2.addLayout(self.layout_tagsButtons)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 3)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.layout_taggingControls.addWidget(self.groupBox_2)
        self.label_5 = QtWidgets.QLabel(self.tab_tagging)
        self.label_5.setObjectName("label_5")
        self.layout_taggingControls.addWidget(self.label_5)
        self.layout_tagging.addLayout(self.layout_taggingControls)
        self.layout_taggingImage = QtWidgets.QVBoxLayout()
        self.layout_taggingImage.setObjectName("layout_taggingImage")
        self.taggableImage = PhotoViewer(self.tab_tagging)
        self.taggableImage.setObjectName("taggableImage")
        self.layout_taggingImage.addWidget(self.taggableImage)
        self.layout_tagging.addLayout(self.layout_taggingImage)
        self.layout_tagging.setStretch(0, 1)
        self.layout_tagging.setStretch(1, 3)
        self.horizontalLayout_3.addLayout(self.layout_tagging)
        self.tabWidget.addTab(self.tab_tagging, "")
        self.tab_targets = QtWidgets.QWidget()
        self.tab_targets.setObjectName("tab_targets")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_targets)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(6, 7, 1701, 1101))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_5)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listView_2 = QtWidgets.QListView(self.groupBox_5)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_6.addWidget(self.listView_2)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_5)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.listView = QtWidgets.QListView(self.groupBox_4)
        self.listView.setObjectName("listView")
        self.verticalLayout_5.addWidget(self.listView)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.tabWidget.addTab(self.tab_targets, "")
        self.tab_map = QtWidgets.QWidget()
        self.tab_map.setObjectName("tab_map")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_map)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_map)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_map)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_map)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_7.addWidget(self.listWidget_3)
        self.gridLayout_3.addWidget(self.groupBox_6, 2, 0, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_map)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_map)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 3, 1, 1)
        self.gridLayout_3.setColumnStretch(3, 3)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_map, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1730, 43))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuTest.addAction(self.actionQuit)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Guardian Image Tagger"))
        self.groupBox.setTitle(_translate("MainWindow", "Session"))
        self.label.setText(_translate("MainWindow", "Working Directory:"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.button_sessionDirectory.setText(_translate("MainWindow", "Browse..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setup), _translate("MainWindow", "Setup"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tags"))
        self.button_addTag.setText(_translate("MainWindow", "Add"))
        self.button_editTag.setText(_translate("MainWindow", "Edit"))
        self.button_removeTag.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Images"))
        self.pushButton_3.setText(_translate("MainWindow", "Mark as Reviewed"))
        self.pushButton_6.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.setText(_translate("MainWindow", "Fit to Screen"))
        self.pushButton_5.setText(_translate("MainWindow", "Previous"))
        self.pushButton_7.setText(_translate("MainWindow", "Toggle View"))
        self.label_5.setText(_translate("MainWindow", "MINIMAP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tagging), _translate("MainWindow", "Tagging"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Select Tag"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Images with Selected Tag"))
        self.lineEdit.setText(_translate("MainWindow", "search image by name"))
        self.label_6.setText(_translate("MainWindow", "MINIMAP"))
        self.label_4.setText(_translate("MainWindow", "IMAGE VIEW"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_targets), _translate("MainWindow", "Targets"))
        self.pushButton_8.setText(_translate("MainWindow", "Search"))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_8.setText(_translate("MainWindow", "MAP VIEW"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_map), _translate("MainWindow", "Map"))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Exit"))

from photoViewer import PhotoViewer
