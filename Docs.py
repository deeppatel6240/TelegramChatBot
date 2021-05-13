import random
import time
from _warnings import filters
import telebot

bot_token = "1885957296:AAF1CNpOeSSBwD3q3XlwdQ7ovkI6qN03CwI"
bot = telebot.TeleBot(bot_token)

# All Commands
user_name = 'deeppatel6240'


@bot.message_handler(func=lambda message: message.text is not None and message.from_user.username != user_name)
def check_username(message):
    bot.send_message(message.chat.id, "You can't use this bot")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey Deep, What's up?")
    # bot.send_message(message.chat.id, message.from_user.username)
    # bot.send_message(message.chat.id, "It it You?")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Hey Deep, I have many features created by my lord\n"
                                      "These bot of mine contain total 3 types of section\n"
                                      "1. Documents of Deep --> /docs_help \n"
                                      "2. Important educations links of Deep --> /imp_links \n"
                                      "3. Wallpaper links --> /wallpapers \n")


@bot.message_handler(commands=['docs_help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Hey Deep, this function of bot is designed for you to easily find your documents 😉 \n"
                     "I have all your important documents 😎\n"
                     "Which one would you like to see 📂?\n"
                     "10th result, 12th result, BE All Semesters, Adharcard etc.")


@bot.message_handler(commands=['imp_links'])
def important_Links(message):
    bot.send_message(message.chat.id,
                     "Hey Deep, this function of bot is designed for you to easily find important links 😉 \n"
                     "Example: Github, LinkedIn, Amazon, Lanquage Docs etc 😎\n"
                     "Which one would you like to see 📂?\n")


@bot.message_handler(commands=['wallpapers'])
def important_Links(message):
    bot.send_message(message.chat.id,
                     "Hey Deep, this function of bot is designed for you to easily find HP and 4K wallpapers 😉 \n"
                     "Example: Unplash, pinterest, wallpaperflare etc 😎\n"
                     "Which one would you like to see 📂?")


# All Content types and handlers
@bot.message_handler(content_types=['audio', 'video', 'document', 'photo'])
def aud(message):
    bot.reply_to(message, 'oops, Something went Wrong. Seems like you sent message in differnet format.\n'
                          'Type /help command to show the available format')


# functions

@bot.message_handler(
    func=lambda message: message.text is not None and 'good' in message.text.lower()
                         or message.text is not None and 'fine' in message.text.lower())
def How_are_you(message):
    bot.reply_to(message,
                 'Okay ' + message.from_user.first_name + '. How can i help you?🙂')
    bot.send_message(message.chat.id, 'If you do not know my features then write /help in message box')


# docs of deep
@bot.message_handler(func=lambda message: message.text is not None and '10' in message.text.lower())
def picture(message):
    bot.send_message(message.chat.id, 'My Lord, Here is mark sheet of your 10th grade')
    bot.send_photo(message.chat.id, 'https://i.ibb.co/bJ4jKxm/Deep-10th-Marksheet.jpg', caption="10th Result!")


@bot.message_handler(func=lambda message: message.text is not None and '12' in message.text.lower())
def picture(message):
    bot.send_message(message.chat.id, 'My Lord, Here is mark sheet of your 12th grade')
    bot.send_photo(message.chat.id, 'https://i.ibb.co/2M2fCCY/Deep-12th-Marksheet.jpg', caption="12th Result!")


@bot.message_handler(func=lambda message: message.text is not None and 'adhar' in message.text.lower())
def picture(message):
    bot.send_message(message.chat.id, 'My Lord, Here is your AdharCard')
    bot.send_photo(message.chat.id, 'https://i.ibb.co/JcCFcYB/pdfresizer-com-pdf-crop-1.jpg', caption="Adharcard")


    '''
        For full size image 
            1. sent the original size picture to your bot
            2. use get method for finding file_id of the image (https://api.telegram.org/1885957296:AAF1CNpOeSSBwD3q3XlwdQ7ovkI6qN03CwI/getUpdates)
            3. then use this command to find file_path
                (bot_token = 1885957296:AAF1CNpOeSSBwD3q3XlwdQ7ovkI6qN03CwI)
                (file_id = BQACAgUAAxkBAAIDgmCbjlKRA9pWKJi3vJlS5RqBwgsJAAJKAgACm8zYVAE8YlSeYU0oHwQ)
                (https://api.telegram.org/token_of_your_bot/getfile?file_id=BQACAgUAAxkBAAIDgmCbjlKRA9pWKJi3vJlS5RqBwgsJAAJKAgACm8zYVAE8YlSeYU0oHwQ)
            4. By using above url you can find file_path which is below
                (https://api.telegram.org/file/1885957296:AAF1CNpOeSSBwD3q3XlwdQ7ovkI6qN03CwI/documents/file_0.jpg)
            5. now you can download image in original size.
    '''


# wallpapers links
@bot.message_handler(func=lambda message: message.text is not None and 'CAR' in message.text.upper())
def car(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    # unsplash
    bot.reply_to(message,
                 "UNSPLASH\n"
                 "For more Information visit:<a href='https://unsplash.com/s/photos/car'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # pixels
    bot.reply_to(message,
                 "PIXELS\n"
                 "For more Information visit:<a href='https://www.pexels.com/search/car'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # wallpapercraft
    bot.reply_to(message,
                 "WALLPAPER CRAFT\n"
                 "For more Information visit:<a href='https://wallpaperscraft.com/catalog/cars/3840x2400'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # wallpaper access
    bot.reply_to(message,
                 "WALLPAPER ACCESS\n"
                 "For more Information visit:<a href='https://wallpaperaccess.com/search?q=car'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)


# nature
@bot.message_handler(func=lambda message: message.text is not None and 'NATURE' in message.text.upper())
def nature(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    # unsplash
    bot.reply_to(message,
                 "UNSPLASH\n"
                 "For more Information visit:<a href='https://unsplash.com/s/photos/4k-landscape'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # wallpaper cave
    bot.reply_to(message,
                 "Wallpaper Cave\n"
                 "For more Information visit:<a href='https://wallpapercave.com/nature-4k-wallpapers'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # wallpaper craft
    bot.reply_to(message,
                 "WALLPAPER ACCESS\n"
                 "For more Information visit:<a href='https://wallpaperscraft.com/catalog/nature/3840x2400'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # hdq walls
    bot.reply_to(message,
                 "HDq walls\n"
                 "For more Information visit:<a href='https://hdqwalls.com/category/nature-wallpapers'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)

    # wallpaper flare
    bot.reply_to(message,
                 "Wallpaper Flare\n"
                 "For more Information visit:<a href='https://www.wallpaperflare.com/search?wallpaper=beauty+In+Nature'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)


# Unrecognized message
@bot.message_handler(content_types=['text'])
def Checking_for_right_msg(message):
    bot.send_message(message.chat.id, "Sorry! I wasn't able to recognize what you sent.Please try again")


bot.polling(none_stop=True)

