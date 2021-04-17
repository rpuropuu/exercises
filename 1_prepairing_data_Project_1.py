# вырезаем и готовим квадраты из размеченной выборки под обучение нейронки
from PIL import Image
import os


# директория с исходными фотографиями
dir_name = r"c:\Users\..."
list_file = os.listdir(dir_name)


# возвращает в кортеж 4 координаты углов четырёхугольника
def get_area(name):
    with open(dir_name + "\\" + name + ".txt", "r") as file:
        l = list(file.readline().split())
        del l[0]
        return tuple(map(int, l))


# возвращает класс фотографии, согласно указанной разметке
# 1 - коты, 2 - собаки. для последующие записи в начало файла
def get_class(name):
    with open(dir_name + "\\" + name + ".txt", "r") as file:
        l = list(file.readline().split())
        return l[0]


# цикл нарезки и ресайза выборки под единые стандартные размеры
for item in list_file:
    # если расширение == джипег, то ...
    if os.path.splitext(item)[1] == ".jpg":
        # берём чисто название файла для цикла и функций
        unit = item.split(".")[0]
        # собираем путь для инициализации файла
        img = Image.open(dir_name + "\\" + unit + ".jpg")
        # передаём в функцию строку с нащванием файла
        area = get_area(unit)
        # вырезаем изображение по разметке area
        cropped_img = img.crop(area)
        # ресайзим под общий стандарт
        resized_img = cropped_img.resize([255, 255])
        # сохраняем в подкаталог для дальнейшей аугментации
        resized_img.save(f"rework/{get_class(unit)}_{unit}.jpg")


