import telebot
from telebot import apihelper
import emoji
import random


apihelper.proxy = {'https': 'socks5h://heroku:aiSha9ib@dev.fstrk.io:1080'}
bot = telebot.TeleBot('1150149081:AAGZ0M5MdQsLsFtX1hRB_pfr5D-vr48iNAw')

Smails = [':smiling_cat_face_with_heart-eyes:',':flushed_face:',':anguished_face:',':face_with_steam_from_nose:', #0-3
':neutral_face:',':smirking_face:',':fearful_face:',':downcast_face_with_sweat:', #4-7
':smiling_face_with_smiling_eyes:',':smiling_face_with_horns:',':slightly_smiling_face:',':expressionless_face:',':hugging_face:', #8-12
':kissing_face:',':smiling_face_with_heart-eyes:',':smiling_face_with_3_hearts:',':face_blowing_a_kiss:',':lying_face:', #13-17
':grinning_cat_face:',':kissing_face_with_closed_eyes:',':relieved_face:',':tired_face:',':yawning_face:', #18-22
':drooling_face:',':zany_face:',':face_savoring_food:',':grinning_face:',':grinning_face_with_sweat:',':face_with_tears_of_joy:', #23-28
':upside-down_face:',':face_with_monocle:',':nerd_face:',':unamused_face:',':smiling_face_with_sunglasses:',':star-struck:',':face_with_tongue:',':confused_face:', #29-36
':slightly_frowning_face:',':persevering_face:',':confounded_face:',':face_without_mouth:',':weary_face:',':pleading_face:',':crying_face:', #37-43
':loudly_crying_face:',':face_with_medical_mask:',':alien:',':pouting_face:',':grinning_squinting_face:',':winking_face_with_tongue:'] #44-49

Smails_Text = ['^ↀᴥↀ^', '(ಠ_ಠ)', 'ಠoಠ', '( ͡°෴ ͡°)', #0-3
'◉_◉', '(¬‿¬)', '(ʘᗩʘ)', '(；一_一)', #4-7
'( ͡ᵔ ͜ʖ ͡ᵔ )', '(◣∀◢)ψ', '◉◡◉', '(￣x￣;)', '＼(￣▽￣)／', #8-12
'( ́ ◕◞ε◟◕`)', '(｡♥️‿♥️｡)', '(◕‿◕)♡', '( ･_･)♡', '( ͡° ͜ ͜つ ͡° )', #13-17
'-^o^-', '(╯3╰)', '(⌒_⌒)', '(＞﹏＜)', '(￣O￣)ツ', #18-22
'(￣﹃￣)', '|◔◡◉|', '(っ˘ڡ˘ς)', '( ° ͜ʖ °', '( ͡° ͜ʖ ͡°; )', '(TᗜT)', #23-28
'( ͜。 ͡ʖ ͜。)', '( ͠°ヘ °)', '(ꝊᨓꝊ)', '〳 ͡° Ĺ̯ ͡° 〵', '(■◡■)', '(⨱◡⨱)', '(ⱺ∀ⱺ)', '(￣～￣)', #29-36
'⊙︿⊙', '＼(＾∀＾)メ', '(>_<)', '(>_<)', '(◢ д ◣)', '(ಥ﹏ಥ)', '(ಥ_ಥ)', #37-43
'(╥_╥)', '(-ロ-)', '⎝❍◡❍⎠', '୧( ಠ Д ಠ )୨', '(ᗒᗜᗕ)', '(⪰∀ⱺ)'] #44-49

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



