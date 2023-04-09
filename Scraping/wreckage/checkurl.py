import requests
import time

baseurl = "https://www.pixiv.net/artworks/"
start_id = 1
end_id = 50
delay = 0.5
ids = []

for id in range(start_id, end_id + 1):
    url = baseurl + str(id)
    response = requests.get(url)
    if response.status_code == 404 or "このページは限定公開されています" in response.text:
        print("Skipping " + url)
    else:
        ids.append(id)
        print("Added " + str(id))
    time.sleep(delay)

print(ids)