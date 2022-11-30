# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_files/designer_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(365, 700))
        MainWindow.setMaximumSize(QtCore.QSize(999999, 999999))
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("Liewa")
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.image_compostion = QtWidgets.QWidget()
        self.image_compostion.setObjectName("image_compostion")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.image_compostion)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.canvas_size = QtWidgets.QLabel(self.image_compostion)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.canvas_size.setFont(font)
        self.canvas_size.setObjectName("canvas_size")
        self.verticalLayout_3.addWidget(self.canvas_size)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.size_dropdown = QtWidgets.QComboBox(self.image_compostion)
        self.size_dropdown.setObjectName("size_dropdown")
        self.size_dropdown.addItem("")
        self.size_dropdown.addItem("")
        self.horizontalLayout_5.addWidget(self.size_dropdown)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.custom_size_checkbox = QtWidgets.QCheckBox(self.image_compostion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_size_checkbox.sizePolicy().hasHeightForWidth())
        self.custom_size_checkbox.setSizePolicy(sizePolicy)
        self.custom_size_checkbox.setMinimumSize(QtCore.QSize(0, 0))
        self.custom_size_checkbox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.custom_size_checkbox.setObjectName("custom_size_checkbox")
        self.horizontalLayout_2.addWidget(self.custom_size_checkbox)
        self.line_2 = QtWidgets.QFrame(self.image_compostion)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.x_label = QtWidgets.QLabel(self.image_compostion)
        self.x_label.setEnabled(False)
        self.x_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.x_label.setObjectName("x_label")
        self.horizontalLayout_2.addWidget(self.x_label, 0, QtCore.Qt.AlignHCenter)
        self.x_value_input = QtWidgets.QSpinBox(self.image_compostion)
        self.x_value_input.setEnabled(False)
        self.x_value_input.setMinimumSize(QtCore.QSize(30, 0))
        self.x_value_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.x_value_input.setMaximum(9999)
        self.x_value_input.setObjectName("x_value_input")
        self.horizontalLayout_2.addWidget(self.x_value_input)
        self.y_label = QtWidgets.QLabel(self.image_compostion)
        self.y_label.setEnabled(False)
        self.y_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.y_label.setObjectName("y_label")
        self.horizontalLayout_2.addWidget(self.y_label, 0, QtCore.Qt.AlignHCenter)
        self.y_value_input = QtWidgets.QSpinBox(self.image_compostion)
        self.y_value_input.setEnabled(False)
        self.y_value_input.setMinimumSize(QtCore.QSize(0, 0))
        self.y_value_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.y_value_input.setMaximum(9999)
        self.y_value_input.setObjectName("y_value_input")
        self.horizontalLayout_2.addWidget(self.y_value_input)
        self.size_error_label = QtWidgets.QLabel(self.image_compostion)
        self.size_error_label.setEnabled(True)
        self.size_error_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.size_error_label.setObjectName("size_error_label")
        self.horizontalLayout_2.addWidget(self.size_error_label)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.background_color = QtWidgets.QLabel(self.image_compostion)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.background_color.setFont(font)
        self.background_color.setObjectName("background_color")
        self.verticalLayout_3.addWidget(self.background_color)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.choose_color_btn = QtWidgets.QPushButton(self.image_compostion)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.horizontalLayout_6.addWidget(self.choose_color_btn)
        self.choosen_color_label = QtWidgets.QLabel(self.image_compostion)
        self.choosen_color_label.setEnabled(True)
        self.choosen_color_label.setStyleSheet("background-color: rgb(255, 49, 59);\n"
"color: rgb(255, 0, 4);")
        self.choosen_color_label.setObjectName("choosen_color_label")
        self.horizontalLayout_6.addWidget(self.choosen_color_label)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.background_img_checkbox = QtWidgets.QCheckBox(self.image_compostion)
        self.background_img_checkbox.setEnabled(True)
        self.background_img_checkbox.setObjectName("background_img_checkbox")
        self.horizontalLayout_3.addWidget(self.background_img_checkbox)
        self.browse_bg_file_btn = QtWidgets.QPushButton(self.image_compostion)
        self.browse_bg_file_btn.setEnabled(False)
        self.browse_bg_file_btn.setObjectName("browse_bg_file_btn")
        self.horizontalLayout_3.addWidget(self.browse_bg_file_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.planets = QtWidgets.QLabel(self.image_compostion)
        self.planets.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.planets.setFont(font)
        self.planets.setObjectName("planets")
        self.verticalLayout_3.addWidget(self.planets)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.planet_list_table = QtWidgets.QListView(self.image_compostion)
        self.planet_list_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planet_list_table.sizePolicy().hasHeightForWidth())
        self.planet_list_table.setSizePolicy(sizePolicy)
        self.planet_list_table.setMaximumSize(QtCore.QSize(325, 83))
        self.planet_list_table.setObjectName("planet_list_table")
        self.horizontalLayout_7.addWidget(self.planet_list_table)
        self.widget = QtWidgets.QWidget(self.image_compostion)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.add_planet_btn = QtWidgets.QPushButton(self.widget)
        self.add_planet_btn.setStyleSheet("")
        self.add_planet_btn.setObjectName("add_planet_btn")
        self.verticalLayout_9.addWidget(self.add_planet_btn)
        self.edit_planet_btn = QtWidgets.QPushButton(self.widget)
        self.edit_planet_btn.setObjectName("edit_planet_btn")
        self.verticalLayout_9.addWidget(self.edit_planet_btn)
        self.delete_planet_btn = QtWidgets.QPushButton(self.widget)
        self.delete_planet_btn.setStyleSheet("")
        self.delete_planet_btn.setAutoDefault(False)
        self.delete_planet_btn.setDefault(False)
        self.delete_planet_btn.setObjectName("delete_planet_btn")
        self.verticalLayout_9.addWidget(self.delete_planet_btn)
        self.horizontalLayout_7.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.custom_config_checkbox = QtWidgets.QCheckBox(self.image_compostion)
        self.custom_config_checkbox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.custom_config_checkbox.setChecked(False)
        self.custom_config_checkbox.setObjectName("custom_config_checkbox")
        self.horizontalLayout_4.addWidget(self.custom_config_checkbox)
        self.browse_config_btn = QtWidgets.QPushButton(self.image_compostion)
        self.browse_config_btn.setEnabled(False)
        self.browse_config_btn.setObjectName("browse_config_btn")
        self.horizontalLayout_4.addWidget(self.browse_config_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.preview_label = QtWidgets.QLabel(self.image_compostion)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.preview_label.setFont(font)
        self.preview_label.setObjectName("preview_label")
        self.verticalLayout_3.addWidget(self.preview_label)
        self.graphicsView = QtWidgets.QGraphicsView(self.image_compostion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(100, 150))
        self.graphicsView.setMaximumSize(QtCore.QSize(9999, 150))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(self.image_compostion)
        self.dialog_buttons.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dialog_buttons.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.dialog_buttons.setCenterButtons(True)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.horizontalLayout.addWidget(self.dialog_buttons)
        self.save_yml_btn = QtWidgets.QPushButton(self.image_compostion)
        self.save_yml_btn.setText("")
        self.save_yml_btn.setObjectName("save_yml_btn")
        self.horizontalLayout.addWidget(self.save_yml_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.image_compostion, "")
        self.scheduler = QtWidgets.QWidget()
        self.scheduler.setObjectName("scheduler")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scheduler)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.scheduler)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.test_now_btn = QtWidgets.QPushButton(self.scheduler)
        self.test_now_btn.setObjectName("test_now_btn")
        self.gridLayout.addWidget(self.test_now_btn, 1, 1, 1, 1)
        self.create_schedueler_btn = QtWidgets.QPushButton(self.scheduler)
        self.create_schedueler_btn.setStyleSheet("color: rgb(0, 170, 0);")
        self.create_schedueler_btn.setObjectName("create_schedueler_btn")
        self.gridLayout.addWidget(self.create_schedueler_btn, 0, 0, 1, 1)
        self.delete_scheduler_btn = QtWidgets.QPushButton(self.scheduler)
        self.delete_scheduler_btn.setStyleSheet("color: rgb(255, 0, 4);")
        self.delete_scheduler_btn.setObjectName("delete_scheduler_btn")
        self.gridLayout.addWidget(self.delete_scheduler_btn, 0, 1, 1, 1)
        self.reload_scheduler_btn = QtWidgets.QPushButton(self.scheduler)
        self.reload_scheduler_btn.setObjectName("reload_scheduler_btn")
        self.gridLayout.addWidget(self.reload_scheduler_btn, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.label_4 = QtWidgets.QLabel(self.scheduler)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.status_label_color = QtWidgets.QLabel(self.scheduler)
        self.status_label_color.setStyleSheet("")
        self.status_label_color.setText("")
        self.status_label_color.setObjectName("status_label_color")
        self.horizontalLayout_8.addWidget(self.status_label_color)
        self.status_label_text = QtWidgets.QLabel(self.scheduler)
        font = QtGui.QFont()
        font.setItalic(True)
        self.status_label_text.setFont(font)
        self.status_label_text.setObjectName("status_label_text")
        self.horizontalLayout_8.addWidget(self.status_label_text)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.reload_status_btn = QtWidgets.QPushButton(self.scheduler)
        self.reload_status_btn.setText("")
        self.reload_status_btn.setObjectName("reload_status_btn")
        self.horizontalLayout_8.addWidget(self.reload_status_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.status_output = QtWidgets.QTextEdit(self.scheduler)
        self.status_output.setReadOnly(True)
        self.status_output.setPlaceholderText("")
        self.status_output.setObjectName("status_output")
        self.verticalLayout_6.addWidget(self.status_output)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.scheduler, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.close_btn = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.close_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout_2.addWidget(self.close_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.canvas_size.setBuddy(self.size_dropdown)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.custom_size_checkbox.toggled['bool'].connect(self.size_dropdown.setDisabled) # type: ignore
        self.custom_size_checkbox.toggled['bool'].connect(self.x_label.setEnabled) # type: ignore
        self.custom_size_checkbox.toggled['bool'].connect(self.y_label.setEnabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.planet_list_table.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.delete_planet_btn.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.edit_planet_btn.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.add_planet_btn.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.background_img_checkbox.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.custom_size_checkbox.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.size_dropdown.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.x_label.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.x_label.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.y_label.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.choose_color_btn.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.browse_bg_file_btn.setDisabled) # type: ignore
        self.choose_color_btn.toggled['bool'].connect(self.browse_bg_file_btn.setEnabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.browse_config_btn.setEnabled) # type: ignore
        self.background_img_checkbox.toggled['bool'].connect(self.browse_bg_file_btn.setEnabled) # type: ignore
        self.background_img_checkbox.toggled['bool'].connect(self.choose_color_btn.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.choosen_color_label.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.planets.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.background_color.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.canvas_size.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.x_value_input.setDisabled) # type: ignore
        self.custom_config_checkbox.toggled['bool'].connect(self.y_value_input.setDisabled) # type: ignore
        self.custom_size_checkbox.toggled['bool'].connect(self.x_value_input.setEnabled) # type: ignore
        self.custom_size_checkbox.toggled['bool'].connect(self.y_value_input.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.size_dropdown)
        MainWindow.setTabOrder(self.size_dropdown, self.custom_size_checkbox)
        MainWindow.setTabOrder(self.custom_size_checkbox, self.background_img_checkbox)
        MainWindow.setTabOrder(self.background_img_checkbox, self.custom_config_checkbox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.image_compostion.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.canvas_size.setText(_translate("MainWindow", "Canvas size:"))
        self.size_dropdown.setItemText(0, _translate("MainWindow", "1920x1080"))
        self.size_dropdown.setItemText(1, _translate("MainWindow", "640x360"))
        self.custom_size_checkbox.setText(_translate("MainWindow", "Custom size"))
        self.x_label.setText(_translate("MainWindow", "x:"))
        self.y_label.setText(_translate("MainWindow", "y:"))
        self.size_error_label.setText(_translate("MainWindow", "invalid size!"))
        self.background_color.setText(_translate("MainWindow", "Background Color:"))
        self.choose_color_btn.setText(_translate("MainWindow", "Choose color"))
        self.choosen_color_label.setText(_translate("MainWindow", "__________"))
        self.background_img_checkbox.setText(_translate("MainWindow", "Background Image"))
        self.browse_bg_file_btn.setText(_translate("MainWindow", "Browse image file"))
        self.planets.setText(_translate("MainWindow", "Planets:"))
        self.add_planet_btn.setText(_translate("MainWindow", "Add"))
        self.edit_planet_btn.setText(_translate("MainWindow", "Edit"))
        self.delete_planet_btn.setText(_translate("MainWindow", "Delete"))
        self.custom_config_checkbox.setText(_translate("MainWindow", "custom config"))
        self.browse_config_btn.setText(_translate("MainWindow", "Browse config file"))
        self.preview_label.setText(_translate("MainWindow", "Preview:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_compostion), _translate("MainWindow", "Image composition"))
        self.label.setText(_translate("MainWindow", "Manage:"))
        self.test_now_btn.setText(_translate("MainWindow", "Test now"))
        self.create_schedueler_btn.setText(_translate("MainWindow", "Create New Scheduler"))
        self.delete_scheduler_btn.setText(_translate("MainWindow", "Delete Scheduler"))
        self.reload_scheduler_btn.setText(_translate("MainWindow", "Reset Schedluer"))
        self.label_4.setText(_translate("MainWindow", "Status:"))
        self.status_label_text.setText(_translate("MainWindow", "Running"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scheduler), _translate("MainWindow", "Scheduler"))
