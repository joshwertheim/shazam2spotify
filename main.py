import sqlite3   

def main():
    dbconnection = sqlite3.connect('data/ShazamDataModel.sqlite')
    cursor = dbconnection.cursor()
    results = cursor.execute("SELECT ZBEACON as ID, ZTRACKNAME as TITLE FROM ZSHTAGRESULTMO")

    # for x in get_ids(results):
    #     print x

    print_rows(results)

    dbconnection.close()

def print_rows(rows):
    for row in rows:
        print row

def get_ids(results):
    ids = set()
    for id in results:
        ids.add(id[0])
    return list(ids)

if __name__ == '__main__':
    main()