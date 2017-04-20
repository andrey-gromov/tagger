# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_setupTab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupTab(object):
    def setupUi(self, SetupTab):
        SetupTab.setObjectName("SetupTab")
        SetupTab.resize(1125, 786)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SetupTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(SetupTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_watchDirectory = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_watchDirectory.setEnabled(False)
        self.line_watchDirectory.setObjectName("line_watchDirectory")
        self.gridLayout_2.addWidget(self.line_watchDirectory, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.button_browseWatchDirectory = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.button_browseWatchDirectory.setFont(font)
        self.button_browseWatchDirectory.setAcceptDrops(False)
        self.button_browseWatchDirectory.setToolTip("")
        self.button_browseWatchDirectory.setAutoFillBackground(False)
        self.button_browseWatchDirectory.setObjectName("button_browseWatchDirectory")
        self.gridLayout_2.addWidget(self.button_browseWatchDirectory, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.group_openExistingFlight = QtWidgets.QGroupBox(SetupTab)
        self.group_openExistingFlight.setEnabled(False)
        self.group_openExistingFlight.setObjectName("group_openExistingFlight")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.group_openExistingFlight)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.combo_flights = QtWidgets.QComboBox(self.group_openExistingFlight)
        self.combo_flights.setObjectName("combo_flights")
        self.gridLayout_3.addWidget(self.combo_flights, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.group_openExistingFlight)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.button_loadFlight = QtWidgets.QPushButton(self.group_openExistingFlight)
        self.button_loadFlight.setObjectName("button_loadFlight")
        self.gridLayout_3.addWidget(self.button_loadFlight, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.group_openExistingFlight)
        self.group_createNewFlight = QtWidgets.QGroupBox(SetupTab)
        self.group_createNewFlight.setEnabled(False)
        self.group_createNewFlight.setObjectName("group_createNewFlight")
        self.gridLayout = QtWidgets.QGridLayout(self.group_createNewFlight)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.group_createNewFlight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.group_createNewFlight)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.group_createNewFlight)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.group_createNewFlight)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.edit_flightDate = QtWidgets.QDateEdit(self.group_createNewFlight)
        self.edit_flightDate.setCalendarPopup(True)
        self.edit_flightDate.setObjectName("edit_flightDate")
        self.gridLayout.addWidget(self.edit_flightDate, 2, 2, 1, 1)
        self.line_locationName = QtWidgets.QLineEdit(self.group_createNewFlight)
        self.line_locationName.setObjectName("line_locationName")
        self.gridLayout.addWidget(self.line_locationName, 0, 2, 1, 1)
        self.line_areaMap = QtWidgets.QLineEdit(self.group_createNewFlight)
        self.line_areaMap.setObjectName("line_areaMap")
        self.gridLayout.addWidget(self.line_areaMap, 4, 2, 1, 1)
        self.button_createFlight = QtWidgets.QPushButton(self.group_createNewFlight)
        self.button_createFlight.setObjectName("button_createFlight")
        self.gridLayout.addWidget(self.button_createFlight, 5, 2, 1, 1)
        self.line_siteElevation = QtWidgets.QLineEdit(self.group_createNewFlight)
        self.line_siteElevation.setObjectName("line_siteElevation")
        self.gridLayout.addWidget(self.line_siteElevation, 1, 2, 1, 1)
        self.button_selectAreaMap = QtWidgets.QPushButton(self.group_createNewFlight)
        self.button_selectAreaMap.setMaximumSize(QtCore.QSize(40, 16777215))
        self.button_selectAreaMap.setObjectName("button_selectAreaMap")
        self.gridLayout.addWidget(self.button_selectAreaMap, 4, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.group_createNewFlight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(SetupTab)
        QtCore.QMetaObject.connectSlotsByName(SetupTab)
        SetupTab.setTabOrder(self.combo_flights, self.button_loadFlight)
        SetupTab.setTabOrder(self.button_loadFlight, self.line_locationName)
        SetupTab.setTabOrder(self.line_locationName, self.line_siteElevation)
        SetupTab.setTabOrder(self.line_siteElevation, self.edit_flightDate)
        SetupTab.setTabOrder(self.edit_flightDate, self.button_createFlight)
        SetupTab.setTabOrder(self.button_createFlight, self.line_watchDirectory)
        SetupTab.setTabOrder(self.line_watchDirectory, self.button_browseWatchDirectory)

    def retranslateUi(self, SetupTab):
        _translate = QtCore.QCoreApplication.translate
        SetupTab.setWindowTitle(_translate("SetupTab", "Form"))
        self.groupBox_3.setTitle(_translate("SetupTab", "General"))
        self.label.setText(_translate("SetupTab", "Watch Directory:"))
        self.button_browseWatchDirectory.setText(_translate("SetupTab", "Browse..."))
        self.group_openExistingFlight.setTitle(_translate("SetupTab", "Open Existing Flight"))
        self.label_3.setText(_translate("SetupTab", "Flight:"))
        self.button_loadFlight.setText(_translate("SetupTab", "Load"))
        self.group_createNewFlight.setTitle(_translate("SetupTab", "Create Flight"))
        self.label_4.setText(_translate("SetupTab", "Site Elevation (MSL):"))
        self.label_5.setText(_translate("SetupTab", "Date:"))
        self.label_6.setText(_translate("SetupTab", "Area Map"))
        self.label_2.setText(_translate("SetupTab", "Location:"))
        self.button_createFlight.setText(_translate("SetupTab", "Create and Load"))
        self.button_selectAreaMap.setText(_translate("SetupTab", "..."))

