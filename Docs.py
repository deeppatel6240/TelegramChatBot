import random
from _warnings import filters

import telebot

bot_token = "1854520305:AAHAa_u5MedduwWiZRtUPWI06ZrpBTRuZBs"
bot = telebot.TeleBot(bot_token)

# All Commands
user_name = 'deeppatel6240'


@bot.message_handler(func=lambda message: message.text is not None and message.from_user.username != user_name)
def check_username(message):
        bot.send_message(message.chat.id, "You can't use this bot")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey Deep, What's up?")
    bot.send_message(message.chat.id, message.from_user.username)
    bot.send_message(message.chat.id, "It it You?")



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Hey Deep, I have many features created by my lord\n"
                                      "These bot of mine contain total 3 types of section\n"
                                      "1. Documents of Deep --> /docs_help \n"
                                      "2. Important educations links of Deep --> /imp_links \n"
                                      "3. Wallpaper links --> /wallpapers \n")


@bot.message_handler(commands=['docs_help'])
def help(message):
    bot.send_message(message.chat.id, "Hey Deep, this function of bot is designed for you to easily find your documents 😉 \n"
                                      "I have all your important documents 😎\n"
                                      "Which one would you like to see 📂?")


@bot.message_handler(commands=['imp_links'])
def important_Links(message):
    bot.send_message(message.chat.id, "Hey Deep, this function of bot is designed for you to easily find important links 😉 \n"
                                      "Example: Github, LinkedIn, Amazon, Lanquage Docs etc 😎\n"
                                      "Which one would you like to see 📂?")


@bot.message_handler(commands=['wallpapers'])
def important_Links(message):
    bot.send_message(message.chat.id, "Hey Deep, this function of bot is designed for you to easily find HP and 4K wallpapers 😉 \n"
                                      "Example: Unplash, pinterest, wallpaperflare etc 😎\n"
                                      "Which one would you like to see 📂?")


@bot.message_handler(commands=['github'])
def Git_hub(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Click Here', url='https://github.com/deeppatel6240'))
    bot.send_message(message.chat.id, 'It is Github Profile of Deep', reply_markup=keyboard)


# All Content types and handlers
@bot.message_handler(content_types=['audio', 'video', 'document', 'photo'])
def aud(message):
    bot.reply_to(message, 'oops, Something went Wrong. Seems like you sent message in differnet format.\n'
                          'Type /help command to show the available format')


#functions
@bot.message_handler(func=lambda message: message.from_user.username)
def Is_it_you(message):
    # user_name = 'deeppatel6240'
    if message.text.lower() == user_name:
        bot.reply_to(message, "Well then let's begin 😎")
    else:
        bot.send_message(message.chat.id, "Sorry! I wasn't able to recognize what you sent.Please try again")


''' # Content_types

# Audio
@bot.message_handler(content_types=['audio'])
def aud(message):
    bot.reply_to(message, 'its an audio')
    bot.send_message(message.chat.id, "Please Send Again")


# link
@bot.message_handler(commands=['github'])
def Git_hub(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Click Here', url='https://github.com/deeppatel6240'))
    bot.send_message(message.chat.id, 'It is Github Profile of Deep', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text is not None and 'DARK' in message.text.upper())
def dia(message):
    bot.reply_to(message,
                 "Dark is a German science fiction thriller streaming television series co-created by Baran bo Odar and Jantje Friese."
                 "[5][6][7] It ran for three seasons from 2017 to 2020. In the aftermath of a child's disappearance, Dark follows "
                 "characters from the fictional German town of Winden as they pursue the truth. They follow connections between four "
                 "estranged families to unravel a sinister time travel conspiracy which spans several generations. "
                 "The series explores the existential implications of time, and its effect on human nature."
                 "\nFor more information visit:<a href='https://en.wikipedia.org/wiki/Dark_(TV_series)'>Wiki</a>",
                 parse_mode='HTML')


# text
@bot.message_handler(content_types=['text'])
def un_rec(message):
    bot.send_message(message.chat.id, "Sorry! I wasn't able to recognize what you sent.Please try again")


# photo
@bot.message_handler(content_types=['photo'])
def picture(message):
    bot.reply_to(message, 'it is photo')
    pic = ['0.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg']
    # reply_pic = open('Resources/Photo/' + random.choice(pic), 'r')
    bot.send_photo(message.chat.id, photo=open('Resources/Photo/' + random.choice(pic), 'rb'))


#document and message method
@bot.message_handler(content_types= ['document'])
def document(message):
    bot.reply_to(message, "it is pdf file")

    bot.send_message(message.chat.id, text="This is your message id :")
    bot.reply_to(message, text=message.message_id, parse_mode='MarkDown')
    # bot.send_message(message.chat.id, msg_date, parse_mode='MarkDown')  '''



bot.polling(none_stop=True)
