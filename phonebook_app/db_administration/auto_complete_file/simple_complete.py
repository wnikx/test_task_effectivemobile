from russian_names import RussianNames
import csv
import random

companies = ['OAO "РелизБизнес"', 'OOO "Скороходы"', 'ЗАО "Спартак"', 'ООО "РэйвПлюс"', 'ИП "Соколовский"',
             'ОАО "Рубеж"', 'ИП "Влесов А.Г."', 'ЗАО "ТойВорлд"', 'ООО "Саншайн"', 'ОАО "Импульс"', 'ЗАО "НефтьСтрой"', 'ИП "Анаконда"']

potential_phone_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def auto_complete_csv_file(count):
    with open("./table_app/db/phone_book.csv", "a") as csv_file:
        for _ in range(count):
            first_name, patronymic, last_name = RussianNames().get_person().split()
            company = random.choice(companies)
            number = [random.choice(potential_phone_number)
                      for _ in range(10)]
            w_num = '7' + ''.join(number)
            random.shuffle(number)
            p_num = '7' + ''.join(number)
            csv_row = [last_name, first_name, patronymic,
                       company, w_num, p_num]
            writer = csv.writer(csv_file)
            writer.writerow(csv_row)
