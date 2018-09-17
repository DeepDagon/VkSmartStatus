#!/usr/bin/env python3

import vk_api
from time import sleep
from threading import Thread

timeout = 60

Token = 'token'

vk_session = vk_api.VkApi(token=Token)
vk = vk_session.get_api()


def friends_online():
    return str(len(vk.friends.getOnline()))

def unread_count():
    return str(vk.messages.getDialogs(unread= 1).get('count'))

def status(status_vk= "Онлайн🔎: {friends_online}. Непрочитано✉: {unread}"):
    return status_vk.format(friends_online= friends_online(), unread= unread_count())

while True:
    vk.status.set(text=status())
    sleep(timeout)
