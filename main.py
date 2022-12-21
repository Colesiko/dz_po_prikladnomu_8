import logging
import random
logging.basicConfig(filename='draw.log', level=logging.INFO)
logging.info("Programm started")
n = input("Введите размер мешочка: ")
bukv = n.isdigit()
if bukv == False:  # проверка на буквы
    while bukv == False:
        n = input("Введите число большее 0(цифрами): ")
        bukv = str.isnumeric(n)
n = int(n)
if n <= 0:
    while n <= 0:
        n = input("Введите число большее 0(цифрами): ")
        bukv = n.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                n = input("Введите число большее 0(цифрами): ")
                bukv = str.isnumeric(n)
        n = int(n)
logging.info(f'razmer meshochka {n}')
# создаем массив чисел от 1 до n
meshok = list(range(1, n + 1))

while len(meshok) > 0:
    # выбираем случайное число из массива
    num = random.choice(meshok)
    print("выпал бочонок под номером ",num)
    # добавляем запись в лог-файл
    logging.info(f'vipawshiy bochonok {num}')
    # удаляем число из массива, чтобы оно не могло быть выбрано снова
    meshok.remove(num)
    logging.info(f'udalenie {num} bochonka')
    logging.info("Programm ended")
