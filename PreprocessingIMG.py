from PIL import Image

class Preprocessing_IMG:

    @staticmethod
    def resize_and_save_image(input_path, output_dir="Temp"):
        try:
            # Открываем изображение
            img = Image.open(input_path)

            # Изменяем размер до 661x561 пикселей
            img_resized = img.resize((661, 561), Image.LANCZOS)

            # Формируем путь для сохранения изображения
            filename = input_path.split('/')[-1].split('.')[0]  # Имя файла без расширения
            output_path = f"{output_dir}/{filename}_resize.{img.format.lower()}"

            # Сохраняем изображение
            img_resized.save(output_path)

            print("Изображение успешно сохранено:", output_path)
            return output_path
        except Exception as e:
            print("Произошла ошибка:", str(e))
            return None
