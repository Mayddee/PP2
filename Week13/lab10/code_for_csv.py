import psycopg2
from config import config

parameters = config()
connection = psycopg2.connect(**parameters)

query_clear="Delete from PhoneBook;" #очистить таблицу
query_create_user = "INSERT INTO PhoneBook (user_name, phone) VALUES (%s, %s) ;" #создаем пользователей

query_filter_by_name ="select*from PhoneBook ORDER BY user_name ASC;" #фильтруем
query_filter_by_name_madina ="select*from PhoneBook where user_name='Madina' or user_name='Aisulu' ;" #выводим пользователей

query_delete_by_name="Delete from PhoneBook where user_name='Madina';" #удаляем полтзователей
cursor = connection.cursor()

users = [
    ('Madina','870964536'),
    ('Aisulu','7856655154'),
    ('Zhansaya','785565555'),
    ('Arsen','456789652'),
]
cursor.execute(query_clear)
cursor.executemany(query_create_user, users) #метод позволяет выполнить одно выражение SQL для последовательности параметров

cursor.execute(query_filter_by_name_madina) #метод для выполнения одного выражения SQL

print(cursor.fetchall()) #озвращает данные, хранящиеся внутри таблицы, в виде строк


cursor.execute(query_delete_by_name)
cursor.execute(query_filter_by_name)
print(cursor.fetchall())


connection.commit() #Записать транзакцию
cursor.close() #немедленно закрывает курсор
connection.close() 