# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3


def print_message(message):
    # Use a breakpoint in the code line below to debug your script.
    print(message)  # Press Ctrl+F8 to toggle the breakpoint.


def read_sqlite(dbname):
    try:
        conn = sqlite3.connect(dbname)
        print_message('DB was created or connected')
        return conn
    except:
        print_message('DB was not created')


def add_new_row():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_message('Start program')
    sqliteconn = read_sqlite('test.db')
    cur = sqliteconn.cursor()
    # sqlrequest = """CREATE TABLE IF NOT EXISTS users(userid INT PRIMARY KEY, fname TEXT, lname TEXT, gender TEXT);"""
    # try:
    #     cur.execute(sqlrequest)
    #     sqliteconn.commit()
    #     print_message('Table was created')
    # except:
    #     print_message('Table was not created')
    # sqlrequest = """INSERT INTO users(userid, fname, lname, gender) VALUES('00002', 'Alex', 'Smith', 'male');"""
    # try:
    #     cur.execute(sqlrequest)
    #     sqliteconn.commit()
    #     print_message('Data was added')
    # except:
    #     print_message('Data was not added')
    cur.execute("SELECT * FROM users WHERE userid = 1;")
    all_results = cur.fetchall()
    print(all_results)




