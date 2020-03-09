# -*- coding: utf-8 -*-

import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='token')

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == u'Начать': #or event.text == u'Начать': Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=u'IP: 34.91.233.9:7777 Полезные ссылки: Наш сайт - laciamemeframe.space (Сайт создателя проекта, так как сайт самого сервера находится в разработке). Форум - В разработке, Группа "Вконтакте" - https://vk.com/pixsetup, Свободная группа "Вконтакте" - В разработке. IP: 34.91.233.9:7777'
		    
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message=u'IP: 34.91.233.9:7777 Полезные ссылки: Наш сайт - laciamemeframe.space (Сайт создателя проекта, так как сайт самого сервера находится в разработке). Форум - В разработке, Группа "Вконтакте" - https://vk.com/pixsetup, Свободная группа "Вконтакте" - В разработке. IP: 34.91.233.9:7777'
		  
		)

    if requests[0:5] == u'!бан'  and event.user.id  in event.admin:
           
           try:
           
                vk.messages.removeChatUser(chat_id=event.chat_id, user_id=requests[5:])
           
           except:
           
                event.text(vk, event.chat_id, u'Шо то не так, попробуй указать правильный ID пользователя.')

           id = requests[5:]
           addBanUser = open('banlist.txt', 'a')
           addBanUser.write(id + '\n')
           addBanUser.close()

    if event.type == VkChatEventType.USER_JOINED and event.from_chat:

        user_id = event.object.get('from_id')
        chat_id = event.chat_id

        with open('banlist.txt', 'a') as CheckBanUsers:
            id = CheckBanUsers.readlines()

        if user_id in id:

            vk.messages.send(
                chat_id=chat_id,
                message=u'Извините, вам запрещено тут находиться. Вы были забанены.'
            )

            vk.messages.removeChatUser(
                chat_id=chat_id,
                user_id=user_id
            )
				
if if __name__ == "__main__":
    main(