#!/usr/bin/python
# coding=utf-8
import sys
import telepot
from urllib.request import urlopen
from datetime import datetime
import traceback


TOKEN = '582476203:AAGzs4MiO0qXoRxCeo51uRWD009sb6wUgZ4'
MAX_MSG_LENGTH = 300
baseurl ='http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidGeneralWeatherCondition?ServiceKey=QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D&stnId=108'
bot = telepot.Bot(TOKEN)


def getData():
    res_list =[]
    url = baseurl
    print(url)
    res_body = urlopen(url).read()
    print(res_body)
    from xml.etree import ElementTree
    root = ElementTree.fromstring(res_body)
    for child in root.iter('item'):
        btime = child.find('tmFc').text  # 발표시간
        today = child.find('wfSv1').text  # 오늘 날씨

        row = '발표시간은=' + btime+'\n오늘 날씨 = '+today
        if row:
            res_list.append(row.strip())
    return res_list


def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)


def replyAptData(user):
    print(user)
    res_list = getData()
    msg = ''
    for r in res_list:
        print(str(datetime.now()).split('.')[0], r )
        if len(r + msg) + 1 > MAX_MSG_LENGTH:
            sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        sendMessage(user, msg )
    else:
        sendMessage(user, '기간에 해당하는 데이터가 없습니다.')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('날씨 조회') and len(args) > 1:
        print('try to 날씨 조회')
        replyAptData(chat_id)
    else:
        sendMessage(chat_id, '''메뉴 입력하세요.\n''')
