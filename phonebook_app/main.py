from db_administration.manage import AdminTable
from lexicon.lexicon import lex
from rich.console import Console
from rich import print

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


if __name__ == "__main__":
    start_session()
