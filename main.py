#!/usr/bin/env python3

# import vk_api
from time import sleep
# import datetime
# import pytz
import sqlite3
# from threading import Thread
#
# timeout = 60
#
#
# class Status_thread(Thread):
#     """
#     A threading example
#     """
#     def __init__(self, Token, VKstatus):
#         """Инициализация потока"""
#         Thread.__init__(self)
#         self.Token = Token
#         self.VKstatus = VKstatus
#
#     def run(self, Token, VKstatus):
#         """Запуск потока"""
#
#         vk_session = vk_api.VkApi(token=self.Token)
#         vk = vk_session.get_api()
#         while True:
#             vk.status.set(text=status(self.VKstatus))
#             sleep(timeout)
#
#
#
# def get_time(tz='Europe/Moscow'):
#     return str(datetime.datetime.now(pytz.timezone(tz)).strftime("%H:%M"))
#
# def friends_online():
#     return str(len(vk.friends.getOnline()))
#
# def unread_count():
#     return str(vk.messages.getDialogs(unread= 1).get('count'))
#
# def status(status_vk= "Онлайн🔎: {friends_online}. Непрочитано✉: {unread}"):
#     return status_vk.format(time= get_time(), friends_online= friends_online(), unread= unread_count())

con = sqlite3.connect('userdb.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")

    while True:
        row = cur.fetchone()
        print(row)
        sleep(4)
