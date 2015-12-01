import sqlite3   

def main():
    dbconnection = sqlite3.connect('data/ShazamDataModel.sqlite')
    cursor = dbconnection.cursor()
    results = cursor.execute(
        '''
        SELECT artistinfo.ZNAME, taginfo.ZTRACKNAME, taginfo.ZBEACON  
        FROM ZSHARTISTMO artistinfo 
        inner join ZSHTAGRESULTMO taginfo 
        on artistinfo.Z_PK = taginfo.Z_PK
        '''
    )

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