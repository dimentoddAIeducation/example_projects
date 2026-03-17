# ШНХos lib / ver: 0.2
import os
import time
from colorama import init
import keyboard as kb

#Запатентованно dimentodd, 22HUNTERS, CDcorporation


class Os:
    class Control:
        class Chose:
            items = []
            delay_time = 0.2
            label = None
            clear_screen = True

            def start(self):
                act = 0
                while True:
                    if self.clear_screen:
                        os.system("cls")

                    # ===========Actions print===========
                    if self.label != None: print(self.label)
                    for i in range(len(self.items)):
                        if i == act: char = ">"
                        else: char = " "
                        data_to_print = f"{char}{self.items[i]}"
                        print(data_to_print)

                    time.sleep(self.delay_time)
                    # ===========Keyboard input===========
                    while True:
                        key = kb.read_key(suppress=True)

                        if key == "up":
                            if act > 0: act -= 1
                            break

                        if key == "down":
                            if act < len(self.items)-1: act += 1
                            break

                        if key == "enter":

                            return self.items[act]

            def set_label(self, name):
                self.label = name

            def set_delay_time(self, delay):
                self.delay_time = delay

            def set_clear_screen(self, mode):
                self.clear_screen = bool(mode)

            def add_item(self, name):
                self.items.append(name)

            def clear(self):
                self.items.clear()

        class Menu:
            actions = []
            OnTick = None
            delay_time = 0.2
            label = None
            clear_screen = True

            def start(self):
                act = 0
                while True:
                    if len(self.actions) == 0:
                        break

                    if self.clear_screen:
                        os.system("cls")

                    self.OnTick()

                    # ===========Actions print===========
                    if self.label != None: print(self.label)
                    for i in range(len(self.actions)):
                        if i == act: char = ">"
                        else: char = " "
                        data_to_print = f"{char}{self.actions[i][0]}"
                        print(data_to_print)

                    time.sleep(self.delay_time)
                    # ===========Keyboard input===========
                    while True:
                        key = kb.read_key(suppress=True)

                        if key == "up":
                            if act > 0: act -= 1
                            break

                        if key == "down":
                            if act < len(self.actions)-1: act += 1
                            break

                        if key == "enter":
                            self.actions[act][1]()
                            break

            def set_label(self, name):
                self.label = name

            def set_delay_time(self, delay):
                self.delay_time = delay

            def add_act(self, name, action):
                self.actions.append([name, action])

            def set_clear_screen(self, mode):
                self.clear_screen = bool(mode)

            def set_ontick_act(self, action):
                self.OnTick = action

    class Debug:
        debug_mode = False
        init()

        def setmode(self, mode):
            self.debug_mode = bool(mode)

        def print(self, type, data):
            if self.debug_mode:
                if type == "deb": data_to_print = f"\033[32m_[DEB]: \033[0m{data}"
                elif type == "err": data_to_print = f"\033[31m_[ERR]: \033[0m{data}"
                elif type == "cyc": data_to_print = f"\033[34m_[CYC]: \033[0m{data}"
                elif type == "buf": data_to_print = f"\033[33m_[BUF]: \033[0m{data}"

                else: print(f"\033[31m_[ERR]\033[0m: Unknown data type: {type}")
                print(data_to_print)

        def clearscreen(self):
            if self.debug_mode:
                print("\033[35m_[CLR_SCR]\033[0m: Screen cleared")
            else:
                os.system("cls")


# Пример использования

cart = {'lemons': 5, 'tomatoes': 3, 'eggs': 4}

deb = Os.Debug()
deb.setmode(0)


def delete_item():
    deb.print("cyc", "Вход в удаления объекта")

    del_item_interface = Os.Control.Chose()

    del_item_interface.clear()  # Очистка буффера
    deb.print("buf", "Буффер _del_item_interface_ очищен")

    del_item_interface.set_label("="*6 + "Выберите товар" + "="*6)

    items = cart.keys()
    items = list(items)
    deb.print("deb", f"Значения: {items}")

    for item in items:
        del_item_interface.add_item(item)

    chose = del_item_interface.start()
    del cart[chose]
    deb.print("deb", f"Удалено значение: {chose}")


def add_item():
    deb.print("cyc", "Вход в Добавление объекта")
    deb.clearscreen()

    name = input("Введите имя: ")
    value = input("Введите значение: ")

    cart.update({name: value})

    deb.print("deb", f"Добавленно значение: {name}:{value}")


def set_value():
    deb.print("cyc", f"Вход в установку значения")

    set_value_interface = Os.Control.Chose()

    set_value_interface.clear()
    deb.print("buf", "Буффер _set_value_interface_ очищен")

    set_value_interface.set_label("=" * 6 + "Выберите товар" + "=" * 6)

    items = cart.keys()
    for item in items:
        set_value_interface.add_item(item)

    chose = set_value_interface.start()

    deb.clearscreen()

    value = int(input("Введите значение: "))

    cart[chose] = value
    deb.print("deb", f"Установленно значение: {chose}:{value}")


def print_items():
    items = cart.keys()
    for item in items:
        print(f"{item}: {cart[item]}")


main_interface = Os.Control.Menu()

main_interface.set_label("="*6 + "Корзина" + "="*6)
main_interface.add_act("Добавить продукты", add_item)
main_interface.add_act("Удалить продукты", delete_item)
main_interface.add_act("Установить значение", set_value)

main_interface.set_ontick_act(print_items)

deb.print("cyc", "Запуск основного цикла")
main_interface.start()
