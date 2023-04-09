#ライブラリのimport
import requests
from bs4 import BeautifulSoup
import time
import sqlite3

#別ファイルのimport
import gettags

baseurl = "https://www.pixiv.net/artworks/"
start_id = 18
end_id = 24
delay = 1
ids = []


connect_db = sqlite3.connect('test.db')

cursor = connect_db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS table_name (
        id INTEGER PRIMARY KEY,
        artworks_number INTEGER,
        url text,
        tags text
    )
    ''')

def insert_data(artworks_number, url, tags):
    #tags_str = ','.join(tags)
    cursor.execute('''INSERT INTO table_name (artworks_number, url, tags) VALUES (?, ?, ?)''', (artworks_number, url, tags))
    connect_db.commit()

#browserを起動
gettags.start_browser()


for id in range(start_id, end_id + 1):
    url = baseurl + str(id)
    response = requests.get(url)
    if response.status_code == 404 or "このページは限定公開されています" in response.text:
        print("Skipping " + url)
    else:
        tags = gettags.get_tags(url)
        tags = ','.join(tags)
        insert_data(id, url, tags)
        ids.append(id)
        print("Added " + str(id))
    time.sleep(delay)

connect_db.close()
gettags.close_browser()

print(ids)