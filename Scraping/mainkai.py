#ライブラリのimport
import requests
from bs4 import BeautifulSoup
import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#別ファイルのimport

baseurl = "https://www.pixiv.net/artworks/"

#with open('set.txt', 'r') as f:
#    text = f.read()
#    start_id, end_id = map(int, text.strip()[1:-1].split(', '))
start_id = 1
end_id = 100000
delay = 0.5
ids = []


connect_db = sqlite3.connect('dataset.db')

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

def get_tags(url):
    # ブラウザを起動するためのオプションを設定
    options = Options()
    options.add_argument('--headless') # ヘッドレスモードを有効にする（コメントアウトするとブラウザが表示される）
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Chromeドライバーを起動する
    driver = webdriver.Chrome(options=options)

    # URLを指定してページを取得する
    driver.get(url)

    # ページのHTMLをBeautifulSoupでパースする
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tags = []

    # ulタグの中身を取得する
    ul = soup.find('ul', {'class': 'sc-pj1a4x-0 gZfuPH'})
    for li in ul.find_all('li'):
        a_tag = li.find('a')
        if a_tag:
            tag_text = a_tag.text
            tags.append(tag_text)

    # ブラウザを終了する
    driver.quit()

    return tags


for id in range(start_id, end_id + 1):
    url = baseurl + str(id)
    response = requests.get(url)
    if response.status_code == 404 or "このページは限定公開されています" in response.text:
        print("Skipping " + url)
    else:
        tags = get_tags(url)
        tags = ','.join(tags)
        insert_data(id, url, tags)
        ids.append(id)
        print("Added " + str(id))
    time.sleep(delay)

connect_db.close()