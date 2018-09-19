#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
from time import sleep
import sqlite3
from threading import Thread


class User(Thread):
    def __init__(self, token, status_vk):
        Thread.__init__(self)
        self.token = token
        self.status_vk = str(status_vk)
        self.timeout = 60
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()

    def friends_online(self):
        return str(len(self.vk.friends.getOnline()))

    def unread_count(self):
        return str(self.vk.messages.getDialogs(unread= 1).get('count'))

    def status_text(self,status_vk):
        return status_vk.format(friends_online= self.friends_online(), unread= self.unread_count())

    def run(self):
        while True:
            self.vk.status.set(text=self.status_text(self.status_vk))
            sleep(self.timeout)

conn = sqlite3.connect('DB.db')
c = conn.cursor()

DB = c.execute('select * from user').fetchall()
last_rowid = len(DB)
for user in DB:
    token = user[1]
    status_vk = user[2]
    User(token, status_vk).start()

while True:
    next_rowid = last_rowid + 1
    next_data = c.execute('SELECT * FROM user WHERE rowid=?', str(next_rowid)).fetchall()
    if next_data != []:
        token = next_data[0][1]
        status_vk = next_data[0][2]
        print(token + ' ' + status_vk)
        User(token, status_vk).start()
        last_rowid += 1
    sleep(1)
