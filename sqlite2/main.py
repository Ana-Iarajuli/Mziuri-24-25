import sqlite3


def connection(file):
    return sqlite3.connect(file)


def fetch_female(conn, gender):
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM Passengers WHERE sex=:gender", {"gender": gender}).fetchall()
    # for record in result:
    #     print(record)
    print(len(result))


def main():
    conn = connection("Titanic.sqlite")
    fetch_female(conn, "female")
    fetch_female(conn, "male")
    conn.close()



if __name__ == "__main__":
    main()