from db_administration.manage import AdminTable
from rich.console import Console
from lexicon.lexicon import lex

console = Console()


def show_page_handler(count: int):
    """Хэндлер который обрабатывает введённые данные"""

    while True:
        console.print("-- [white]Введите номер страницы[/white]: ")
        page = input()
        try:
            page = int(page)
            pages = count // 10
            if any([count % 2 == 0 and page > pages, count % 2 != 0 and page > pages + 1, page < 1]):
                console.print(lex["page_does_not_exist"])
            else:
                return page
        except:
            console.print(lex["input_correct_data"])


def add_row_handler():
    """Обработчик который забирает данные у пользователя прежде чем добавить их в файл"""

    data = {}
    columns = ["Фамилия", "Имя", "Отчество",
               "Название организации", "Телефон рабочий", "Телефон личный"]
    for idx in range(6):
        console.print(
            f"-- [white]Введите данные, которые добавяться в колонку '{columns[idx]}'[/white]")
        word = input('---- ')
        data[columns[idx]] = word
    return data
