import cv2
import numpy as np
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, qRgb, QColor
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QApplication
from PyQt5 import QtCore, QtWidgets
from PIL import Image

from PreprocessingIMG import Preprocessing_IMG


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #region base_pyqt
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 221, 121))
        self.groupBox.setObjectName("groupBox")
        self.button_download_img = QtWidgets.QPushButton(self.groupBox)
        self.button_download_img.setGeometry(QtCore.QRect(10, 40, 201, 28))
        self.button_download_img.setObjectName("button_download_img")
        self.button_save_img = QtWidgets.QPushButton(self.groupBox)
        self.button_save_img.setGeometry(QtCore.QRect(10, 80, 201, 28))
        self.button_save_img.setObjectName("button_save_img")

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
        self.slider_intensive_B.setMaximum(100)
        self.slider_intensive_B.setProperty("value", 50)
        self.slider_intensive_B.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_B.setObjectName("slider_intensive_B")
        self.slider_intensive_G = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_G.setGeometry(QtCore.QRect(40, 150, 161, 22))
        self.slider_intensive_G.setMaximum(100)
        self.slider_intensive_G.setProperty("value", 50)
        self.slider_intensive_G.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_G.setObjectName("slider_intensive_G")
        self.slider_intensive_R = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_R.setGeometry(QtCore.QRect(40, 120, 161, 21))
        self.slider_intensive_R.setMaximum(100)
        self.slider_intensive_R.setProperty("value", 50)
        self.slider_intensive_R.setOrientation(QtCore.Qt.Horizontal)
        self.slider_intensive_R.setObjectName("slider_intensive_R")
        self.slider_intensive_all = QtWidgets.QSlider(self.groupBox_3)
        self.slider_intensive_all.setGeometry(QtCore.QRect(10, 61, 191, 20))
        self.slider_intensive_all.setMaximum(100)
        self.slider_intensive_all.setProperty("value", 50)
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
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 730, 221, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.slider_contrast = QtWidgets.QSlider(self.groupBox_4)
        self.slider_contrast.setGeometry(QtCore.QRect(10, 30, 201, 22))
        self.slider_contrast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slider_contrast.setMaximum(100)
        self.slider_contrast.setProperty("value", 50)
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
        self.text_output_console.setGeometry(QtCore.QRect(930, 220, 231, 91))
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
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(930, 320, 231, 481))
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
        self.spin_box_profile_intensive_num_colomn.setObjectName("spin_box_profile_intensive_num_colomn")
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
        self.view_small_square.setGeometry(QtCore.QRect(960, 30, 170, 170))
        self.view_small_square.setScaledContents(True)
        self.view_small_square.setObjectName("view_small_square")
        self.view_small_square.setStyleSheet("border: 1px solid black;")  # Добавляем рамку



        #region fields
        self.image_path = None
        self.original_pixmap = None  # Сохраняем оригинальное изображение
        #endregion

        #region action
        self.button_download_img.clicked.connect(self.handle_load_image)


        #region grey
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

        # region swap chanel
        self.button_swap_R_B.clicked.connect(self.button_swap_R_B_clicked)
        self.button_swap_R_G.clicked.connect(self.button_swap_R_G_clicked)
        self.button_swap_B_G.clicked.connect(self.button_swap_B_G_clicked)
        # endregion

        #region IMG flip
        self.button_flip_vertical.clicked.connect(self.button_flip_vertical_clicked)
        self.button_flip_horizontal.clicked.connect(self.button_flip_horizontal_clicked)
        #endregion



        # Подключаем обработчик события мыши для отслеживания движения
        self.view_main_window.mouseMoveEvent = self.mouseMoveEvent

        #endregion

    def handle_load_image(self):
        # Диалоговое окно выбора файла для загрузки изображения
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выбрать изображение", "",
                                                            "Images (*.png *.tiff *.bmp)")

        if filename:  # Если пользователь выбрал файл
            # Вызываем метод из модуля Preprocessing_IMG для изменения размера и сохранения изображения
            resized_image_path = Preprocessing_IMG.resize_and_save_image(filename)
            self.image_path = resized_image_path

            if resized_image_path:
                # Загружаем изображение на QLabel из папки Temp
                pixmap = QPixmap(resized_image_path)
                self.original_pixmap = pixmap.copy()  # Сохраняем оригинальное изображение
                self.view_main_window.setPixmap(pixmap)  # Отображаем изображение на основном QLabel


    def update_img(self):
        pixmap = QPixmap(self.image_path)
        self.original_pixmap = pixmap.copy()  # Сохраняем оригинальное изображение
        self.view_main_window.setPixmap(pixmap)  # Отображаем изображение на основном QLabel

    def mouseMoveEvent(self, event):
        # Получаем текущие координаты курсора
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
                painter.setPen(QPen(Qt.yellow, 2))  # Устанавливаем желтую рамку толщиной 2 пикселя
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
                intensity = np.mean(rgb_values)  # Вычисляем интенсивность
                average_rgb = np.mean(rgb_values, axis=(0, 1))  # Вычисляем средние значения RGB
                std_deviation = np.std(rgb_values)  # Вычисляем стандартное отклонение

                # Округляем значения до двух знаков после запятой
                intensity = round(intensity, 2)
                average_rgb = tuple(round(val, 2) for val in average_rgb)
                std_deviation = round(std_deviation, 2)

                # Отображаем значения в text_output_console
                self.text_output_console.setText(
                    f"Координаты: ({cursor_position.x()}, {cursor_position.y()})\n"
                    f"RGB: {average_rgb}\n"
                    f"Интенсивность: {intensity}\n"
                    f"𝜇𝑊𝑝: {np.mean(intensity)}\n"
                    f"𝑠𝑊𝑝: {std_deviation}"
                )
            else:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DoubleATeam_CV_lab_1"))
        self.groupBox.setTitle(_translate("MainWindow", "Изображение"))
        self.button_download_img.setText(_translate("MainWindow", "Загрузить"))
        self.button_save_img.setText(_translate("MainWindow", "Сохранить"))
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
        self.text_output_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Координаты:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RGB значения:<br />Интенсивность:<br />Мат отклонение:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Среднее:</p></body></html>"))
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
        self.action.setText(_translate("MainWindow", "Загрузить"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))

    # region grey

    def button_grey_img_clicked(self, channel):


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
        img = img.convert('RGBA')  # Используем RGBA для поддержки прозрачности
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
        pass

    def button_negative_G_clicked(self):
        pass
    def button_negative_B_clicked(self):
        pass

    def button_negative_all_clicked(self):
        pass

    #endregion

    #region IMG FLIP
    def button_flip_vertical_clicked(self):
        pass

    def button_flip_horizontal_clicked(self):
        pass

    #endregion

    #region SWAP CHANEL RGB

    def button_swap_R_G_clicked(self):
        pass

    def button_swap_R_B_clicked(self):
        pass

    def button_swap_B_G_clicked(self):
        pass

    #endregion



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
