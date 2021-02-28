import telegram
import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
import json
import mapper

now = datetime.datetime.now()

token = '1524068848:AAFhmxo3iPasbCiGKYdSu5fO-wrWGZ6WQz0'

bot = telegram.Bot(token=token)

url1 = 'https://gall.dcinside.com/board/lists'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


word_arr = []

for page in range(1, 11):
    params = {
        'id': 'bitcoins',
        'page': str(page)
    }

    webpage = requests.get(url1, params=params, headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(webpage.content, "html.parser")

    _list = soup.select('td.gall_tit')

    for item in _list:
        words = item.text.split(' ')

        for word in words:
            word_arr.append(word)


json_obj = dict()
for item in word_arr:
    item_str = item.replace('\n', '').replace('\n', '')
    item_str = re.sub('\[[0-9]*\]', '', item_str)

    if item_str == '':
        continue

    if item_str in json_obj:
        json_obj[item_str] = json_obj[item_str] + 1
    else:
        json_obj[item_str] = 1


tmp_arr = []
for item in json_obj:
    tmp_obj = dict()
    tmp_obj['title'] = item
    tmp_obj['count'] = json_obj[item]
    tmp_arr.append(tmp_obj)


for i in range(0, len(tmp_arr)):
    for j in range(i+1, len(tmp_arr)-1):
        if(tmp_arr[j]['count'] > tmp_arr[i]['count']):
            tm = tmp_arr[i]
            tmp_arr[i] = tmp_arr[j]
            tmp_arr[j] = tm


message_text = "현재 빗갤러들은 어떤 이야기를 하며 인생을 낭비하고 있을까요?\n"
message_text += "====================================\n"
message_text += "수집시간 : " + str(now) + "\n"
message_text += "수집데이터 : 빗갤 1~10 페이지\n"
message_text += "====================================\n"

cnt = 1
url_arr = []
for item in tmp_arr:
    if item['count'] > 10:
        url_arr.append(item['title'])
        message_text += str(cnt) + ". " + \
            str(item['title']) + ",    " + \
            "언급횟수 : " + str(item['count']) + "\n"

        cnt += 1

message_text += "====================================\n"

url2 = "https://api.upbit.com/v1/ticker?markets=" + \
    mapper.get_url_query(url_arr)
price_info = requests.get(url2).content
price_json = json.loads(price_info)

for item in price_json:
    message_text += mapper.get_coin_name(item['market']) + \
        " : " + str(item['trade_price']) + "원\n"


print(message_text)


chat_ids = ['1581809877', '1514697082']
for bs in chat_ids:
    bot.send_message(chat_id=bs, text=message_text)
