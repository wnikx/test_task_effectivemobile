from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.text import Text
from rich import box
from lexicon.lexicon import lex

console = Console()


def stylish_output(df, title=lex["default_title"]):
    # Создание новой таблицы Rich
    table = Table(show_header=True, header_style="cyan")
    table.title = title
    table.border_style = "bright_yellow"
    table.box = box.MINIMAL
    # Добавление заголовков столбцов
    table.add_column("№")
    table.add_column("Фамилия")
    table.add_column("Имя")
    table.add_column("Отчество")
    table.add_column("Название организации")
    table.add_column("Телефон рабочий")
    table.add_column("Телефон личный")

    # Добавление данных из DataFrame
    for index, row in df.iterrows():
        surname_style = Style(color="white")
        name_style = Style(color="white")
        patronymic_style = Style(color="white")
        company_style = Style(color="white")
        w_phone_style = Style(color="white")
        p_phone_style = Style(color="white")

        table.add_row(
            Text(str(index), style=Style(color="white")),
            Text(row["Фамилия"], style=surname_style),
            Text(row["Имя"], style=name_style),
            Text(row["Отчество"], style=patronymic_style),
            Text(row["Название организации"], style=company_style),
            Text(str(row["Телефон рабочий"]), style=w_phone_style),
            Text(str(row["Телефон личный"]), style=p_phone_style),
        )

    # Вывод таблицы
    console.print(table, justify="center")


def stylish_output_add_operation(word):
    console.rule(f"[bold][white]{word}[/white][/bold]",
                 style="green")
