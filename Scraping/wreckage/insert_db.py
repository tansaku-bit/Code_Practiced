#ライブラリのimport
import requests
import time
import sqlite3

baseurl = "https://www.pixiv.net/artworks/"
start_id = 15
end_id = 25
delay = 1
ids = []

tags = "test, images, picture"

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

for id in range(start_id, end_id + 1):
    url = baseurl + str(id)
    response = requests.get(url)
    if response.status_code == 404 or "このページは限定公開されています" in response.text:
        print("Skipping " + url)
    else:
        insert_data(id, url, tags)
        ids.append(id)
        print("Added " + str(id))
    time.sleep(delay)

connect_db.close()
print(ids)