import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения
image_path = 'data/pngwing.com.png'
image = cv2.imread(image_path)

# region Показать изображение на экране
cv2.imshow('Original Image', image)
cv2.waitKey(0)
# endregion

# region Преобразование изображения в ч/б
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
#endregion

# region Разделение изображения на цветовые составляющие

blue, green, red = cv2.split(image)

# Гистограммы яркости для каждого канала
hist_blue = cv2.calcHist([blue], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([green], [0], None, [256], [0, 256])
hist_red = cv2.calcHist([red], [0], None, [256], [0, 256])

# Отобразить гистограммы
plt.plot(hist_blue, color='b')
plt.plot(hist_green, color='g')
plt.plot(hist_red, color='r')
plt.title('Гистограмма RGB каналов')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()
#endregion


# Создать копию изображения для отображения рамки
image_with_rectangle = image.copy()


# Функция для вычисления среднего значения

def my_mean(arr):
    return np.sum(arr) / arr.size

# Функция для вычисления стандартного отклонения
def my_std(arr):
    mean = my_mean(arr)
    variance = np.sum((arr - mean) ** 2) / arr.size
    return np.sqrt(variance)


# Обработка событий мыши
def mouse_event(event, x, y, flags, param):
    global image_with_rectangle

    if event == cv2.EVENT_MOUSEMOVE:
        if x >= 5 and y >= 5 and x < image.shape[1] - 5 and y < image.shape[0] - 5:
            # Создать копию изображения снова перед каждой отрисовкой рамки
            image_with_rectangle = image.copy()
            # Отрисовать внешнюю рамку
            cv2.rectangle(image_with_rectangle, (x - 6, y - 6), (x + 6, y + 6), (255, 255, 255), 1)
            # Выделение окна 11x11
            window = image[y - 5:y + 6, x - 5:x + 6]
            # Отобразить информацию о пикселе и окне
            print("="*50)
            print('Координаты:', (x, y))
            print('RGB значения:', image[y, x])
            print('Интенсивность:', my_mean(image[y, x]))
            print('Среднее значение в окне:', my_mean(window))
            print('Стандартное отклонение в окне:', my_std(window))
            print("="*50)


            # Отобразить изображение с рамкой
            cv2.imshow('Image', image_with_rectangle)


# Создание окна изображения и установка обработчика событий мыши
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_event)

# Отображение изображения
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Функции для редактирования параметров изображения
def adjust_brightness(image, alpha, beta):
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

def adjust_contrast(image, alpha):
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha)
    return adjusted_image

def apply_negative(image):
    negative_image = 255 - image
    return negative_image

def swap_channels(image, channel1, channel2):
    swapped_image = image.copy()
    swapped_image[:, :, channel1], swapped_image[:, :, channel2] = image[:, :, channel2], image[:, :, channel1]
    return swapped_image

def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

def blur_image(image, kernel_size):
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    return blurred_image

# Примеры использования функций редактирования изображения
# Увеличение/уменьшение интенсивности яркости
brightness_adjusted_image = adjust_brightness(image, alpha=1.5, beta=0)
cv2.imshow('Brightness Adjusted Image', brightness_adjusted_image)
cv2.waitKey(0)

# Повышение/снижение контрастности изображения
contrast_adjusted_image = adjust_contrast(image, alpha=1.5)
cv2.imshow('Contrast Adjusted Image', contrast_adjusted_image)
cv2.waitKey(0)

# Получение негатива яркости
negative_image = apply_negative(gray_image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)

# Обмен цветовых каналов
swapped_channels_image = swap_channels(image, 0, 2)  # Обмен красного и синего каналов
cv2.imshow('Swapped Channels Image', swapped_channels_image)
cv2.waitKey(0)

# Выполнение симметричного отображения изображения по горизонтали или вертикали
flipped_image_horizontal = flip_image(image, 1)  # Отражение по горизонтали
cv2.imshow('Flipped Image Horizontal', flipped_image_horizontal)
cv2.waitKey(0)

flipped_image_vertical = flip_image(image, 0)  # Отражение по вертикали
cv2.imshow('Flipped Image Vertical', flipped_image_vertical)
cv2.waitKey(0)

# Удаление шума методом размытия изображения
blurred_image = blur_image(image, kernel_size=5)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)

# Функция для просмотра профиля яркости по пиксельной строке
def brightness_profile(image, row):
    profile = image[row, :]
    plt.plot(profile)
    plt.title('Brightness Profile')
    plt.xlabel('Pixel')
    plt.ylabel('Brightness')
    plt.show()

brightness_profile(gray_image, 100)  # Профиль яркости для 100-ой строки

# Функция для создания карты контрастности изображения
def contrast_map(image, method='4_neighbors'):
    if method == '4_neighbors':
        # Карта контрастности по 4 соседям
        contrast_map = np.abs(image[1:, :] - image[:-1, :]) + np.abs(image[:, 1:] - image[:, :-1])
    elif method == '8_neighbors':
        # Карта контрастности по 8 соседям
        contrast_map = np.abs(image[1:, :] - image[:-1, :]) + np.abs(image[:, 1:] - image[:, :-1]) + \
                       np.abs(image[1:, 1:] - image[:-1, :-1]) + np.abs(image[1:, :-1] - image[:-1, 1:])
    else:
        # Карта контрастности по окну с задаваемым размером
        pass  # Здесь нужно добавить реализацию

    return contrast_map

contrast_map_image = contrast_map(gray_image, method='4_neighbors')
plt.imshow(contrast_map_image, cmap='hot')
plt.title('Contrast Map')
plt.colorbar()
plt.show()

# Сохранение изображения в файл
cv2.imwrite('edited_image.jpg', image)

cv2.destroyAllWindows()
