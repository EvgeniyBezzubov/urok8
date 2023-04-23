import glob
import re
import csv


def parser(fread, poisk, list_add):  # фуункция ищет в тексте (fread) входжения (poisk), добавляет в цуказанный лист
    m = re.search(poisk, fread)  # извлечение "Изготовитель системы"
    m2 = re.search(r'\s{2}.*', m[0])
    name = re.search(r'\S.*', m2[0])
    list_add.append(name[0])
    # print(list_add)


def get_data():
    name = glob.glob(".\\\\*[0-9].txt")
    print(name)
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data_all = []
    for i in name:

        f = open(i, "r")
        fread = f.read()
        #    print(f.read())
        parser(fread, 'Изготовитель системы:.*', os_prod_list)  # 4 списка
        parser(fread, 'Название ОС:.*', os_name_list)
        parser(fread, 'Код продукта:.*', os_code_list)
        parser(fread, 'Тип системы:.*', os_type_list)
        main_data = ["Изготовитель системы", "Название ОС", "Код продукта",
                     "Тип системы"]  # мейн дата с названиями столбцов
        f.close()

        # зачем нам в этой части задания говорят записывать всё в промежуточный какой-то фаил, потом всё равно нам ещё одну функцию создавать под запись в csv?
        with open("main_data.txt", "w") as f2:
            for line in main_data_all:
                for elem in line:
                    f2.write(str(elem))
                    f2.write(",  ")
                f2.write('\n')

        f2.close()
    # print(main_data_all,"sddasad")
    for i in range(len(main_data) - 1):
        main_data_all.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data_all, main_data


def write_to_csv():
    data = get_data()
    data_main = data[1]
    data = data[0]

    with open('kp_data_write_4.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerow(data_main)
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data)

    with open('kp_data_write_3.csv') as f_n:
        print(f_n.read())


write_to_csv()
