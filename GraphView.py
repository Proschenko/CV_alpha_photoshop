import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class GraphView:
    @staticmethod
    def plot_rgb_histogram(image_path):
        img = Image.open(image_path)
        img_array = np.array(img)

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for i, color in enumerate(['red', 'green', 'blue']):
            axes[i].hist(img_array[:,:,i].ravel(), bins=256, color=color)
            axes[i].set_title(f'{color.upper()} Histogram')
            axes[i].set_xlim(0, 255)
            axes[i].set_ylim(0, 10000)  # Может потребоваться изменить диапазон в зависимости от изображения

        plt.show()


    @staticmethod
    def plot_intensity_histogram(image_path):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(img_array.ravel(), bins=256, color='gray')
        ax.set_title('Intensity Histogram')
        ax.set_xlim(0, 255)
        ax.set_ylim(0, 10000)  # Может потребоваться изменить диапазон в зависимости от изображения

        plt.show()


    @staticmethod
    def contrast_map(image_path, method='4_neighbors', window_size=None):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

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

        img_filtered = np.abs(np.convolve(img_array, kernel, mode='same'))
        img_filtered = Image.fromarray(np.uint8(img_filtered))

        plt.imshow(img_filtered, cmap='gray')
        plt.title('Contrast Map')
        plt.colorbar()
        plt.show()


    @staticmethod
    def intensity_profile_row(image_path, row_number):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        row_data = img_array[row_number, :]

        plt.figure()
        plt.plot(row_data)
        plt.title('Intensity Profile - Row {}'.format(row_number))
        plt.xlabel('Column')
        plt.ylabel('Intensity')
        plt.show()


    @staticmethod
    def intensity_profile_column(image_path, column_number):
        img = Image.open(image_path).convert('L')
        img_array = np.array(img)

        column_data = img_array[:, column_number]

        plt.figure()
        plt.plot(column_data)
        plt.title('Intensity Profile - Column {}'.format(column_number))
        plt.xlabel('Row')
        plt.ylabel('Intensity')
        plt.show()
