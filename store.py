from instabot import Bot
import telebot
from telebot import types
import requests

bot = telebot.TeleBot("1477680087:AAFGTuSpqSMOgmHQ0YhhpDwG2m9UzEEg99k")
j = Bot()
j.login(username='88.bq', password='ahmed2000koky')
r1 = requests.session()
idi = 209501902
open('down.txt', 'a').write('')


def login():
    global ig_did, csrftoken, sessionid
    username = ("xc26.zp")
    password = ('qqqq1111')
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
    login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
    print(login_to_acc.text)


login()


@bot.message_handler(commands=['start'])
def key(msg):
    if f'{msg.chat.id}\n' in open('down.txt', 'r'):
        pass
    else:
        open('down.txt', 'a').write(f'{msg.chat.id}\n')
    q = types.InlineKeyboardMarkup()
    q1 = types.InlineKeyboardButton("صوره الشخصية 💫", callback_data='q1')
    q2 = types.InlineKeyboardButton("تحميل من الاستوري ♻️", callback_data='q2')
    q3 = types.InlineKeyboardButton("تحميل مقطع فيديو 🎥", callback_data='q3')
    q4 = types.InlineKeyboardButton("تحميل صور متحركة من الويب 📡", callback_data='q4')
    q.add(q1, q2)
    q.add(q3, q4)
    bot.send_message(msg.chat.id, 'اهلا و سهلا بك ايها المستخدم في بوت التحميل ✨', reply_markup=q)


@bot.callback_query_handler(lambda call: True)
def any(call):
    if call.data == 'q1':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل صورته الشخصية 🌀", reply_markup=markup)
    if call.data == 'q2':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل استوري الحساب ☄️", reply_markup=markup)
    if call.data == 'q3':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل مقطع الفيديو من الحساب 👁‍🗨",
                         reply_markup=markup)
    if call.data == 'q4':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل الكلمة التي تريد الحصول على صور المتحركة ❇️",
                         reply_markup=markup)
    if 'a' == call.data[:1]:
        try:
            if f'{call.message.chat.id}' in h:
                if call.data == 'a1':
                    i = 15
                    d = 21
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a2')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
                if call.data == 'a2':
                    i = 25
                    d = 31
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a3')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
                if call.data == 'a3':
                    i = 35
                    d = 41
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a4')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
                if call.data == 'a4':
                    i = 45
                    d = 51
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a5')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
                if call.data == 'a5':
                    i = 55
                    d = 61
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a6')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
                if call.data == 'a6':
                    i = 65
                    d = 71
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a7')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1

                if call.data == 'a7':
                    i = 75
                    d = 81
                    while i < d:
                        try:
                            a = telebot.types.InlineKeyboardMarkup()
                            a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a')
                            c = v.split('.gif"')[i]
                            a.add(a1)
                            n = c.split('["https://')[-1]
                            if len(n) < 55:
                                if i == d - 1:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif', reply_markup=a)
                                else:
                                    bot.send_message(call.message.chat.id, f'https://{n}.gif')
                            else:
                                d += 1

                        except:
                            pass
                        i += 1
            else:
                bot.send_message(call.message.chat.id, 'اضغط مره اخرى لاعادة المحاولة /start')
        except:
            pass
        if call.data == 'q6':
            i = 5
            try:
                while True:
                    bot.send_message(call.message.chat.id, n.split('video_url')[i][
                                                           n.split('video_url')[1].find('https:'):
                                                           n.split('video_url')[1].find('video_view_count') - 4])
                    i += 1
            except:
                pass

