#Подключение библеотек
import os
import time
import random


# Admin. Настройки debug режима
debug_mode=0 #1 или 0
debug_skip_intro=False
version="1.0.0"

#==================================

#Создание функций debug режима

#подготовка настроек для debug_print()
err='err'
deb='deb'
cyc='cyc'
lis='lis'

def debug_print(type, stroke):  #Вывод данных в режиме debug
    stroke= str(stroke)

    data_to_print=0
    if type == 'err': data_to_print = "\033[31m[ERROR]_\033[0m " + stroke
    elif type=='deb': data_to_print = "\033[32m[DEBUG]_\033[0m " + stroke
    elif type=='cyc': data_to_print = "\033[34m[CYCLE]_\033[0m " + stroke

    if debug_mode == 1: print(data_to_print)

def clear_creen():  #Очистка экрана
    if debug_mode == 0: os.system("cls")



#==================================



#Начало работы. Проверка файла сохранений
work_direct=os.getcwd()
path=rf"{os.getcwd()}/saves/"
os.chdir(path) #Переход в папку saves

while True: #Попытки прочитать файл, пока не получится
    #Начинаем чтение данных файла save
    debug_print(cyc, "Чтение данных")
    debug_print(deb, "Чтение данных файла save.txt")
    try:
        #Получаем данные из файла save.txt и построчно записываем в массив
        file_save_data=[]
        with open('save.txt', 'r', encoding='utf-8') as f:
            for line in f:
                file_save_data.append(line.strip())
        debug_print(deb, "Успешно")
        debug_print(deb, file_save_data)
        debug_print(cyc, "Чтение данных сохранений завершено")

    except FileNotFoundError: #Не найден файл
        debug_print(err, "Файл сохранений отсутствует. Создание файла")
        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write("100\n0\n0.00001\n")
        debug_print(deb, "Файл создан. Перезагрузка")
        clear_creen()

    #Чтение данных файла updates
    debug_print(deb, "Чтение данных файла updates.txt")
    try:
        #Получаем данные из файла save.txt и построчно записываем в массив
        file_updates_data=[]
        with open('updates.txt', 'r', encoding='utf-8') as f:
            for line in f:
                file_updates_data.append(line.strip())
        debug_print(deb, "Успешно")
        debug_print(deb, file_updates_data)
        debug_print(cyc, "Чтение данных завершено")
        break

    except FileNotFoundError: #Не найден файл
        debug_print(err, "Файл сохранений отсутствует. Создание файла")
        with open('updates.txt', 'w', encoding='utf-8') as f:
            f.write("1\n1\n1\n1000\n1000\n1000")
        debug_print(deb, "Файл создан. Перезагрузка")
        clear_creen()

#Чтение завершено. Данные записаны в file_save_data

#Начало игры. Вывод интро
clear_creen()
debug_print(deb, "Начало игры")

#вывод логотипа
if debug_skip_intro==False:
    debug_print(deb, "Вывод интро")
    logo=fr"""
     __         __   _   _     _   _____   _______
    |  \       /  | |_| | \   | | |  ___| |  ___  |   version: {version}
    | |\\     //| |  _  |  \  | | | |     | |   | |
    | | \\___// | | | | | \ \ | | | |___  | |___| |
    | |  \___/  | | | | | |\ \| | |  ___| |    ___|
    | |         | | | | | | \ \ | | |     | |  \
    | |         | | | | | |  \  | | |___  | |\  \
    |_|         |_| |_| |_|   \_| |_____| |_| \__\    by dimentodd
    """
    print(logo)

    time.sleep(3)
    clear_creen()

    print("Подключение библеотек", end="")
    for i in range(7): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\nУспешно!")

    time.sleep(3)
    print("Создание точки доступа:\n    _Подготовка", end="")
    for i in range(3): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\n    _Запуск виртуальной точки\n    _Открытие портов", end="")
    for i in range(5): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")

    time.sleep(3)
    print("\nОшибка!_ Невозможно открыть порты вне белого списка машины")

    time.sleep(3)
    print("Попытка сопряежния с устройством", end="")
    for i in range(2): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\nУпсешно!\nРедактирование белого списка устройства", end="")
    for i in range(4): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\nУспешно!")

    time.sleep(5)
    print("Создание точки доступа:\n    _Подготовка", end="")
    for i in range(3): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\n    _Запуск виртуальной точки\n    _Открытие портов", end="")
    for i in range(5): #Илюзия ожидания
        time.sleep(0.5)
        print(".", end="")
    print("\nУспешно!\nВаш ключ доступа:", random.randint(100000000, 999999999))

    wait=input("Нажмите 'enter' для продолжения: ")


#Получаем данные и записываем в переменные
file_save_data = []
file_updates_data = []

with open('updates.txt', 'r', encoding='utf-8') as f:
    for line in f:
        file_updates_data.append(line.strip())
with open('save.txt', 'r', encoding='utf-8') as f:
    for line in f:
        file_save_data.append(line.strip())

debug_print(deb, "Запись данных в переменные")
money = float(file_save_data[0])
cryptobal = float(file_save_data[1])
crypto_per_sec = float(file_save_data[2])
kurs = 6024739

update_frequency=int(file_updates_data[0])
update_NOO=int(file_updates_data[1])
update_count=int(file_updates_data[2])
#=============
update_frequency_cost=int(file_updates_data[3])
update_NOO_cost=int(file_updates_data[4])
update_count_cost=int(file_updates_data[5])
debug_print(deb, "Данные записаны в переменные")

