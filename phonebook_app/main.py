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
    while True:
        user_input = input()
        if user_input == "q":
            break
        elif user_input == '*':
            console.print(f"{lex['config']}")
        elif user_input == "1":
            user.show_table()
        elif user_input == "2":
            user.show_table_pagination()
        elif user_input == "3":
            page = handlers.show_page_handler(len(user.df))
            user.show_table_page(page)
        elif user_input == "4":
            row = handlers.add_row_handler()
            user.append_row(row)
        elif user_input == "8":
            user.auto_add_rows(len(user.df))


if __name__ == "__main__":
    start_session()