@bot.message_handler(content_types=["text"])
def a(message):
    if extract_emojis(message.text):
        if emoji.demojize(message.text) == Smails[0]:
          bot.reply_to(message, Smails_Text[0])
        if emoji.demojize(message.text) == Smails[1]:
          bot.reply_to(message, Smails_Text[1])
        if emoji.demojize(message.text) == Smails[2]:
          bot.reply_to(message, Smails_Text[2])
        if emoji.demojize(message.text) == Smails[3]:
          bot.reply_to(message, Smails_Text[3])
        if emoji.demojize(message.text) == Smails[4]:
          bot.reply_to(message, Smails_Text[4])
        if emoji.demojize(message.text) == Smails[5]:
          bot.reply_to(message, Smails_Text[5])
        if emoji.demojize(message.text) == Smails[6]:
          bot.reply_to(message, Smails_Text[6])
        if emoji.demojize(message.text) == Smails[7]:
          bot.reply_to(message, Smails_Text[7])
        if emoji.demojize(message.text) == Smails[8]:
          bot.reply_to(message, Smails_Text[8])
        if emoji.demojize(message.text) == Smails[9]:
          bot.reply_to(message, Smails_Text[9])
        if emoji.demojize(message.text) == Smails[10]:
          bot.reply_to(message, Smails_Text[10])
        if emoji.demojize(message.text) == Smails[11]:
          bot.reply_to(message, Smails_Text[11])
        if emoji.demojize(message.text) == Smails[12]:
          bot.reply_to(message, Smails_Text[12])
        if emoji.demojize(message.text) == Smails[13]:
          bot.reply_to(message, Smails_Text[13])
        if emoji.demojize(message.text) == Smails[14]:
          bot.reply_to(message, Smails_Text[14])
        if emoji.demojize(message.text) == Smails[15]:
          bot.reply_to(message, Smails_Text[15])
        if emoji.demojize(message.text) == Smails[16]:
          bot.reply_to(message, Smails_Text[16])
        if emoji.demojize(message.text) == Smails[17]:
          bot.reply_to(message, Smails_Text[17])
        if emoji.demojize(message.text) == Smails[18]:
          bot.reply_to(message, Smails_Text[18])
        if emoji.demojize(message.text) == Smails[19]:
          bot.reply_to(message, Smails_Text[19])
        if emoji.demojize(message.text) == Smails[20]:
          bot.reply_to(message, Smails_Text[20])
        if emoji.demojize(message.text) == Smails[21]:
          bot.reply_to(message, Smails_Text[21])
        if emoji.demojize(message.text) == Smails[22]:
          bot.reply_to(message, Smails_Text[22])
        if emoji.demojize(message.text) == Smails[23]:
          bot.reply_to(message, Smails_Text[23])
        if emoji.demojize(message.text) == Smails[24]:
          bot.reply_to(message, Smails_Text[24])
        if emoji.demojize(message.text) == Smails[25]:
          bot.reply_to(message, Smails_Text[25])
        if emoji.demojize(message.text) == Smails[26]:
          bot.reply_to(message, Smails_Text[26])
        if emoji.demojize(message.text) == Smails[27]:
          bot.reply_to(message, Smails_Text[27])
        if emoji.demojize(message.text) == Smails[28]:
          bot.reply_to(message, Smails_Text[28])
        if emoji.demojize(message.text) == Smails[29]:
          bot.reply_to(message, Smails_Text[29])
        if emoji.demojize(message.text) == Smails[30]:
          bot.reply_to(message, Smails_Text[30])
        if emoji.demojize(message.text) == Smails[31]:
          bot.reply_to(message, Smails_Text[31])
        if emoji.demojize(message.text) == Smails[32]:
          bot.reply_to(message, Smails_Text[32])
        if emoji.demojize(message.text) == Smails[33]:
          bot.reply_to(message, Smails_Text[33])
        if emoji.demojize(message.text) == Smails[34]:
          bot.reply_to(message, Smails_Text[34])
        if emoji.demojize(message.text) == Smails[35]:
          bot.reply_to(message, Smails_Text[35])
        if emoji.demojize(message.text) == Smails[36]:
          bot.reply_to(message, Smails_Text[36])
        if emoji.demojize(message.text) == Smails[37]:
          bot.reply_to(message, Smails_Text[37])
        if emoji.demojize(message.text) == Smails[38]:
          bot.reply_to(message, Smails_Text[38])
        if emoji.demojize(message.text) == Smails[39]:
          bot.reply_to(message, Smails_Text[39])
        if emoji.demojize(message.text) == Smails[40]:
          bot.reply_to(message, Smails_Text[40])
        if emoji.demojize(message.text) == Smails[41]:
          bot.reply_to(message, Smails_Text[41])
        if emoji.demojize(message.text) == Smails[42]:
          bot.reply_to(message, Smails_Text[42])
        if emoji.demojize(message.text) == Smails[43]:
          bot.reply_to(message, Smails_Text[43])
        if emoji.demojize(message.text) == Smails[44]:
          bot.reply_to(message, Smails_Text[44])
        if emoji.demojize(message.text) == Smails[45]:
          bot.reply_to(message, Smails_Text[45])
        if emoji.demojize(message.text) == Smails[46]:
          bot.reply_to(message, Smails_Text[46])
        if emoji.demojize(message.text) == Smails[47]:
          bot.reply_to(message, Smails_Text[47])
        if emoji.demojize(message.text) == Smails[48]:
          bot.reply_to(message, Smails_Text[48])
        if emoji.demojize(message.text) == Smails[49]:
          bot.reply_to(message, Smails_Text[48])
        else:
          bot.reply_to(message, 'Простите, но такого смайла пока нет в базе данных. Дождитесь, пока разработчики его добавят (￣﹃￣)')
    else:
        bot.reply_to(message, "Это не смайл. Простите, но так бот вас не понимает (ⱺ  ⱺ)")

def extract_emojis(s):
    return s in emoji.UNICODE_EMOJI



bot.polling(none_stop=True, interval=0)