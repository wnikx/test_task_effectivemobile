from db_administration.manage import AdminTable
from rich.console import Console
from lexicon.lexicon import lex
import time

console = Console()


def show_page_handler(count: int):
    """Обработчик, который проверяет валидность данных, прежде чем показать страницу"""

    if not count // 10:
        page_count = 1
    else:
        page_count = count // 10
    while True:
        console.print(
            f"---- [white]Введите номер страницы[/white]\n---- (от 1 до {page_count}) ")
        page = input("-------- ")
        if page == "q":
            console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                         style="#FFD700")
            console.print(lex["config"])
            break
        else:
            try:
                page = int(page)
                pages = 1 if not count // 10 else count // 10
                if page <= 0 or page > pages:
                    console.print(lex["page_does_not_exist"])
                else:
                    return page
            except:
                console.print(lex["input_correct_data"])


def add_row_handler():
    """Обработчик, который проверяет валидность данных, прежде чем добавить их в файл"""

    data = {}
    columns = ["Фамилия", "Имя", "Отчество",
               "Название организации", "Телефон рабочий", "Телефон личный"]
    for idx in range(6):
        console.print(
            f'---- [white]Введите данные, которые добавятся в колонку "[blue]{columns[idx]}[/blue]"[/white]:')
        word = input("--" + lex["user_input"])
        if word == "q":
            console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                         style="#FFD700")
            console.print(lex["config"])
            data = {}
            break
        elif not word:
            data[columns[idx]] = "Нет данных"
        else:
            data[columns[idx]] = word
    return data


def update_row_handler(length, columns):
    "Обработчик, который проверяет валидность данных, прежде чем обновить запись в файле"

    flag = False
    if length == 0:
        console.print(lex["empty_table"])
    else:
        while True:
            if flag:
                break
            console.print(
                f"---- [white]Введите номер записи в которой хотите поменять данные[/white]\n---- [blue](от 1 до {length})[/blue]")
            user_input = input("--" + lex["user_input"])
            if user_input == 'q':
                print()
                console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                             style="#FFD700")
                print()
                console.print(lex["config"])
                return False
            try:
                if length > int(user_input) > 0:
                    while True:
                        console.print("----" + lex["user_input_columns"])
                        user_input_1 = input("----" + lex["user_input"])
                        user_columns = user_input_1.split()
                        user_dict = {}
                        if user_input_1 == 'q':
                            flag = True
                            print()
                            console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                                         style="#FFD700")
                            print()
                            console.print(lex["config"])
                            return False
                        elif user_input_1 and all([False if column not in columns else True for column in user_columns]):
                            for coll in user_columns:
                                console.print(
                                    f'-------- [white]Введите данные, которые добавяться в колонку [blue]"{coll}"[/blue]:[/white]')
                                user_input_2 = input(
                                    "------" + lex["user_input"])
                                if user_input_2 == 'q':
                                    user_dict = {}
                                    print()
                                    console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                                                 style="#FFD700")
                                    console.print(lex["config"])
                                    print()
                                    return False
                                user_dict[coll] = user_input_2
                            if user_dict:
                                flag = True
                                print()

                                console.rule(f"[bold][white]Запись обновлена[/white][/bold]",
                                             style="#FFD700")
                                print()
                                return user_input, user_dict
                        else:
                            console.print(lex["incorrect_column_name"])

                else:
                    console.print(lex["incorrect_string_number"])

            except:
                console.print(lex["incorrect_type"])


def delete_row_handler(length):
    "Обработчик, который проверяет валидность данных, прежде чем удалить запись в файле"

    if length == 0:
        console.print(lex["empty_table"])
        return False
    else:
        while True:
            console.print(
                f"---- [white]Введите номер строки, которую хотите удалить[/white]\n---- [blue](от 1 до {length})[/blue]")
            user_input = input("--" + lex["user_input"])
            if user_input == "q":
                print()
                console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                             style="#FFD700")
                console.print(lex["config"])
                print()
                return False
            else:
                try:
                    dig = int(user_input)
                    if length >= dig > 0:
                        print()
                        console.rule(f"[bold][white]Запись удалена[/white][/bold]",
                                     style="#FFD700")
                        print()
                        return dig
                    else:
                        console.print(lex["incorrect_string_number"])
                except:
                    console.print(lex["incorrect_string_number"])


def search_rows_handler():
    "Обработчик, который проверяет валидность данных, прежде чем искать записи в файле"
    while True:
        console.print(lex["user_input_words_for_search"])
        words = input("--" + lex["user_input"])
        if words == "q":
            print()
            console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                         style="#FFD700")
            console.print(lex["config"])
            print()
            return False
        elif not words:
            console.print(lex["empty_words"])
        else:
            return words.split()


def settings_handler(user):
    "Обработчик, который устанавливает настройки юзера"

    console.print(lex["settings"])
    comma = input("--" + lex["user_input"])
    if comma == "q":
        print()
        console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                     style="#FFD700")
        console.print(lex["config"])
        print()
    if comma == "1":
        console.print("------ [white]Введите новое имя юзера:[/white]")
        user_input_1 = input("----" + lex["user_input"])
        user.username = user_input_1 if user_input_1 else "Пользователь"
        print()
        console.rule(f"[bold][white]{'Имя изменено'}[/white][/bold]",
                     style="#FFD700")
        print()
    elif comma == "2":
        while True:
            console.print(
                "------ [white]Изменить автозаполнение таблицы?[/white]\n------ [blue][Да | Нет][/blue]")
            user_input_1 = input("----" + lex["user_input"])
            if user_input_1 == "Да":
                if user.api:
                    user.api = False
                else:
                    user.api = True
                print()
                console.rule(f"[bold][white]{'Автозаполенение с помощью API включено' if user.api else 'Автозаполнение с помощью API отключено'}[/white][/bold]",
                             style="#FFD700")
                print()
                break
            elif user_input_1 == "Нет":
                print()
                break
            elif user_input_1 == "q":
                print()
                console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                             style="#FFD700")
                console.print(lex["config"])
                print()
                break
            else:
                console.print(lex["yes_or_no_error"])
    elif comma == "3":
        while True:
            console.print(
                "------ [white]Введите количество записей при автозаполнении:[/white]")
            user_input_1 = input("----" + lex["user_input"])
            if user_input_1 == "q":
                print()
                console.rule(f"[bold][white]{lex['exit']}[/white][/bold]",
                             style="#FFD700")
                console.print(lex["config"])
                print()
                break
            try:
                user_input_1 = int(user_input_1)
                if user_input_1 > 0:
                    user.count = user_input_1
                    print()
                    console.rule(f"[bold][white]{f'Настройки автозаполнения изменены'}[/white][/bold]",
                                 style="#FFD700")
                    print()
                    break
                else:
                    console.print(lex["less_zero_dig_error"])
            except:
                console.print(lex["input_correct_data"])
