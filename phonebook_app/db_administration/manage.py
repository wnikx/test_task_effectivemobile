from .auto_complete_file import api_complete, simple_complete
import pandas as pd


class AdminTable:
    TABLE = "./phonebook_app/db/phone_book.csv"

    def __init__(self, name: str, api: bool = False, count: int = 50, pagination: int = 10):
        self.name = name
        self.api = api
        self.count = count
        self.pagination = pagination

    def auto_add_rows(self):
        """Авто-заполнение файла phone_book.csv """

        if not self.api:
            simple_complete.auto_complete_csv_file(self.count)
        else:
            api_complete.auto_complete_csv_file(self.count)

    def show_table_pagination(self):
        """Постраничный вывод файла phone_book.csv"""

        df = pd.read_csv(self.TABLE, index_col=None,
                         chunksize=self.pagination)
        for chunk in df:
            print(chunk)

    def show_table_page(self, num: int):
        """Демонстрация конкретной страницы файла phone_book.csv"""

        df = pd.read_csv(self.TABLE)
        page = num * self.pagination
        return df.iloc[page: page + 10]

    def append_row(self, row: list):
        """Добавление строки в файл phone_book.csv"""

        with open("self.TABLE", "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)
            return "Запись удалена"

    def update_row(self, dig: int, column: str, value: str):
        """Изменение конкретной записи в файле phone_book.csv"""

        df = pd.read_csv(self.TABLE)
        df.at[dig, column] = value
        df.to_csv(self.TABLE, index=False)

    def delete_row(self, dig: int):
        """Удаление строки из файла phone_book.csv"""

        df = pd.read_csv(self.TABLE)
        if isinstance(dig, int) and len(df) > dig > 0:
            df = df.drop(dig)
            df.to_csv(self.TABLE, index=False)
            return f"Запись {dig} удалена!"
        return "Некорректные данные. Пожалуйста введите корректный номер строки который хотите удалить."

    def search_rows(self, value):
        """Поиск записей в файле phone_book.csv"""

        df = pd.read_csv(self.TABLE)
        result = df[df['Имя'] == f'{value}'][
            df['Отчество'] == 'Андреевич'
        ]
        return result

    def show_table(self):
        """Демонстрация всех записей в файле phone_book.csv"""

        df = pd.read_csv(self.TABLE, index_col=None)
        return df
