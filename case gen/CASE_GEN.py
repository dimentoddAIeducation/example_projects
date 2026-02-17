import os
import time
import json
#'["name", "description", [["item1", "description for item1", 50], ["item2", "description for item2", 50]]]'
#CASE_GEN

#ADMIN
cmd_list="""
print_current_case() - Вывести предпросмотр кейса
open_case_file(<FILE_NAME>) - прочитать файл с кейсом

"""

def filter(data):
    stroke=""
    for i in data:
        if i != "'":
            stroke+=i
        else:
            stroke+='"'
    return stroke
def file_update(data):
    with open(f"{current_file}.txt", "w") as file:
        file.write(data)


print("CASE GEN by dimentodd")
time.sleep(1)
os.system("cls")

case_name="NULL"
description="NULL"
current_file="NULL"
items_to_print="NULL"

def formater():
    with open(f'{case_file_name}.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    data_filtered=json.loads(data)
    data_to_print=str(data_filtered[0])+"="+str(data_filtered)
    print(data_to_print)

    act=input("Нажмите enter для прододлжения: ")

while True:
    os.system("cls")
    interface=f"""
Current file: {current_file}
    
Current case name: {case_name}
Description: {description}
    
Items:
{items_to_print}
    """
    print(interface)
    act=input("_")

    if act=="cmd.list()":
        print(cmd_list)
        act=input("Нажмите enter для продолжения: ")



    elif act.find("new(")!=-1:

        case_file_name = act[4: len(act) - 1]

        with open(f"{case_file_name}.txt", "w") as file:
            file.write('["name", "description", [["item1", "description for item1", 50], ["item2", "description for item2", 50]]]')


    elif act=="new_item()":
        data_filtered=str(data_filtered)
        data_filtered_H1=data_filtered[0: len(data_filtered)-2]
        data_filtered_H2=data_filtered[len(data_filtered)-2: len(data_filtered)]

        data= data_filtered_H1+", ['name', 'description', 50]" + data_filtered_H2

        file_update(filter(data))

    elif act.find("del(")!=-1:
        try:
            num=int(act[4: len(act)-1])

            items.pop(num)
            data_filtered = f"['{case_name}', '{description}', {items}]"
            file_update(filter(data_filtered))
        except Exception as err:
            print(err)
            time.sleep(3)

    elif act.find("change")!=-1:
        try:
            act=act[7: len(act)-1]
            temp=act.split(", ")

            act=temp[0]
            num=temp[1]
            change=temp[2]
            print(act, num, change)

            if int(num)==-1:
                if act=="name":
                    data_filtered[0]=change
                    data=str(data_filtered)
                    print(filter(data))
                    file_update(filter(data))

                elif act=="des":
                    data_filtered[1]=change
                    data=str(data_filtered)
                    print(filter(data))
                    file_update(filter(data))

            else:
                if act == "name":
                    data_filtered[2][int(num)][0] = change
                    data = str(data_filtered)
                    print(filter(data))
                    file_update(filter(data))

                elif act == "des":
                    data_filtered[2][int(num)][1] = change
                    data = str(data_filtered)
                    print(filter(data))
                    file_update(filter(data))

                elif act == "chan":
                    data_filtered[2][int(num)][2] = int(change)
                    data = str(data_filtered)
                    print(filter(data))
                    file_update(filter(data))


        except Exception as err:
            print(err)
            time.sleep(3)


    elif act.find("open(")!=-1:
        case_file_name=act[5: len(act)-1]

        try:
            with open(f'{case_file_name}.txt', 'r', encoding='utf-8') as file:
                data = file.read()

            current_file = case_file_name

        except FileNotFoundError as err:
            print(f"Ошибка: {err}\nФайла с кейсом не существует :(")
            time.sleep(3)



    elif act=="format()":
        print("CASE!")
        try:
            formater()
        except Exception as err:
            print(err)
            time.sleep(3)






    if current_file!="NULL":

        with open(f'{current_file}.txt', 'r') as file:
            data = file.read()

        print(data, current_file)

        try:
            data_filtered = json.loads(data)

            case_name = data_filtered[0]
            description = data_filtered[1]
            items = data_filtered[2]

            items_to_print=""

            names = []
            for i in range(len(items)):
                names.append(len(items[i][0]))
            biggest_name=max(names)

            desc = []
            for i in range(len(items)):
                desc.append(len(items[i][1]))
            biggest_desc = max(desc)

            if len(items) > 9: temp = 7
            elif len(items) > 99: temp = 6
            elif len(items) > 999: temp = 5
            elif len(items) > 9999: temp = 4
            else: temp=8

            seps = 14 + biggest_name + 2 + 12 + biggest_desc - 10 + 7 + 6

            for i in range(len(items)):

                item_name=items[i][0]
                while len(item_name)<=biggest_name or len(item_name) <= 2:
                    item_name += " "

                desc = items[i][1]
                while len(desc) <= biggest_desc or len(desc) <= 10:
                    desc += " "

                stroke=f"{i}{" "*temp}|{item_name} |{desc}|{items[i][2]}\n{"-"*seps}\n"
                items_to_print += stroke

            if i > 9: temp = 7
            elif i > 99: temp = 6
            elif i > 999: temp = 5
            elif i > 9999: temp = 4

            stroke=f"Num      |Name{" "*(biggest_name-2)}|Description{" "*(biggest_desc-10)}|Chance\n{"-"*seps}\n"
            items_to_print= stroke + items_to_print
        except Exception as err:
            print(err)
            time.sleep(3)
