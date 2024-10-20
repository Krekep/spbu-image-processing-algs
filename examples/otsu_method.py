import matplotlib.pyplot as plt

from image_convertions import convert_to_gray
from project.image_characteristics import get_brightness_histogram
from project.binary_images import otsu_method
from project.transform import image_from_datalist
from PIL import Image


image = Image.open("data/1.jpg")  # открываем картинку
rgb_data = list(image.getdata())  # получаем плоский список всех пикселей изображения
binary_image = otsu_method(rgb_data)  # проводим бинаризацию с помощью метода отсу
binary_image = image_from_datalist(
    binary_image, image.width, image.height
)  # создаём новую картинку из бинарной
binary_image.show()  # показываем результат бинаризации
# binary_image.save("test.png")  # сохраняем в test.png

g = convert_to_gray(image.getdata())  # переводим картинку в серый цвет
h = get_brightness_histogram(g)  # получаем гистограмму яркости
plt.bar(*zip(*h))  # строим её с помощью matplotlib
# plt.show()  # отображаем
