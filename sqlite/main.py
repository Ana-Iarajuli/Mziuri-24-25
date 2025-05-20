import sqlite3


def connection(file):
    return sqlite3.connect(file)

def fetch_all(conn):
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM books").fetchall()
    for record in result:
        print(record)

def delete_author(conn):
    cursor = conn.cursor()


def main():
    conn = connection("books.sqlite")
    fetch_all(conn)
    conn.close()

if __name__ == "__main__":
    main()

# conn.row_factory = sqlite3.Row

cursor.execute('''CREATE TABLE books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
author VARCHAR(100),
price FLOAT
);
''')

# cursor.execute('''
# INSERT INTO books (title, author, price)
# VALUES ('Hamlet', 'William Shakespeare', 10.5);
# ''')


# b_title = "Animal Farm"
# b_author = "George Orwell"
# b_price = 11.2


# book1 = ("1984", "George Orwell", 10)
# cursor.execute('INSERT INTO books (title, author, price) '
#                'VALUES (?, ?, ?)', book1)


# book_list = [
#             ('The Book Thief', 'Markus Zusak', 17 ),
#             ('Animal Farm', 'George Orwell', 13 ),
#             ('The Hunger Games', 'Suzanne Collins', 17 ),
#             ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
#             ('Harry Potter and the Goblet of Fire', 'Rowling', 24 ),
#             ('გამზრდელი', 'აკაკი წერეთელი', 8),
#             ('ჩემი თავგადასავალი', 'აკაკი წერეთელი', 8),
#             ('განდეგილი', 'ილია ჭავჭავაძე', 10 ),
#             ('ვეფხისტყაოსანი', 'შოთა რუსთაველი', 29)
#         ]

# cursor.executemany('INSERT INTO books (title, author, price) VALUES (?,?,?)', book_list)
# conn.commit()

# result = cursor.execute("SELECT * FROM books").fetchone()
# record = cursor.fetchone()
# print("Title = ", record[1])
# record = cursor.fetchone()
# print("Title = ", record[1])
# records = cursor.fetchall()
# # records = cursor.fetchmany(2)
# print(result)
# for record in result:
#     print(record)
    # print(f"Title is {record['title']} by {record['author']}")


# pr_value = 13
# author_name = "Rowling"
# cursor.execute("SELECT * FROM books WHERE price>:pr AND author=:author",
#                {'pr': pr_value, 'author': author_name})
# records = cursor.fetchall()
# for record in records:
#     print(record)


# query = 'UPDATE books SET price=12 WHERE author="Rowling"'
# cursor.execute(query)
# info = 'SELECT * FROM books'
# cursor.execute(info)
# print(cursor.rowcount)
# conn.commit()
# records = cursor.fetchall()
# for record in records:
#     print(record)


# # DELETE
# query = 'DELETE FROM books WHERE author="Rowling"'
# cursor.execute(query)
# print(cursor.rowcount)
#
# conn.commit()

# conn.close()