@bot.message_handler(content_types='text')
def an(msg):
    global n
    global v
    try:
        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل صورته الشخصية 🌀":
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
            }
            INSTA_URL = "https://www.instagram.com/"
            USER_ID = msg.text
            TAIL = "/?__a=1"
            URL = INSTA_URL + USER_ID + TAIL
            response = r1.get(URL).json()
            n = str(response['graphql']['user']['edge_owner_to_timeline_media']['edges'])
            hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]
            bot.send_message(msg.chat.id, hd_image_location)
    except:
        pass
    try:

        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل مقطع الفيديو من الحساب 👁‍🗨":

            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            }
            INSTA_URL = "https://www.instagram.com/"
            USER_ID = msg.text
            TAIL = "/?__a=1"
            URL = INSTA_URL + USER_ID + TAIL
            response = r1.get(URL, headers=header).json()
            if '{}' in str(response):
                bot.reply_to(msg, 'لا يمكننا الوصول لهذا اليوزر ❌')
            if "is_private': True" in str(response):
                bot.reply_to(msg, 'هذا الحساب برايفد 🤙🏼')
            else:

                n = str(response['graphql']['user']['edge_owner_to_timeline_media']['edges'])
                if 'video_url' in n:
                    v = n[n.find('video_url') + 13:]
                    i = 1
                    while i < 5:
                        if i == 4:
                            try:
                                print(n.split('video_url')[i + 1][
                                      n.split('video_url')[1].find('https:'):n.split('video_url')[1].find(
                                          'video_view_count') - 4])
                                q = types.InlineKeyboardMarkup()
                                q1 = types.InlineKeyboardButton('المزيد ♐️', callback_data='q6')
                                q.add(q1)
                                bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                                   n.split('video_url')[1].find('https:'):
                                                                   n.split('video_url')[1].find(
                                                                       'video_view_count') - 4], reply_markup=q)
                            except:
                                bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                                   n.split('video_url')[1].find('https:'):
                                                                   n.split('video_url')[1].find(
                                                                       'video_view_count') - 4])
                        else:
                            bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                               n.split('video_url')[1].find('https:'):
                                                               n.split('video_url')[1].find('video_view_count') - 4])

                        i += 1
                else:
                    bot.reply_to(msg, 'عفوا هذا اليوزر لا يحتوي على فيديوهات ️⚠️')
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل استوري الحساب ☄️":
            try:
                v = str(j.get_user_stories(user_id=j.convert_to_user_id(usernames=msg.text)))
            except:
                pass
            try:
                if v == '([], [])':
                    bot.reply_to(msg, 'تاكد من اليوزر الذي ارسلته')
                else:
                    i = 0
                    while i < len(v) + 1:
                        try:
                            bot.send_message(msg.chat.id, v.split(',')[i])
                        except:
                            pass
                        i += 1
            except:
                bot.reply_to(msg, 'تاكد من اليوزر الذي ارسلته')
    except:
        pass
    try:
        if msg.text == 'الاعضاء' and msg.chat.id == idi:
            x = open('down.txt', 'r').readlines()
            bot.reply_to(msg, '{}'.format(len(x)))
    except:
        pass
    try:
        if msg.text == 'الاذاعة' and msg.chat.id == idi:
            markup = types.ForceReply(selective=False)
            bot.send_message(msg.chat.id, "ارسل اذاعتك", reply_markup=markup)
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل اذاعتك":
            s = msg.text
            x = open('down.txt', 'r').readlines()
            z = 0
            try:
                while z < len(x):
                    if str(x[z]) == '\n':
                        pass
                    else:
                        bot.send_message(x[z], s)
                    z += 1
            except:
                pass
    except:
        pass
    global h, w
    try:
        if msg.reply_to_message.text == "ارسل الكلمة التي تريد الحصول على صور المتحركة ❇️":
            w = f'gif {msg.text}'
            h = f'{w}{msg.chat.id}'
            bot.send_message(idi, f'{msg.text}// @{msg.from_user.username}')
            url = f'https://www.google.com/search?q={w}&tbm=isch&ved=2ahUKEwi4iazyrKHtAhVSLxoKHV-mCrUQ2-cCegQIABAA&oq=sexy&gs_lcp=CgNpbWcQAzoHCAAQsQMQQzoECAAQQzoFCAAQsQM6CAgAELEDEIMBOgIIAFCVlB1YgZ8dYIGxHWgAcAB4AIABywKIAdkHkgEFMi0zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=gjjAX7jANdLeaN_MqqgL&bih=597&biw=557&hl=ar'
            head = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; HSID=ACpCi--xKNWBuzc1V; SSID=AxTv5nnKkxKd-t24h; APISID=OvtsQIlYX38DaDAB/AejTrmzLNAmxJKW5L; SAPISID=VictV1NMEEknSmKC/Ap3tCyc9Rw-nNhkKN; __Secure-3PAPISID=VictV1NMEEknSmKC/Ap3tCyc9Rw-nNhkKN; CONSENT=YES+IQ.ar+201908; SEARCH_SAMESITE=CgQIoJAB; OTZ=5713657_44_44__44_; SID=3gekKKpt2BDYs3HGt2dbGMJygRXv0S_uH30dI87nwwd9kPVGeJPLKTJluqScaUfUXXkqGg.; __Secure-3PSID=3gekKKpt2BDYs3HGt2dbGMJygRXv0S_uH30dI87nwwd9kPVGofFKYNMh0FN74vl_7RXMLg.; ANID=AHWqTUl-D-kiT0ekElpQYvwaLkYpmfjEj0_vWVNyeQ9lR3vPGLYG1ea_vAtrh9jw; 1P_JAR=2020-11-26-23; NID=204=Nvh8sYQiAGl2xGl9Rivw7mwHK0oiirbBuBjelwbKer7spRkQS3Xh-9GYO5GR2WOwUG-GICaT4wz4vP8fWCpH8Zao3AEmb_XGvZ7CoLvMiTCbcSnMjY6GCGnFcwc9Ap2D0Iu1ltcyj4qzLl25BPgZf0KdrrpVYB_UyBb_LrJWA7A4dgrtBLEwtyBFzHe1XdYKS_yOA6QzeeHlNNtZm2YYpYUzvzevK2wxD2EMs9f9OOnq_es; DV=Q77RAgvgUI1KQP_f7OZE3e4dEcltYJdw4P5MyRCtgwEAAHAXk3Gqw6shngAAAAyZb21iQXUwRQAAAA; SIDCC=AJi4QfGRLCnLLJayzTS67kgRZvvsMJ8WJx4Z3VQIypirxBw8XSvY82_9ydx6j9Wr0SSSgWwkPw; __Secure-3PSIDCC=AJi4QfFg7EgRAZ_f0vxbunVqGgMst8xwoewWB6J0ZP6y8sihJ3OufFh34ZiNnfFg87jxfwhwgg',
                'referer': 'https://www.google.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'x-client-data': 'CIy2yQEIpLbJAQjBtskBCKmdygEIlqzKAQisx8oBCPbHygEI6cjKAQi0y8oBCI3PygEI3NXKAQjul8sBCJGZywEImJrLARiKwcoB'
            }
            data = {
                'q': 'sexy',
                'tbm': 'isch',
                'ved': '2ahUKEwi4iazyrKHtAhVSLxoKHV-mCrUQ2-cCegQIABAA',
                'oq': 'sexy',
                'gs_lcp': 'CgNpbWcQAzoHCAAQsQMQQzoECAAQQzoFCAAQsQM6CAgAELEDEIMBOgIIAFCVlB1YgZ8dYIGxHWgAcAB4AIABywKIAdkHkgEFMi0zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ',
                'sclient': 'img',
                'ei': 'gjjAX7jANdLeaN_MqqgL',
                'bih': '597',
                'biw': '557',
                'hl': 'ar'
            }
            v = r1.get(url, headers=head).text
            # print(v[v.find('"https://'):v.find('.jpg"')+5])
            i = 1
            d = 7
            try:
                while i < d:
                    a = telebot.types.InlineKeyboardMarkup()
                    a1 = telebot.types.InlineKeyboardButton('المزيد ♐️', callback_data='a1')
                    c = v.split('.gif"')[i]
                    a.add(a1)
                    n = c.split('["https://')[-1]
                    if len(n) < 55:
                        if i == d - 1:
                            bot.send_message(msg.chat.id, f'https://{n}.gif', reply_markup=a)
                        else:
                            bot.send_message(msg.chat.id, f'https://{n}.gif')
                    else:
                        d += 1
                    i += 1
            except:
                pass
    except:
        pass



bot.polling()
