import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

class GraphView:
    @staticmethod
    def plot_rgb_histogram(image_path):
        img = Image.open(image_path)
        img_array = np.array(img)

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for i, color in enumerate(['red', 'green', 'blue']):
            axes[i].hist(img_array[:,:,i].ravel(), bins=256, color=color)
            axes[i].set_title(f'{color.upper()} гистограмма')
            axes[i].set_xlim(0, 255)

        plt.show()


    @staticmethod
    def plot_intensity_histogram(image_path):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(img_array.ravel(), bins=256, color='gray')
        ax.set_title('Гистограмма яркости')
        ax.set_xlim(0, 255)

        plt.show()

    @staticmethod
    def contrast_map(image_path, method='4_neighbors', window_size=None):
        try:
            # Проверяем наличие файла изображения
            with open(image_path, 'rb') as f:
                pass
        except FileNotFoundError:
            raise FileNotFoundError("Image file not found.")

        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        try:
            if method == '4_neighbors':
                kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
            elif method == '8_neighbors':
                kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])
            elif method == 'custom':
                if window_size is None:
                    raise ValueError("Please provide window size for custom method.")
                kernel = np.ones((window_size, window_size)) / (window_size ** 2)
            else:
                raise ValueError("Unknown method.")

            img_filtered = np.abs(convolve2d(img_array, kernel, mode='same')) #TODO собственная реализация
            img_filtered = Image.fromarray(np.uint8(img_filtered))

            plt.figure()
            plt.imshow(img_filtered, cmap='gray')
            plt.title('Карта контрастности')
            plt.colorbar()
            plt.show()
        finally:
            pass



    @staticmethod
    def intensity_profile_row(image_path, row_number):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        row_data = img_array[row_number, :]

        plt.figure()
        plt.plot(row_data)
        plt.title('Профиль яркости - Строка {}'.format(row_number))
        plt.xlabel('Колонка')
        plt.ylabel('Интенсивность')
        plt.show()


    @staticmethod
    def intensity_profile_column(image_path, column_number):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        column_data = img_array[:, column_number]

        plt.figure()
        plt.plot(column_data)
        plt.title('Профиль яркости - Колонка {}'.format(column_number))
        plt.xlabel('Строка')
        plt.ylabel('Интенсивность')
        plt.show()
