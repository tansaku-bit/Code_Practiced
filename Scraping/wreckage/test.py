from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ブラウザを起動するためのオプションを設定
options = Options()
options.add_argument('--headless') # ヘッドレスモードを有効にする（コメントアウトするとブラウザが表示される）
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Chromeドライバーを起動する
driver = webdriver.Chrome(options=options)

# URLを指定してページを取得する
url = 'https://www.pixiv.net/artworks/106962433'
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

print(tags)

# ブラウザを終了する
driver.quit()