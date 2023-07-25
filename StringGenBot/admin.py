import telebot
bot = telebot.TeleBot('')
botuser = "Bot_string_51_bot"
dev = 5108562302
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    u = []
    with open(f"data/{botuser}.txt", "r") as file:
        u = file.read().splitlines()

    if user_id not in u:
        with open(f"data/{botuser}.txt", "a") as file:
            file.write(str(user_id) + "\n")

@bot.message_handler(commands=['commands'])
def commands(message):
    user_id = message.from_user.id
    if user_id == dev:
        bot.send_message(chat_id=message.chat.id,
                         text="• مرحبا بك في قائمة المطور ",
                         reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add("الاعضاء 🙍🏻‍♂️", "اذاعة ✔️"))

@bot.message_handler(func=lambda message: message.text == 'الاعضاء 🙍🏻‍♂️' and message.from_user.id == dev)
def members(message):
    c = 0
    with open(f"data/{botuser}.txt", "r") as file:
        c = len(file.readlines())

    bot.send_message(chat_id=message.chat.id,
                     text="• اعضاء البوت  :- " + str(c))

@bot.message_handler(func=lambda message: message.text == 'اذاعة ✔️' and message.from_user.id == dev)
def broadcast(message):
    with open(f"data/2{botuser}.txt", "w") as file:
        file.write("yas")

    bot.send_message(chat_id=message.chat.id,
                     text="• ارسل رسالتك الان وسيتم نشرها لـ " + str(c) + " مشترك",
                     reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add("- الغاء النشر ."))

@bot.message_handler(func=lambda message: message.text != '- الغاء النشر .' and message.from_user.id == dev and message.text and mode == "yas")
def broadcast_message(message):
    u = []
    with open(f"data/{botuser}.txt", "r") as file:
        u = file.read().splitlines()

    for user in u:
        dev = bot.send_message(chat_id=user, text=message.text)
        sendd = dev_i.message_id
        bot.pin_chat_message(chat_id=user, message_id=sendd)

    bot.send_message(chat_id=message.chat.id,
                     text="• تم الارسال بنجاح ...",
                     reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add("الاعضاء 🙍🏻‍♂️", "اذاعة "))

    with open(f"data/2{botuser}.txt", "w") as file:
        file.write("no")

@bot.message_handler(func=lambda message: message.text == 'الغاء 🍷' and message.from_user.id == dev)
def cancel_broadcast(message):
    with open(f"data/2{botuser}.txt", "w") as file:
        file.write("no")

    bot.send_message(chat_id=message.chat.id,
                     text="• تـم الغاء الاذاعة ✔️",
                     reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add("الاعضاء 🙍🏻‍♂️", "اذاعة ✔️"))

bot.polling()
