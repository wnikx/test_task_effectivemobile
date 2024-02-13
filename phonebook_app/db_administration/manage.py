from .auto_complete_file import api_complete, simple_complete
import pandas as pd
from style.style import stylish_output, stylish_output_add_operation
import csv


class AdminTable:
    TABLE = "./phonebook_app/db/phone_book.csv"

    def __init__(self, name: str = "Пользователь", api: bool = False, count: int = 20):
        self.username = name
        self.api = api
        self.count = count
        self.df = pd.read_csv(self.TABLE, index_col=None)
        self.df.index = self.df.index + 1

    def auto_add_rows(self):
        """Авто-заполнение файла phone_book.csv """

        if not self.api:
            simple_complete.auto_complete_csv_file(self.count)
        else:
            api_complete.auto_complete_csv_file(self.count)

    def show_table_pagination(self):
        """Постраничный вывод файла phone_book.csv"""

        df = pd.read_csv(self.TABLE, index_col=None, chunksize=10)
        page = 0
        for chunk in df:
            page += 1
            stylish_output(chunk, f'"{page}" страница')

    def show_table_page(self, num: int):
        """Демонстрация конкретной страницы файла phone_book.csv"""

        self.df = pd.read_csv(self.TABLE, index_col=None)
        self.df.index = self.df.index + 1
        page = num * 10
        stylish_output(self.df.iloc[page - 10: page], f"{num} страница")

    def append_row(self, new_row: dict):
        """Добавление строки в файл phone_book.csv"""

        self.df = self.df._append(new_row, ignore_index=True)
        self.df.to_csv(self.TABLE, index=False)
        print()
        stylish_output_add_operation("Запись добавлена")
        print()

    def update_row(self, dig: int, column: str, value: str):
        """Изменение конкретной записи в файле phone_book.csv"""

        self.df.at[dig, column] = value
        self.df.to_csv(self.TABLE, index=False)

    def delete_row(self, dig: int):
        """Удаление строки из файла phone_book.csv"""

        self.df = self.df.drop(dig)
        self.df.to_csv(self.TABLE, index=False)

    def search_rows(self, value: list):
        """Поиск записей в файле phone_book.csv"""

        df = pd.read_csv(self.TABLE, index_col=None)
        df.index = df.index + 1
        index = 0
        while index < len(value):
            df = df[(df["Фамилия"] == f'{value[index]}') |
                    (df["Имя"] == f'{value[index]}') |
                    (df["Отчество"] == f'{value[index]}') |
                    (df["Название организации"] == f'{value[index]}') |
                    (df["Телефон рабочий"] == f'{value[index]}') |
                    (df["Телефон личный"] == f'{value[index]}')
                    ]
            index += 1
        stylish_output(df, f'Поиск - {" ".join(value)}')

    def show_table(self):
        """Демонстрация всех записей в файле phone_book.csv"""

        self.df = pd.read_csv(self.TABLE, index_col=None)
        self.df.index = self.df.index + 1
        stylish_output(self.df)
