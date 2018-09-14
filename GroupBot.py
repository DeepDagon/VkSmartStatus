#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from time import sleep
import sqlite3

#DATABASE
DB = sqlite3.connect("userdb.db")
cur = DB.cursor()
#DATABASE



vk_session = vk_api.VkApi(token='dd38b1ee28a878e995d013ddea790414f810f1573e2d1f99b710679940e71425354d49d7ff953ebd43eba')
vk = vk_session.get_api()

def write_msg(user_id, s):
    vk.messages.send(user_id= user_id, message= s)




def answer(user_id, text):
    status = '''Онлайн🔎: {friends_online}. Непрочитано✉: {unread}'''
    if 'помощь' in text.lower():
        help = open("help.txt","r")
        message = help.read()
        help.close()
        write_msg(user_id, message)
    elif 'часовые пояса' in text.lower():
        timezones = open("timezones.txt","r")
        message = timezones.read()
        timezones.close()
        write_msg(user_id, message)
    elif 'статус:' in text.lower():
        status = text[8:]
    elif 'https://oauth.vk.com/blank.html#access_token=' in text.lower():
        s = text.split('#')[1].split('&')
        access_token = s[0].split('=')[1]
        args = (access_token, status, user_id)
        cur.execute("UPDATE Users SET Token = ? AND SET Status = ? WHERE Id = ?", args)

        # args = (user_id, access_token, status)
        # cur.execute("INSERT INTO Users VALUES(?, ?, ?)", args)
        DB.commit()
        message = 'Всё в порядке'
    elif 'secret' in text.lower():
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        write_msg(user_id, 'Я вас не понимаю, напишите "помощь"')



longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text
        user_id = event.user_id
        answer(user_id, text)
