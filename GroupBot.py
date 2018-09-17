#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from time import sleep

vk_session = vk_api.VkApi(token='dd38b1ee28a878e995d013ddea790414f810f1573e2d1f99b710679940e71425354d49d7ff953ebd43eba')
vk = vk_session.get_api()

def write_msg(user_id, s):
    vk.messages.send(user_id= user_id, message= s)




def answer(user_id, text):
    '''
    Здесь должен быть обработчик сообщений
    https://vk.cc/8tPksu
    ссылка для получения токена, её нужно отправить пользователю
    '''


# обработчик событий, запускает функцию answer, когда боту поступает сообщение, передаёт функции ID пользователя и текст сообщения
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text
        user_id = event.user_id
        answer(user_id, text)
