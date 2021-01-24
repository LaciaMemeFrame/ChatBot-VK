# -*- coding: utf-8 -*-

import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload 

session = requests.Session()
vk_session = vk_api.VkApi(token='токен')

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)
dog = []
kitty = []
wallpaper = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:		
        if event.text == u'Начать':
            if event.from_user: 
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=u'IP Сервера: 159.69.218.29:7777\nВсе команды выводятся командой !хелп'
		    
		)
            elif event.from_chat: 
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message=u'IP Сервера: 159.69.218.29:7777\nВсе команды выводятся командой !хелп'
		)

        if event.text == u'!хелп': 
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=u'!китти, !догс, !обои'
        )
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message=u'!китти, !догс, !обои'
        )

        if event.text == u'!китти':
            if event.from_user:
                url = 'https://api.thecatapi.com/v1/images/search'
                r = requests.get(url, allow_redirects=True)
                r.headers['x-api-key'] = 'токен'
                json = r.json()
                for j in json:
                    kittyurl = j['url']
                    rs = requests.get(kittyurl, allow_redirects=True)
                    image_url = kittyurl
                    image = session.get(image_url, stream=True)
                    photo = upload.photo_messages(photos=image.raw)[0]
                    kitty.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )
                print('photo{}_{}'.format(photo['owner_id'], photo['id']))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    attachment=kitty
                )
                kitty.clear()
        
        if event.text == u'!догс':
            if event.from_user:
                url = 'https://api.thedogapi.com/v1/images/search'
                r = requests.get(url, allow_redirects=True)
                r.headers['x-api-key'] = 'токен'
                json = r.json()
                for j in json:
                    dogsurl = j['url']
                    rs = requests.get(dogsurl, allow_redirects=True)
                    image_url = dogsurl
                    image = session.get(image_url, stream=True)
                    photo = upload.photo_messages(photos=image.raw)[0]
                    dog.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )
                print('photo{}_{}'.format(photo['owner_id'], photo['id']))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    attachment=dog
                )
                dog.clear()

        if event.text == u'!обои':
            if event.from_user:
                url = 'https://nekos.life/api/v2/img/wallpaper'
                r = requests.get(url, allow_redirects=True)
                r.headers
                json = r.json()
                pussyurl = json['url']
                rs = requests.get(pussyurl, allow_redirects=True)
                image_url = pussyurl
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                wallpaper.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )
                print('photo{}_{}'.format(photo['owner_id'], photo['id']))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    attachment=wallpaper
                )
                wallpaper.clear()


if   __name__ == "__main__":
    print('Работает!')
    event()
    while True:
        event()