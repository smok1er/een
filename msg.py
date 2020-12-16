import time
import telebot
from telebot import types
from os import unlink
import pafy
h = []

idi = 209501902
bot = telebot.TeleBot('1309535869:AAGDVOA3Mj-P2GyBZPyYnweE03JOidfRwts')


@bot.message_handler(commands=['start'])
def key(msg):
    ch = msg.chat.id
    if f'{msg.chat.id}\n' in open('tube.txt', 'r'):
        pass
    else:
        open('tube.txt', 'a').write(f'{msg.chat.id}\n')
    bot.send_message(ch, 'اهلا و سهلا بكم في بوت  تحميل يوتيوب ☑️ ')


@bot.message_handler(content_types='text')
def an(msg):
    try:
      unlink('Q5QQQQ.mp4')
    except:
      pass
    try:
      unlink('Q5QQQQ.mp3')
    except:
      pass
    ch = msg.chat.id
    url = msg.text
    if str(ch) in str(h):
        i = 0
        try:
            while True:
                if int(h[i].split(':')[0]) == ch:
                    h.remove(f"{h[i].split(':')[0]}:{h[i].split(':')[1]}:{h[i].split(':')[2]}")
                else:
                    pass
                i += 1
        except:
            pass
        h.append(f'{ch}:{url}')
    else:
        h.append(f'{ch}:{url}')
    print(h)

    a = types.InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton('صوت فقط 🔊💚', callback_data='a1')
    a2 = types.InlineKeyboardButton('فيديو كامل 🎥💚', callback_data='a2')
    a.add(a1, a2)
    bot.send_message(ch, 'اضغط للحصول على مقطعك الذي ارسلته 👇🏻✅', reply_markup=a)




@bot.callback_query_handler(lambda call:True)
def any(call):
    ch = call.message.chat.id
    if call.data == 'a1':
        if str(ch) in str(h):
            i = 0
            try:
                while True:
                    if int(h[i].split(':')[0]) == ch:
                        url = f"{h[i].split(':')[1]}:{h[i].split(':')[2]}"
                        print(url)
                        video = pafy.new(str(url))
                        v = str(video).split(': ')[1][:str(video).find('Author') - len('Author') - 2].replace('/', '_')
                        best = video.getbestaudio()
                        best.download(filepath=f'vid/ahmed.mp3')
                        time.sleep(2)
                        bot.send_audio(ch, open(f"vid/ahmed.mp3", "rb"), caption= f'{v}\n@Q5QQQQ')
                        unlink(f'vid/ahmed.mp3')
                    else:
                        pass
                    i += 1
            except:
                pass
            
              
            
        else:
            bot.send_message(ch, 'ارسل رابط الفيديو من فضلك 💚')
    if call.data == 'a2':
        if str(ch) in str(h):
            i = 0
            try:
                while True:
                    if int(h[i].split(':')[0]) == ch:
                        url = f"{h[i].split(':')[1]}:{h[i].split(':')[2]}"
                        
                        video = pafy.new(str(url))
                        print(video)
                        v = str(video).split(': ')[1][:str(video).find('Author') - len('Author') - 2].replace('/', '_')
                        best = video.getbest()
                        strem = video.streams
                        
                        strem[0].download(filepath=f'vid/ahmed.mp4')
                        
                        bot.send_video(ch, open(f"vid/ahmed.mp4", "rb"), caption= f'{v}\n@Q5QQQQ')
                        unlink(f'vid/ahmed.mp4')
                    else:
                        pass
                    i += 1
            except:
                pass
            
              
            
        else:
            bot.send_message(ch, 'ارسل رابط الفيديو من فضلك 💚')


bot.polling()
