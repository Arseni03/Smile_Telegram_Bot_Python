import telebot
from telebot import apihelper
import emoji
import random


apihelper.proxy = {'https': 'socks5h://heroku:aiSha9ib@dev.fstrk.io:1080'}
bot = telebot.TeleBot('1150149081:AAGZ0M5MdQsLsFtX1hRB_pfr5D-vr48iNAw')
Smail = {':smiling_cat_face_with_heart-eyes:': '^ↀᴥↀ^', ':flushed_face:': '(ಠ_ಠ)', ':anguished_face:': 'ಠoಠ',
         ':face_with_steam_from_nose:': '( ͡°෴ ͡°)', ':neutral_face:': '◉_◉', ':smirking_face:': '(¬‿¬)',
         ':fearful_face:': '(ʘᗩʘ)', ':downcast_face_with_sweat:': '(；一_一)',
         ':smiling_face_with_smiling_eyes:': '( ͡ᵔ ͜ʖ ͡ᵔ )', ':smiling_face_with_horns:': '(◣∀◢)ψ',
         ':slightly_smiling_face:': '◉◡◉', ':expressionless_face:': '(￣x￣;)', ':hugging_face:': '＼(￣▽￣)／',
         ':kissing_face:': '( ́ ◕◞ε◟◕`)', ':smiling_face_with_heart-eyes:': '(｡♥️‿♥️｡)',
         ':smiling_face_with_3_hearts:': '(◕‿◕)♡', ':face_blowing_a_kiss:': '( ･_･)♡', ':lying_face:': '( ͡° ͜ ͜つ ͡° )',
         ':grinning_cat_face:': '-^o^-', ':kissing_face_with_closed_eyes:': '(╯3╰)', ':relieved_face:': '(⌒_⌒)',
         ':tired_face:': '(＞﹏＜)', ':yawning_face:': '(￣O￣)ツ', ':drooling_face:': '(￣﹃￣)', ':zany_face:': '|◔◡◉|',
         ':face_savoring_food:': '(っ˘ڡ˘ς)', ':grinning_face:': '( ° ͜ʖ °',
         ':grinning_face_with_sweat:': '( ͡° ͜ʖ ͡°; )', ':face_with_tears_of_joy:': '(TᗜT)',
         ':upside-down_face:': '( ͜。 ͡ʖ ͜。)', ':face_with_monocle:': '( ͠°ヘ °)', ':nerd_face:': '(ꝊᨓꝊ)',
         ':unamused_face:': '〳 ͡° Ĺ̯ ͡° 〵', ':smiling_face_with_sunglasses:': '(■◡■)', ':star-struck:': '(⨱◡⨱)',
         ':face_with_tongue:': '(ⱺ∀ⱺ)', ':confused_face:': '(￣～￣)', ':slightly_frowning_face:': '⊙︿⊙',
         ':persevering_face:': '＼(＾∀＾)メ', ':confounded_face:': '(>_<)', ':face_without_mouth:': '(>_<)',
         ':weary_face:': '(◢ д ◣)', ':pleading_face:': '(ಥ﹏ಥ)', ':crying_face:': '(ಥ_ಥ)',
         ':loudly_crying_face:': '(╥_╥)', ':face_with_medical_mask:': '(-ロ-)', ':alien:': '⎝❍◡❍⎠',
         ':pouting_face:': '୧( ಠ Д ಠ )୨', ':grinning_squinting_face:': '(ᗒᗜᗕ)', ':winking_face_with_tongue:': '(⪰∀ⱺ)'}

@bot.message_handler(commands=['start'])
def send_welcome(message):
      bot.reply_to(message, "Добрый день, я бот, переводящий обычный смайл в текстовый (¬‿¬). Просто отправьте мне его.")
      bot.reply_to(message, "Чтобы узнать больше, используйте команду /help")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "EmojiBot - бот, созданный для перевода обычных эмодзи в текст (｡♥️‿♥️｡). Бот всё производит автоматически, достаточно лишь отправить ему смайл. На данный момент бот имеет ограниченный функционал, в его базе 50 наиболее часто используемых смайлов ( ͜。 ͡ʖ ͜。)")
    bot.reply_to(message, "Также у бота имеется команда /random, выводящая случайный смайл")

@bot.message_handler(commands=['random'])
def send_welcome(message):
    s = random.randint(0,49)
    bot.reply_to(message, Smails_Text[s])

@bot.message_handler(commands=['find'])
def send_welcome(message):
    mes = str(message.text)[5:].replace(' ', '')
    print(mes)
    count = 0
    for i in Smail.keys():
        if i.find(mes):
            bot.reply_to(message, Smail[i])
            count+=1
    if count == 0:
        bot.reply_to(message, 'Нет такого тега')





@bot.message_handler(content_types=["text"])
def a(message):
    if extract_emojis(message.text):
        if Smail.get(emoji.demojize(message.text)) is not None:
            bot.reply_to(message, Smail[emoji.demojize(message.text)])
        else:
          bot.reply_to(message, 'Простите, но такого смайла пока нет в базе данных. Дождитесь, пока разработчики его добавят (￣﹃￣)')
    else:
        bot.reply_to(message, "Это не смайл. Простите, но так бот вас не понимает (ⱺ  ⱺ)")

def extract_emojis(s):
    return s in emoji.UNICODE_EMOJI



bot.polling(none_stop=True, interval=0)