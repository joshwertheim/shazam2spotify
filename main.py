import sqlite3
from ConfigParser import SafeConfigParser

class Track(object):
    """docstring for Track"""
    def __init__(self, artist, trackname, id):
        self.artist = artist
        self.trackname = trackname
        self.id = id 

def main():
    tracks = get_query_results()
    print_tracks(tracks)

def get_db_path():
    config_parser = SafeConfigParser()
    config_parser.read('config.txt')
    dir_path = config_parser.get('options', 'dir')
    return dir_path

def get_query_results():
    dir_path = get_db_path()
    dbconnection = sqlite3.connect(dir_path)
    cursor = dbconnection.cursor()
    results = cursor.execute(
        '''
        SELECT artistinfo.ZNAME, taginfo.ZTRACKNAME, taginfo.ZBEACON  
        FROM ZSHARTISTMO artistinfo 
        inner join ZSHTAGRESULTMO taginfo 
        on artistinfo.Z_PK = taginfo.Z_PK
        '''
    )

    tracks = get_tracks(results)
    dbconnection.close()
    return tracks

def print_rows(rows):
    for row in rows:
        print row

def get_ids(results):
    ids = set()
    for id in results:
        ids.add(id[0])
    return list(ids)

def get_tracks(results):
    tracks = list()
    for song in results:
        track = Track(song[0], song[1], song[2])
        tracks.append(track)
    return tracks

def print_tracks(tracks):
    for t in tracks:
        print t.artist, t.trackname, t.id

if __name__ == '__main__':
    main()