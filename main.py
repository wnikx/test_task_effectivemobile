from phonebook_app.db_administration import manage

run = manage.AdminTable("Никита")

# run.add_rows()
# print(run.show_table())
# print(run.delete_row(frffr))
# print(run.show_table())
# print(run.show_table())
# run.show_table_pagination()
print(run.search_rows("Дмитрий"))
