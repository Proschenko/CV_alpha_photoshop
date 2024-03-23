import numpy as np
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, qRgb, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QApplication, QMessageBox, QMenu, \
    QToolButton, QAction
from PyQt5 import QtCore, QtWidgets
from PIL import Image, ImageFilter, ImageEnhance
from GraphView import GraphView

from PreprocessingIMG import Preprocessing_IMG


class Ui_MainWindow(object):
    def __init__(self):
        self.show_frame = True  # Флаг для отображения рамки
        self.sepia_filters = [
            np.array([[0.393, 0.769, 0.189],
                      [0.349, 0.686, 0.168],
                      [0.272, 0.534, 0.131]]),
            np.array([[0.393, 0.769, 0.189],
                      [0.272, 0.534, 0.131],
                      [0.168, 0.686, 0.349]]),
            np.array([[0.272, 0.534, 0.131],
                      [0.393, 0.769, 0.189],
                      [0.168, 0.686, 0.349]])
        ]
        self.current_sepia_index = 0
        self.flag_LA_picture = False
    def setupUi(self, MainWindow):
        #region base
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 221, 121))
        self.groupBox.setObjectName("groupBox")
        self.button_download_img = QtWidgets.QPushButton(self.groupBox)
        self.button_download_img.setGeometry(QtCore.QRect(10, 40, 161, 28))
        self.button_download_img.setObjectName("button_download_img")
        self.button_save_img = QtWidgets.QPushButton(self.groupBox)
        self.button_save_img.setGeometry(QtCore.QRect(10, 80, 201, 28))
        self.button_save_img.setObjectName("button_save_img")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 40, 31, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 221, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_grey_img_R = QtWidgets.QPushButton(self.groupBox_2)
        self.button_grey_img_R.setGeometry(QtCore.QRect(10, 40, 201, 28))
        self.button_grey_img_R.setObjectName("button_grey_img_R")
        self.button_grey_img_G = QtWidgets.QPushButton(self.groupBox_2)
        self.button_grey_img_G.setGeometry(QtCore.QRect(10, 80, 201, 28))
        self.button_grey_img_G.setObjectName("button_grey_img_G")
        self.button_grey_img_B = QtWidgets.QPushButton(self.groupBox_2)
        self.button_grey_img_B.setGeometry(QtCore.QRect(10, 120, 201, 28))
        self.button_grey_img_B.setObjectName("button_grey_img_B")
        self.button_grey_img_RGB_mean = QtWidgets.QPushButton(self.groupBox_2)
        self.button_grey_img_RGB_mean.setGeometry(QtCore.QRect(10, 160, 201, 28))
        self.button_grey_img_RGB_mean.setObjectName("button_grey_img_RGB_mean")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 370, 221, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.slider_intensive_B = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_B.setGeometry(QtCore.QRect(40, 180, 161, 22))
        self.slider_intensive_B.setMinimum(-100)
        self.slider_intensive_B.setMaximum(100)
        self.slider_intensive_B.setProperty("value", 0)
        self.slider_intensive_B.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_B.setObjectName("slider_intensive_B")
        self.slider_intensive_G = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_G.setGeometry(QtCore.QRect(40, 150, 161, 22))
        self.slider_intensive_G.setMinimum(-100)
        self.slider_intensive_G.setMaximum(100)
        self.slider_intensive_G.setProperty("value", 0)
        self.slider_intensive_G.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_G.setObjectName("slider_intensive_G")
        self.slider_intensive_R = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_R.setGeometry(QtCore.QRect(40, 120, 161, 21))
        self.slider_intensive_R.setMinimum(-100)
        self.slider_intensive_R.setMaximum(100)
        self.slider_intensive_R.setProperty("value", 0)
        self.slider_intensive_R.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_R.setObjectName("slider_intensive_R")
        self.slider_intensive_all = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_all.setGeometry(QtCore.QRect(10, 61, 191, 20))
        self.slider_intensive_all.setMinimum(-100)
        self.slider_intensive_all.setMaximum(100)
        self.slider_intensive_all.setProperty("value", 0)
        self.slider_intensive_all.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_all.setObjectName("slider_intensive_all")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 221, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 16, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 16, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 16, 21))
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 730, 221, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.slider_contrast = QtWidgets.QSlider(self.groupBox_4)
        self.slider_contrast.setGeometry(QtCore.QRect(10, 30, 201, 22))
        self.slider_contrast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slider_contrast.setMinimum(-100)
        self.slider_contrast.setMaximum(100)
        self.slider_contrast.setProperty("value", 0)
        self.slider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contrast.setInvertedAppearance(False)
        self.slider_contrast.setInvertedControls(False)
        self.slider_contrast.setObjectName("slider_contrast")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 600, 221, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.button_flip_vertical = QtWidgets.QPushButton(self.groupBox_5)
        self.button_flip_vertical.setGeometry(QtCore.QRect(20, 30, 171, 28))
        self.button_flip_vertical.setObjectName("button_flip_vertical")
        self.button_flip_horizontal = QtWidgets.QPushButton(self.groupBox_5)
        self.button_flip_horizontal.setGeometry(QtCore.QRect(20, 70, 171, 28))
        self.button_flip_horizontal.setObjectName("button_flip_horizontal")
        self.text_output_console = QtWidgets.QTextEdit(self.centralwidget)
        self.text_output_console.setGeometry(QtCore.QRect(940, 220, 291, 91))
        self.text_output_console.setObjectName("text_output_console")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(260, 600, 211, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.button_negative_R = QtWidgets.QPushButton(self.groupBox_6)
        self.button_negative_R.setGeometry(QtCore.QRect(10, 40, 191, 28))
        self.button_negative_R.setObjectName("button_negative_R")
        self.button_negative_G = QtWidgets.QPushButton(self.groupBox_6)
        self.button_negative_G.setGeometry(QtCore.QRect(10, 80, 191, 28))
        self.button_negative_G.setObjectName("button_negative_G")
        self.button_negative_B = QtWidgets.QPushButton(self.groupBox_6)
        self.button_negative_B.setGeometry(QtCore.QRect(10, 120, 191, 28))
        self.button_negative_B.setObjectName("button_negative_B")
        self.button_negative_all = QtWidgets.QPushButton(self.groupBox_6)
        self.button_negative_all.setGeometry(QtCore.QRect(10, 160, 191, 28))
        self.button_negative_all.setObjectName("button_negative_all")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(490, 600, 191, 201))
        self.groupBox_7.setObjectName("groupBox_7")
        self.button_swap_R_G = QtWidgets.QPushButton(self.groupBox_7)
        self.button_swap_R_G.setGeometry(QtCore.QRect(20, 50, 151, 31))
        self.button_swap_R_G.setObjectName("button_swap_R_G")
        self.button_swap_R_B = QtWidgets.QPushButton(self.groupBox_7)
        self.button_swap_R_B.setGeometry(QtCore.QRect(20, 87, 151, 31))
        self.button_swap_R_B.setObjectName("button_swap_R_B")
        self.button_swap_B_G = QtWidgets.QPushButton(self.groupBox_7)
        self.button_swap_B_G.setGeometry(QtCore.QRect(20, 130, 151, 28))
        self.button_swap_B_G.setObjectName("button_swap_B_G")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(700, 600, 211, 201))
        self.groupBox_8.setObjectName("groupBox_8")
        self.radio_mean_value = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_mean_value.setGeometry(QtCore.QRect(20, 30, 151, 31))
        self.radio_mean_value.setChecked(True)
        self.radio_mean_value.setObjectName("radio_mean_value")
        self.radio_model_4 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_model_4.setGeometry(QtCore.QRect(20, 69, 151, 31))
        self.radio_model_4.setChecked(False)
        self.radio_model_4.setObjectName("radio_model_4")
        self.radio_model_8 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_model_8.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.radio_model_8.setObjectName("radio_model_8")
        self.button_blur_accept = QtWidgets.QPushButton(self.groupBox_8)
        self.button_blur_accept.setGeometry(QtCore.QRect(40, 150, 111, 28))
        self.button_blur_accept.setObjectName("button_blur_accept")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(970, 320, 231, 481))
        self.groupBox_10.setObjectName("groupBox_10")
        self.button_graph_show = QtWidgets.QPushButton(self.groupBox_10)
        self.button_graph_show.setGeometry(QtCore.QRect(20, 440, 191, 28))
        self.button_graph_show.setObjectName("button_graph_show")
        self.check_box_hist_intensive = QtWidgets.QCheckBox(self.groupBox_10)
        self.check_box_hist_intensive.setGeometry(QtCore.QRect(20, 30, 191, 20))
        self.check_box_hist_intensive.setObjectName("check_box_hist_intensive")
        self.check_box_hist_RGB = QtWidgets.QCheckBox(self.groupBox_10)
        self.check_box_hist_RGB.setGeometry(QtCore.QRect(20, 60, 191, 21))
        self.check_box_hist_RGB.setObjectName("check_box_hist_RGB")
        self.check_box_profile_intensive_str = QtWidgets.QCheckBox(self.groupBox_10)
        self.check_box_profile_intensive_str.setGeometry(QtCore.QRect(10, 250, 191, 20))
        self.check_box_profile_intensive_str.setObjectName("check_box_profile_intensive_str")
        self.check_box_map_contrast = QtWidgets.QCheckBox(self.groupBox_10)
        self.check_box_map_contrast.setGeometry(QtCore.QRect(20, 90, 191, 20))
        self.check_box_map_contrast.setObjectName("check_box_map_contrast")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 120, 211, 121))
        self.groupBox_9.setObjectName("groupBox_9")
        self.radio_formula_4n = QtWidgets.QRadioButton(self.groupBox_9)
        self.radio_formula_4n.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.radio_formula_4n.setChecked(True)
        self.radio_formula_4n.setObjectName("radio_formula_4n")
        self.radio_formula_8n = QtWidgets.QRadioButton(self.groupBox_9)
        self.radio_formula_8n.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.radio_formula_8n.setObjectName("radio_formula_8n")
        self.radio_formula_window_n_n = QtWidgets.QRadioButton(self.groupBox_9)
        self.radio_formula_window_n_n.setGeometry(QtCore.QRect(10, 60, 181, 21))
        self.radio_formula_window_n_n.setObjectName("radio_formula_window_n_n")
        self.spin_box_n_for_formula = QtWidgets.QSpinBox(self.groupBox_9)
        self.spin_box_n_for_formula.setGeometry(QtCore.QRect(150, 90, 42, 21))
        self.spin_box_n_for_formula.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_box_n_for_formula.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_box_n_for_formula.setObjectName("spin_box_n_for_formula")
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_6.setGeometry(QtCore.QRect(70, 90, 81, 21))
        self.label_6.setObjectName("label_6")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 280, 211, 61))
        self.groupBox_11.setObjectName("groupBox_11")
        self.spin_box_profile_intensive_num_str = QtWidgets.QSpinBox(self.groupBox_11)
        self.spin_box_profile_intensive_num_str.setGeometry(QtCore.QRect(20, 30, 171, 22))
        self.spin_box_profile_intensive_num_str.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_box_profile_intensive_num_str.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_box_profile_intensive_num_str.setMinimum(1)
        self.spin_box_profile_intensive_num_str.setMaximum(561)
        self.spin_box_profile_intensive_num_str.setObjectName("spin_box_profile_intensive_num_str")
        self.check_box_profile_colomn = QtWidgets.QCheckBox(self.groupBox_10)
        self.check_box_profile_colomn.setGeometry(QtCore.QRect(10, 341, 191, 20))
        self.check_box_profile_colomn.setObjectName("check_box_profile_colomn")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 370, 211, 61))
        self.groupBox_12.setObjectName("groupBox_12")
        self.spin_box_profile_intensive_num_colomn = QtWidgets.QSpinBox(self.groupBox_12)
        self.spin_box_profile_intensive_num_colomn.setGeometry(QtCore.QRect(20, 30, 171, 22))
        self.spin_box_profile_intensive_num_colomn.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_box_profile_intensive_num_colomn.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_box_profile_intensive_num_colomn.setMinimum(1)
        self.spin_box_profile_intensive_num_colomn.setMaximum(661)
        self.spin_box_profile_intensive_num_colomn.setObjectName("spin_box_profile_intensive_num_colomn")
        self.tool_button_type_shape = QtWidgets.QToolButton(self.centralwidget)
        self.tool_button_type_shape.setGeometry(QtCore.QRect(1130, 30, 50, 50))
        self.tool_button_type_shape.setObjectName("tool_button_type_shape")
        self.button_sepia = QtWidgets.QPushButton(self.centralwidget)
        self.button_sepia.setGeometry(QtCore.QRect(1120, 150, 111, 51))
        self.button_sepia.setObjectName("button_sepia")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #endregion

        # Заменяем QGraphicsView на QLabel для отображения основного изображения
        self.view_main_window = QLabel(self.centralwidget)
        self.view_main_window.setGeometry(QtCore.QRect(256, 30, 661, 561))
        self.view_main_window.setObjectName("view_main_window")

        self.view_main_window.setMouseTracking(True)  # Включаем отслеживание движения мыши
        self.view_main_window.setStyleSheet("border: 1px solid black;")  # Добавляем рамку

        # Заменяем QGraphicsView на QLabel для отображения увеличенной версии пикселя
        self.view_small_square = QLabel(self.centralwidget)
        self.view_small_square.setGeometry(QtCore.QRect(940, 30, 170, 170))
        self.view_small_square.setScaledContents(True)
        self.view_small_square.setObjectName("view_small_square")
        self.view_small_square.setStyleSheet("border: 1px solid black;")  # Добавляем рамку

        self.feature_color()

        #region fields
        self.image_path = None #Рабочее пространство
        self.original_path = None #Исходник
        self.original_pixmap = None  # Сохраняем оригинальное изображение

        self.color_pen_shape = Qt.yellow
        self.size_shape = None
        #endregion


        #region action
        self.button_download_img.clicked.connect(self.handle_load_image)
        self.button_save_img.clicked.connect(self.handle_save_image)
        self.pushButton.clicked.connect(self.handle_reload_image)

        #region grey DONE
        self.button_grey_img_R.clicked.connect(lambda: self.button_grey_img_clicked('red'))
        self.button_grey_img_G.clicked.connect(lambda: self.button_grey_img_clicked('green'))
        self.button_grey_img_B.clicked.connect(lambda: self.button_grey_img_clicked('blue'))
        self.button_grey_img_RGB_mean.clicked.connect(lambda: self.button_grey_img_clicked('rgb_mean'))

        #endregion

        # region negative
        self.button_negative_R.clicked.connect(self.button_negative_R_clicked)
        self.button_negative_B.clicked.connect(self.button_negative_B_clicked)
        self.button_negative_G.clicked.connect(self.button_negative_G_clicked)
        self.button_negative_all.clicked.connect(self.button_negative_all_clicked)
        # endregion

        # region swap chanel DONE
        self.button_swap_R_B.clicked.connect(self.button_swap_R_B_clicked)
        self.button_swap_R_G.clicked.connect(self.button_swap_R_G_clicked)
        self.button_swap_B_G.clicked.connect(self.button_swap_B_G_clicked)
        # endregion

        #region IMG flip DONE
        self.button_flip_vertical.clicked.connect(self.button_flip_vertical_clicked)
        self.button_flip_horizontal.clicked.connect(self.button_flip_horizontal_clicked)
        #endregion

        #region blur
        self.button_blur_accept.clicked.connect(self.button_blur_accept_clicked)
        #endregion

        #region contrast
        self.slider_contrast.valueChanged.connect(self.update_img)
        #endregion

        #region intensive
        self.slider_intensive_R.sliderReleased.connect(self.update_img)
        self.slider_intensive_G.sliderReleased.connect(self.update_img)
        self.slider_intensive_B.sliderReleased.connect(self.update_img)
        self.slider_intensive_all.sliderReleased.connect(self.update_img)
        #endregion

        #region sepia
        self.button_sepia.clicked.connect(self.apply_sepia)
        #endregion
        #region graph hist map
        self.button_graph_show.clicked.connect(self.button_show_graph_clicked)

        #endregion
        # Подключаем обработчик события мыши для отслеживания движения
        self.view_main_window.mouseMoveEvent = self.mouseMoveEvent

    # region feature
    def feature_color(self):
        self.tool_button_type_shape.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_button_type_shape.setIcon(QIcon("icons/Желтый.png"))

        menu = QMenu(self.tool_button_type_shape)
        self.tool_button_type_shape.setMenu(menu)

        self.addIconAction(menu, "Желтый", "icons/Желтый.png", Qt.yellow)
        self.addIconAction(menu, "Красный", "icons/Красный.png", Qt.red)
        self.addIconAction(menu, "Зеленый", "icons/Зеленый.png", Qt.green)
        self.addIconAction(menu, "Черный", "icons/Черный.png", Qt.black)
        self.addIconAction(menu, "Белый", "icons/Черный.png", Qt.white)

    def addIconAction(self, menu, name, icon_path, color):
        action = QAction(QIcon(icon_path), name, menu)
        action.triggered.connect(lambda checked, color=color: self.onActionTriggered(color))
        menu.addAction(action)

    def onActionTriggered(self, color):
        self.color_pen_shape = color
        # Устанавливаем иконку соответствующего цвета на кнопку
        if color == Qt.yellow:
            self.tool_button_type_shape.setIcon(QIcon("icons/Желтый.png"))
        elif color == Qt.red:
            self.tool_button_type_shape.setIcon(QIcon("icons/Красный.png"))
        elif color == Qt.green:
            self.tool_button_type_shape.setIcon(QIcon("icons/Зеленый.png"))
        elif color == Qt.black:
            self.tool_button_type_shape.setIcon(QIcon("icons/Черный.png"))
        elif color == Qt.white:
            self.tool_button_type_shape.setIcon(QIcon("icons/Черный.png"))

    # endregion



    #region load

    def set_default_value_slider(self):
        self.slider_contrast.setProperty("value", 0)
        self.slider_intensive_B.setProperty("value",0)
        self.slider_intensive_R.setProperty("value",0)
        self.slider_intensive_G.setProperty("value",0)
        self.slider_intensive_all.setProperty("value",0)

        self.button_sepia.setText("Click me pls")

    def handle_load_image(self):
        # Диалоговое окно выбора файла для загрузки изображения
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выбрать изображение", "",
                                                            "Images (*.png *.tiff *.bmp)")

        if filename:  # Если пользователь выбрал файл
            # Вызываем метод из модуля Preprocessing_IMG для изменения размера и сохранения изображения
            self.original_path = filename
            resized_image_path = Preprocessing_IMG.resize_and_save_image(filename)
            self.image_path = resized_image_path

            if resized_image_path:
                self.set_default_value_slider()
                # Загружаем изображение на QLabel из папки Temp
                pixmap = QPixmap(resized_image_path)
                self.original_pixmap = pixmap.copy()  # Сохраняем оригинальное изображение
                self.view_main_window.setPixmap(pixmap)  # Отображаем изображение на основном QLabel

    def handle_reload_image(self):
        if  self.original_path is not None:
            resized_image_path = Preprocessing_IMG.resize_and_save_image(self.original_path)
            self.image_path = resized_image_path

            if resized_image_path:
                self.set_default_value_slider()
                # Загружаем изображение на QLabel из папки Temp
                pixmap = QPixmap(resized_image_path)
                self.original_pixmap = pixmap.copy()  # Сохраняем оригинальное изображение
                self.view_main_window.setPixmap(pixmap)  # Отображаем изображение на основном QLabel

    def handle_save_image(self):
        # Получаем изображение из QLabel
        self.show_frame = False
        pixmap = self.view_main_window.pixmap()
        if pixmap is None:
            # Если QLabel пустой, выходим из метода
            return

        # Получаем родительский виджет (окно) для QLabel
        parent_widget = self.view_main_window.window()

        # Открываем диалоговое окно сохранения файла
        file_path, _ = QFileDialog.getSaveFileName(parent_widget, "Сохранить изображение", "",
                                                   "Images (*.png *.jpg *.bmp)")

        pixmap=self.update_img()
        if file_path:
            # Сохраняем изображение
            pixmap.save(file_path)
        self.show_frame = True


    def update_img(self):
        # Загружаем изображение в QPixmap
        if (self.image_path != None):

            # Получаем значения яркости и контрастности из слайдеров
            intensity_R = self.slider_intensive_R.value()
            intensity_G = self.slider_intensive_G.value()
            intensity_B = self.slider_intensive_B.value()
            intensity_all = self.slider_intensive_all.value()
            contrast = self.slider_contrast.value()

            # Применяем настройки яркости и контрастности к изображению
            pixmap = self.apply_brightness_contrast(self.image_path, intensity_R, intensity_G, intensity_B, intensity_all,
                                               contrast)
            self.original_pixmap = pixmap.copy()  # Сохраняем оригинальное изображение

            # Обновляем изображение на QLabel
            self.view_main_window.setPixmap(pixmap)
            return pixmap
        else:
            self.show_error_message("Ошибка", "Отсутствует изображение")
            return  None


    #endregion

    #region sepia
    def apply_sepia(self):
        if self.image_path is not None:
            img = Image.open(self.image_path)

            if img.mode == 'RGBA':
                img = img.convert('RGB')

            self.current_sepia_index = (self.current_sepia_index + 1) % len(self.sepia_filters)
            img = self.sepia_filter(img, self.sepia_filters[self.current_sepia_index])

            sepia_name = f"Сепия {self.current_sepia_index + 1}"
            self.button_sepia.setText(sepia_name)

            output_path = self.image_path
            img.save(output_path)

            self.update_img()

    def sepia_filter(self, img, sepia_filter):
        # Применяем фильтр сепии к изображению
        img_array = np.array(img)
        sepia_img_array = np.dot(img_array, sepia_filter.T).clip(0, 255).astype(np.uint8)
        sepia_img = Image.fromarray(sepia_img_array)
        return sepia_img

    #endregion

    #region intensive and contrast


    def apply_brightness_contrast(self, image_path, brightness_R, brightness_G, brightness_B, brightness_all, contrast):

        # Загрузить изображение из файла
        image = QImage(image_path)

        # Преобразовать QImage в массив NumPy
        width = image.width()
        height = image.height()
        bytes_per_line = image.bytesPerLine()
        img_data = image.bits().asarray(height * bytes_per_line)
        img_np = np.frombuffer(img_data, dtype=np.uint8).reshape((height, width, 4))

        # Применить настройки яркости и контрастности
        img_np = self.apply_brightness(img_np, brightness_R, brightness_G, brightness_B, brightness_all)
        img_np = self.apply_contrast(img_np, contrast)

        # Преобразовать массив NumPy обратно в изображение PIL
        img_pil = Image.fromarray(img_np)

        # Преобразовать изображение PIL в QPixmap для отображения на QLabel
        pixmap = QPixmap.fromImage(
            QImage(img_pil.tobytes(), img_pil.width, img_pil.height, img_pil.width * 4, QImage.Format_ARGB32))

        return pixmap
    @staticmethod
    def apply_brightness(image_np, brightness_R, brightness_G, brightness_B, brightness_all):
        # Применить яркость к каждому каналу RGB
        image_np[..., 0] = np.clip(image_np[..., 0] + brightness_R, 0, 255).astype(np.uint8)
        image_np[..., 1] = np.clip(image_np[..., 1] + brightness_G, 0, 255).astype(np.uint8)
        image_np[..., 2] = np.clip(image_np[..., 2] + brightness_B, 0, 255).astype(np.uint8)
        image_np[..., :3] = np.clip(image_np[..., :3] + brightness_all, 0, 255).astype(np.uint8)
        return image_np

    @staticmethod
    def apply_contrast(image_np, contrast):
        # Применить контрастность к каждому каналу RGB
        alpha = (contrast + 100) / 100
        image_np[..., :3] = (image_np[..., :3] - 127.5) * alpha + 127.5
        # Ограничить значения в диапазоне от 0 до 255
        np.clip(image_np[..., :3], 0, 255, out=image_np[..., :3])
        return image_np

    #endregion

    #region IMG shape
    def mouseMoveEvent(self, event):
        # Получаем текущие координаты курсора
        if self.show_frame:
            cursor_position = event.pos()

            # Обновляем изображение и рамку в виджетах
            self.update_display(cursor_position)

    def update_display(self, cursor_position):
        if self.original_pixmap is not None:
            image_width = self.original_pixmap.width()
            image_height = self.original_pixmap.height()

            # Проверяем, находится ли курсор внутри изображения
            if 0 <= cursor_position.x() < image_width and 0 <= cursor_position.y() < image_height:
                # Создаем новый объект QPixmap для редактирования
                pixmap_copy = QPixmap(self.original_pixmap)

                # Создаем объект QPainter для рисования рамки
                painter = QPainter(pixmap_copy)
                painter.setPen(QPen(self.color_pen_shape, 2))  # Устанавливаем желтую рамку толщиной 2 пикселя
                frame_size = 13  # Размер рамки (13 на 13 пикселей)

                # Получаем координаты верхнего левого угла рамки
                top_left_corner = cursor_position - QPoint(frame_size // 2, frame_size // 2)

                # Проверяем, чтобы рамка не выходила за пределы изображения
                if top_left_corner.x() < 0:
                    top_left_corner.setX(0)
                if top_left_corner.y() < 0:
                    top_left_corner.setY(0)
                if top_left_corner.x() + frame_size > image_width:
                    top_left_corner.setX(image_width - frame_size)
                if top_left_corner.y() + frame_size > image_height:
                    top_left_corner.setY(image_height - frame_size)

                # Рисуем рамку вокруг курсора
                painter.drawRect(top_left_corner.x(), top_left_corner.y(), frame_size, frame_size)

                # Завершаем рисование
                painter.end()

                # Устанавливаем отредактированное изображение в основное окно
                self.view_main_window.setPixmap(pixmap_copy)

                # Обрезаем изображение для маленького окна (11x11 пикселей вокруг курсора)
                small_image = self.original_pixmap.copy(top_left_corner.x(), top_left_corner.y(), frame_size,
                                                        frame_size)
                self.view_small_square.setPixmap(small_image)

                # Получаем значения пикселей
                pixels = small_image.toImage().bits().asstring(frame_size * frame_size * 4)
                img = np.frombuffer(pixels, dtype=np.uint8).reshape((frame_size, frame_size, 4))

                # Вычисляем необходимые показатели
                rgb_values = img[..., :3]  # Извлекаем только RGB значения
                rgba_values_center_pix=rgb_values[6,6]

                intensity_center_pix = np.mean(rgba_values_center_pix)  # Вычисляем интенсивность пикселя центрального

                intensity = np.mean(rgb_values)

                std_deviation = np.std(np.mean(rgb_values,axis=2)) # Вычисляем стандартное отклонение


                # Округляем значения до двух знаков после запятой
                intensity = round(intensity, 2)
                intensity_center_pix = round(intensity_center_pix, 2)
                std_deviation = round(std_deviation, 2)

                # Отображаем значения в text_output_console
                self.text_output_console.setText(
                    f"Координаты: ({cursor_position.x()}, {cursor_position.y()})\n"
                    f"RGB: {rgba_values_center_pix[::-1]}\n"
                    f"Интенсивность: {intensity_center_pix}\n"
                    f"Средняя интенсивность: {intensity}\n"
                    f"Стандартное отклонение: {std_deviation}"
                )
            else:
                pass

    #endregion

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DoubleATeam_CV_lab_1"))
        self.groupBox.setTitle(_translate("MainWindow", "Изображение"))
        self.button_download_img.setText(_translate("MainWindow", "Загрузить"))
        self.button_save_img.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton.setText(_translate("MainWindow", "↻"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ч/Б фильтр"))
        self.button_grey_img_R.setText(_translate("MainWindow", "Красный канал"))
        self.button_grey_img_G.setText(_translate("MainWindow", "Зеленый канал"))
        self.button_grey_img_B.setText(_translate("MainWindow", "Синий канал"))
        self.button_grey_img_RGB_mean.setText(_translate("MainWindow", "Усредненное RGB"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Интенсивность яркости"))
        self.label.setText(_translate("MainWindow", "Общая яркость"))
        self.label_2.setText(_translate("MainWindow", "Якрость опредленного канала"))
        self.label_3.setText(_translate("MainWindow", "R"))
        self.label_4.setText(_translate("MainWindow", "G"))
        self.label_5.setText(_translate("MainWindow", "B"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Контрастность"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Отражение"))
        self.button_flip_vertical.setText(_translate("MainWindow", "По вертикали"))
        self.button_flip_horizontal.setText(_translate("MainWindow", "По горизонтали"))
        self.text_output_console.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Негатив"))
        self.button_negative_R.setText(_translate("MainWindow", "Красный канал"))
        self.button_negative_G.setText(_translate("MainWindow", "Зеленый канал"))
        self.button_negative_B.setText(_translate("MainWindow", "Синий канал"))
        self.button_negative_all.setText(_translate("MainWindow", "Яркости"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Обмен цветовых каналов"))
        self.button_swap_R_G.setText(_translate("MainWindow", "R и G"))
        self.button_swap_R_B.setText(_translate("MainWindow", "R и B"))
        self.button_swap_B_G.setText(_translate("MainWindow", "B и G"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Размытие"))
        self.radio_mean_value.setText(_translate("MainWindow", "Средним значением"))
        self.radio_model_4.setText(_translate("MainWindow", "Модель 4-связности"))
        self.radio_model_8.setText(_translate("MainWindow", "Модель 8-связности"))
        self.button_blur_accept.setText(_translate("MainWindow", "Применить"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Графики"))
        self.button_graph_show.setText(_translate("MainWindow", "Показать"))
        self.check_box_hist_intensive.setText(_translate("MainWindow", "Гистограмма яркости"))
        self.check_box_hist_RGB.setText(_translate("MainWindow", "Гистограмма RGB"))
        self.check_box_profile_intensive_str.setText(_translate("MainWindow", "Профиль яркости (строка)"))
        self.check_box_map_contrast.setText(_translate("MainWindow", "Карта контрасности"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Выбрать рассчетную формулу"))
        self.radio_formula_4n.setText(_translate("MainWindow", "По 4 соседям"))
        self.radio_formula_8n.setText(_translate("MainWindow", "По 8 соседям"))
        self.radio_formula_window_n_n.setText(_translate("MainWindow", "По окну с значением n*n"))
        self.label_6.setText(_translate("MainWindow", "Значение n:"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Выберите строку"))
        self.check_box_profile_colomn.setText(_translate("MainWindow", "Профиль яркости (столбец)"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Выберите Столбец"))
        self.tool_button_type_shape.setText(_translate("MainWindow", "..."))
        self.button_sepia.setText(_translate("MainWindow", "Click me pls"))
        self.action.setText(_translate("MainWindow", "Загрузить"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))

    # region grey DONE

    def button_grey_img_clicked(self, channel):
        if self.image_path is not None:

            input_path = self.image_path
            output_path= self.image_path

            if channel == 'rgb_mean':
                grayscale_img = self.grayscale_average(input_path)
                grayscale_img.save(output_path)
            else:
                channel_img = self.extract_channel(input_path, channel)
                channel_img.save(output_path)

            self.update_img()
            print("Изображение успешно сохранено:", output_path)

    def extract_channel(self, image_path, channel='red'):
        img = Image.open(image_path)
        img = img.convert('RGBA')
        if channel == 'red':
            r, _, _, _ = img.split()
            return r
        elif channel == 'green':
            _, g, _, _ = img.split()
            return g
        elif channel == 'blue':
            _, _, b, _ = img.split()
            return b
        else:
            print("Invalid channel name")
            return None

    def grayscale_average(self, image_path):
        img = Image.open(image_path)
        img = img.convert('RGBA')  # Используем RGBA для поддержки прозрачности
        grayscale_img = img.convert('L')  # Конвертируем в оттенки серого
        return grayscale_img
    # endregion

    #region negative

    def button_negative_R_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию",
                                        "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:
                r, g, b = img.split()
                a = None

            r_negative = Image.eval(r, lambda x: 255 - x)
            if a:  # альфа-канал существует
                img_negative = Image.merge(img.mode, (r_negative, g, b, a))
            else:  # альфа-канал отсутствует
                img_negative = Image.merge(img.mode, (r_negative, g, b))
            img_negative.save(output_path)

            self.update_img()

    def button_negative_G_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию",
                                        "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
                a = None  # устанавливаем a в None, чтобы в дальнейшем при объединении каналов не возникало ошибок

            g_negative = Image.eval(g, lambda x: 255 - x)
            if a:  # Если альфа-канал существует
                img_negative = Image.merge(img.mode, (r, g_negative, b, a))
            else:  # Если альфа-канал отсутствует
                img_negative = Image.merge(img.mode, (r, g_negative, b))
            img_negative.save(output_path)

            self.update_img()

    def button_negative_B_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию",
                                        "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
                a = None  # устанавливаем a в None, чтобы в дальнейшем при объединении каналов не возникало ошибок

            b_negative = Image.eval(b, lambda x: 255 - x)
            if a:  # Если альфа-канал существует
                img_negative = Image.merge(img.mode, (r, g, b_negative, a))
            else:  # Если альфа-канал отсутствует
                img_negative = Image.merge(img.mode, (r, g, b_negative))
            img_negative.save(output_path)

            self.update_img()

    def button_negative_all_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию",
                                        "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
                a = None  # устанавливаем a в None, чтобы в дальнейшем при объединении каналов не возникало ошибок

            r_negative = Image.eval(r, lambda x: 255 - x)
            g_negative = Image.eval(g, lambda x: 255 - x)
            b_negative = Image.eval(b, lambda x: 255 - x)
            if a:  # Если альфа-канал существует
                img_negative = Image.merge(img.mode, (r_negative, g_negative, b_negative, a))
            else:  # Если альфа-канал отсутствует
                img_negative = Image.merge(img.mode, (r_negative, g_negative, b_negative))
            img_negative.save(output_path)

            self.update_img()

    #endregion

    #region IMG FLIP DONE
    @staticmethod
    def flip_vertical_custom(image):
        width, height = image.size
        pixels = image.load()

        for x in range(width):
            for y in range(height // 2):
                temp = pixels[x, y]
                pixels[x, y] = pixels[x, height - 1 - y]
                pixels[x, height - 1 - y] = temp

        return image
    @staticmethod
    def flip_horizontal_custom(image):
        width, height = image.size
        pixels = image.load()

        for y in range(height):
            for x in range(width // 2):
                temp = pixels[x, y]
                pixels[x, y] = pixels[width - 1 - x, y]
                pixels[width - 1 - x, y] = temp

        return image

    def button_flip_vertical_clicked(self):
        if self.image_path is not None:
            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            img_flipped = self.flip_vertical_custom(img)  # Используем собственную реализацию
            img_flipped.save(output_path)
            self.update_img()

    def button_flip_horizontal_clicked(self):
        if self.image_path is not None:
            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            img_flipped = self.flip_horizontal_custom(img)  # Используем собственную реализацию
            img_flipped.save(output_path)
            self.update_img()

    #endregion

    #region SWAP CHANEL RGB DONE

    def button_swap_R_G_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию", "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
            img_swapped = Image.merge("RGB", (g, r, b))
            img_swapped.save(output_path)

            self.update_img()

    def button_swap_R_B_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию", "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
            img_swapped = Image.merge("RGB", (b, g, r))
            img_swapped.save(output_path)

            self.update_img()

    def button_swap_B_G_clicked(self):
        if self.image_path is not None:

            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            if img.mode == 'L':  # Проверяем режим изображения (L - оттенки серого)
                self.show_error_message("Невозможно выполнить операцию", "Черно-белое изображение не может быть обработано.")
                return

            if img.mode == 'RGBA':  # Если изображение имеет альфа-канал
                r, g, b, a = img.split()
            else:  # Если изображение имеет только RGB каналы
                r, g, b = img.split()
            img_swapped = Image.merge("RGB", (r, b, g))
            img_swapped.save(output_path)

            self.update_img()

    #endregion

    #region blur

    def apply_mean_blur(self, img_array):
        kernel = np.ones((3, 3)) / 9  # Среднее значение из 3x3 окна
        img_blurred = self.convolve2d(img_array, kernel, img_array.shape[:2])  # Используйте только первые два элемента кортежа
        return img_blurred

    def apply_model_4_blur(self, img_array):
        kernel = np.array([[0, 1, 0],
                           [1, 2, 1],
                           [0, 1, 0]]) / 6  # Модель 4 с соседями слева, справа, сверху и снизу
        img_blurred = self.convolve2d(img_array, kernel, img_array.shape[:2])  # Используйте только первые два элемента кортежа
        return img_blurred

    def apply_model_8_blur(self, img_array):
        kernel = np.ones((3, 3)) / 8  # Модель 8 с восемью соседями
        img_blurred = self.convolve2d(img_array, kernel, img_array.shape[:2])  # Используйте только первые два элемента кортежа
        return img_blurred

    @staticmethod
    def convolve2d(image, kernel, image_shape):
        image_height, image_width = image_shape

        kernel_height, kernel_width = kernel.shape

        pad_height = kernel_height // 2
        pad_width = kernel_width // 2

        output = np.zeros_like(image)
        padded_image = np.zeros((image_height + 2 * pad_height, image_width + 2 * pad_width, image.shape[2]))
        padded_image[pad_height:-pad_height, pad_width:-pad_width, :] = image

        for y in range(image_height):
            for x in range(image_width):
                for c in range(image.shape[2]):
                    output[y, x, c] = np.sum(kernel * padded_image[y:y + kernel_height, x:x + kernel_width, c])

        return output

    def button_blur_accept_clicked(self):
        if self.image_path is not None:
            input_path = self.image_path
            output_path = self.image_path

            img = Image.open(input_path)
            img_array = np.array(img)

            blur_type = ""
            if self.radio_mean_value.isChecked():
                blur_type = "mean"
            elif self.radio_model_4.isChecked():
                blur_type = "model_4"
            elif self.radio_model_8.isChecked():
                blur_type = "model_8"

            if blur_type in ["mean", "model_4", "model_8"]:
                img_blurred = getattr(self, f"apply_{blur_type}_blur")(img_array)
            else:
                self.show_error_message("Ошибка", "Выберите тип размытия")
                return

            img_blurred = Image.fromarray(img_blurred.astype('uint8'))  # Преобразование массива обратно в изображение
            img_blurred.save(output_path)
            self.update_img()

    #endregion


    #region hist

    def pixmap_to_numpy(self, pixmap):
        # Получаем размеры изображения
        width = pixmap.width()
        height = pixmap.height()

        # Преобразуем QPixmap в QImage
        image = pixmap.toImage()

        # Создаем массив NumPy
        img_array = np.zeros((height, width, 4), dtype=np.uint8)

        # Заполняем массив данными из QImage
        for y in range(height):
            for x in range(width):
                color = image.pixelColor(x, y)
                img_array[y, x, 0] = color.red()
                img_array[y, x, 1] = color.green()
                img_array[y, x, 2] = color.blue()
                img_array[y, x, 3] = color.alpha()

        return img_array
    def button_show_graph_clicked(self):
        if self.image_path is not None:
            image_path = self.image_path

            if self.check_box_hist_RGB.isChecked():
                GraphView.plot_rgb_histogram(image_path)

            if self.check_box_hist_intensive.isChecked():
                GraphView.plot_intensity_histogram(image_path)

            if self.check_box_map_contrast.isChecked():
                method = '4_neighbors' if self.radio_formula_4n.isChecked() else '8_neighbors' if self.radio_formula_8n.isChecked() else 'custom'
                window_size = self.spin_box_n_for_formula.value() if method == 'custom' else None
                try:
                    GraphView.contrast_map(image_path, method, window_size)
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))

            if self.check_box_profile_colomn.isChecked():
                col_num = self.spin_box_profile_intensive_num_colomn.value()
                GraphView.intensity_profile_column(image_path, col_num)

            if self.check_box_profile_intensive_str.isChecked():
                row_num = self.spin_box_profile_intensive_num_str.value()
                GraphView.intensity_profile_row(image_path, row_num)

    #endregion


    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
