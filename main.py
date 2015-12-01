import sqlite3

def main():
    dbconnection = sqlite3.connect('data/ShazamDataModel.sqlite')
    cursor = dbconnection.cursor()
    results = cursor.execute("SELECT * FROM ZSHTAGRESULTMO")

def print_rows(rows):
    for row in rows:
        print row

if __name__ == '__main__':
    main()