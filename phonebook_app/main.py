from db_administration.manage import AdminTable
from lexicon.lexicon import lex
from rich.console import Console
from handlers import handlers

console = Console()


def start_session():
    user = AdminTable()
    console.rule(f"[bold][white]{lex['start']}[/white][/bold]",
                 style="#FFD700")
    console.print(f"{lex['config']}")
    start_work(user)


def start_work(user):
    while True:
        console.print(lex["user_comma"])
        user_input = input(lex["user_input"])
        if user_input == "q":
            console.rule(f"[bold][white]Удачи, {user.username}[/white][/bold]",
                         style="#FFD700")
            break
        elif user_input == '*':
            console.print(f"{lex['config']}")
        elif user_input == "1":
            user.show_table()
        elif user_input == "2":
            user.show_table_pagination()
        elif user_input == "3":
            page = handlers.show_page_handler(len(user.df))
            if page:
                user.show_table_page(page)
        elif user_input == "4":
            row = handlers.add_row_handler()
            if len(row) != 0:
                user.append_row(row)
        elif user_input == "5":
            result = handlers.update_row_handler(len(user.df), user.df.columns)
            if result:
                for column, value in result[1].items():
                    user.update_row(int(result[0]), column=column, value=value)
        elif user_input == "6":
            result = handlers.delete_row_handler(len(user.df))
            if result:
                user.delete_row(result)
        elif user_input == "7":
            result = handlers.search_rows_handler()
            if result:
                user.search_rows(result)
        elif user_input == "8":
            user.auto_add_rows()
            print()
            console.rule(f"[bold][white]{user.count} записей добавлено в таблицу![/white][/bold]",
                         style="#FFD700")
            print()
        elif user_input == "0":
            handlers.settings_handler(user)


if __name__ == "__main__":
    start_session()
