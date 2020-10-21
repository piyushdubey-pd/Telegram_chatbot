# -*- coding: UTF8 -*-
import requests
import datetime



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '953196435:AAFBgwQsVewPGMqPSujTZ_mvXOT0jwnsHNA' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')
    z=0
    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
                if z == 0:
                    magnito_bot.send_message(first_chat_id, 'Hello there!!!!!')
                    magnito_bot.send_message(first_chat_id,
                                             ' Thank you for dedicating your attention towards this project.')
                    magnito_bot.send_message(first_chat_id,
                                             ' It is under development process, still you can try it with some basic yellow circle emojis and media files. ')
                    magnito_bot.send_message(first_chat_id, 'Welcome, and Thank you for cooperating ' + first_chat_name)
                    new_offset = first_update_id + 1
                    z=1
                if first_chat_text == 'Hello' or first_chat_text == 'Hi' or first_chat_text == 'Hey' :
                    magnito_bot.send_message(first_chat_id, 'Hi, how are you doing ' + first_chat_name)
                    new_offset = first_update_id + 1
                emoji = {
                '😄':'smile',
                '😆':'laughing',
                "😊":"blush",
                '😃':'smiley',
                '☺️': 'relaxed',
                '😏':"smirk",
                '😍':"heart eyes",
                '😘':"kissing heart",
                '😚':"kissing closed eyes",
                '😳':"flushed",
                '😌':"relieved",
                '😆':"satisfied",
                '😁':"grin",
                '😉':"wink",
                '😜':"stuck out tongue winking eye",
                '😝':"stuck out tongue closed eyes",
                '😀':"grinning",
                '😗':"kissing",
                '😙':"kissing smiling eyes",
                '😛':"stuck out tongue",
                '😴':"sleeping",
                '😟':"worried",
                '😦':"frowning",
                '😧':"anguished",
                '😮':"open_mouth",
                '😬':"grimacing",
                '😕':"confused",
                '😯':"hushed",
                '😑':"expressionless",
                '😒':"unamused",
                '😅':"sweat_smile",
                '😓':"sweat",
                '😥':"disappointed relieved",
                '😩':"weary",
                '😔':"pensive",
                '😞':"disappointed",
                '😖':"confounded",
                '😨':"fearful",
                '😰':"cold_sweat",
                '😣':"persevere",
                '😢':"cry",
                '😭':"sob",
                '😂':"joy",
                '😲':"astonished",
                '😱':"scream",
                '😫':"tired_face",
                '😠':"angry",
                '😡':"rage",
                '😤':"triumph",
                '😪':"sleepy",
                '😋':"yum",
                '😷':"mask",
                '😎':"sunglasses",
                '😵':"dizzy_face",
                '👿':"imp",
                '😈':"smiling_imp",
                '😐':"neutral_face",
                '😶':"no_mouth",
                '😇':"innocent",
                '☺️':"shy",
                '🤣': "rofl",
                '🥰':"heartfelt"
                }
                x=first_chat_text[0]
                if x in emoji :
                    magnito_bot.send_message(first_chat_id, emoji[x])
                    new_offset = first_update_id + 1
                    break
                if 'photo' in current_update['message']:
                    magnito_bot.send_message(first_chat_id, 'Nice picture')
                    new_offset = first_update_id + 1
                    break
                if 'video' in current_update['message']:
                    magnito_bot.send_message(first_chat_id, 'Wow, I am amazed.')
                    magnito_bot.send_message(first_chat_id, 'Thank you for sharing this video '+ first_chat_name)
                    new_offset = first_update_id + 1
                    break
                else:
                    magnito_bot.send_message(first_chat_id, 'Sorry, this input is not defined yet '+first_chat_name)
                    new_offset = first_update_id + 1



#if  0 < current_update['message']['photo'][0]['file_size'] :
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()