#Окончание интро. Начало основной игры
while True:
    debug_print(cyc, "Начало основной игры")

    start_time = time.perf_counter() #Запоминаем время

    #Очищаем экран и выводим интерфейс
    clear_creen()

    interface=f"""
    Money= {money:.2f} ₽ _Rubles_
    CRYPTO/sec= {crypto_per_sec:.5f} ₿ _BITCOIN_
    
    Currency (_BITCOIN_)= {kurs}
    CRYPTO balance= {cryptobal:.5f} ₿ _BITCOIN_
    
    Действия:
        1. Вывести валюту
        2. Открыть средство обновления компонентов
    
    """

    print(interface)
    act=input("Введите ваше действие {/help для справки}: ")

    #Получение и запись данных в переменные
    file_save_data = []
    with open('save.txt', 'r', encoding='utf-8') as f:
        for line in f:
            file_save_data.append(line.strip())

    debug_print(deb, "Запись данных в переменные")
    debug_print(deb, file_save_data)
    money = float(file_save_data[0])
    cryptobal = float(file_save_data[1])
    crypto_per_sec = float(file_save_data[2])
    kurs = 6024739
    debug_print(deb, "Данные записаны в переменные")

    #Ищем сколько времени прошло
    end_time = time.perf_counter()
    time_was = end_time-start_time
    time_was = round(time_was)
    debug_print(deb, f"Время прошло: {time_was}")

    for i in range(time_was):
        kurs=kurs+random.randint(-5000, 5000)

    cryptobal = cryptobal + (crypto_per_sec*time_was)

    #Смотрим на другие команды
    if act=="/help":
        clear_creen()
        debug_print(deb, "Открытие справки")

        print_help=f"""
        MINER v:{version} by dimentodd
        Игра miner это игра про заработок криптовалюты и дальнейшие манипуляции такие как вывод в деньги и использование их в других проектах
        
        Как играть:
        Майнер зарабатывает деньги всё время.
        после того как вы заработаете нужное кол-во криптовалюты напишите команду miner.withdraw после этого на ваш баланс начислятся
        деньги, взависимости от курса криптовалюты
        """
        print(print_help)
        wait=input("Нажмите 'enter' чтобы выйти: ")

    elif act=="2":
        debug_print(cyc, "Вход в меню updates")
        while True:
            clear_creen()
            interface_updates=f"""
    ======UPDATES======
    1. Frequency= {update_frequency}  mGz | Cost= {update_frequency_cost}
    2. Number of operations= {update_NOO} / sec | Cost= {update_NOO_cost}
    3. Count of miners= {update_count} | Cost= {update_count_cost}
    
    
            """
            print(interface_updates)
            act=input("Выберите обновление. (Назад-0): ")
            if act=="0": break

            mult_cost=3

            if act=="1":
                if money>=update_frequency_cost:
                    update_frequency+=1
                    crypto_per_sec+=0.00001
                    money-=update_frequency_cost
                    update_frequency_cost*=mult_cost
                    with open('save.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{money}\n{cryptobal}\n{crypto_per_sec}\n{kurs}")
                    with open('updates.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{update_frequency}\n{update_NOO}\n{update_count}\n{update_frequency_cost}\n{update_NOO_cost}\n{update_count_cost}")
                else:
                    clear_creen()
                    print(f"Недостаточно денег!\nДля покупки необходимо ещё {round(update_frequency_cost-money)}.")
                    time.sleep(3)

            elif act == "2":
                if money >= update_NOO_cost:
                    update_NOO += 1
                    crypto_per_sec += 0.00001
                    money -= update_NOO_cost
                    update_NOO_cost *= mult_cost
                    with open('save.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{money}\n{cryptobal}\n{crypto_per_sec}\n{kurs}")
                    with open('updates.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{update_frequency}\n{update_NOO}\n{update_count}\n{update_frequency_cost}\n{update_NOO_cost}\n{update_count_cost}")
                else:
                    clear_creen()
                    print(f"Недостаточно денег!\nДля покупки необходимо ещё {round(update_frequency_cost - money)}.")
                    time.sleep(3)

            elif act == "3":
                if money >= update_count_cost:
                    update_count += 1
                    crypto_per_sec += 0.00001
                    money -= update_count_cost
                    update_count_cost *= mult_cost
                    with open('save.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{money}\n{cryptobal}\n{crypto_per_sec}\n{kurs}")
                    with open('updates.txt', 'w', encoding='utf-8') as f:
                        f.write(f"{update_frequency}\n{update_NOO}\n{update_count}\n{update_frequency_cost}\n{update_NOO_cost}\n{update_count_cost}")
                else:
                    clear_creen()
                    print(f"Недостаточно денег!\nДля покупки необходимо ещё {round(update_frequency_cost - money)}.")
                    time.sleep(3)




    elif act=="1":
        debug_print(deb, "Вывод денег")

        money=money+(cryptobal*kurs) #К деньгам прибавляем вывод крипты
        debug_print(deb, f"Денег получено: {cryptobal*kurs}")
        cryptobal=0

        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write(f"{money}\n{cryptobal}\n{crypto_per_sec}\n{kurs}")

        debug_print(deb, "Данные записаны")

    else:
        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write(f"{money}\n{cryptobal}\n{crypto_per_sec}\n{kurs}")