import telebot
import random

bot = telebot.TeleBot("6174889744:AAHA0Rrk7puKZ8PFFZnDyOwLfEop2_X-Qnw")

flag = None
sweets = 80
max_sweets = 23

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, f'Приветствую вас в игре!')
    flag = random.choice(['bot', 'user'])
    bot.send_message(message.chat.id, f'Всего в игре {sweets} конфет')
    if flag == 'user':
        bot.send_message(message.chat.id, f'Первым ходите Вы')
    else:
        bot.send_message(message.chat.id, f'Первым ходит bot')
    controller(message)

def controller(message):
    global flag
    if sweets > 0:
        if flag == 'user':
            bot.send_message(message.chat.id, f'Ваш ход, введите кол-во кофнет от 0 до {max_sweets}')
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = 'user' if flag == 'bot' else 'bot'
        bot.send_message(message.chat.id, f'победил {flag}')

def user_input(message):
    global sweets, flag
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)

def bot_input(message):
    global sweets, flag
    if sweets <= max_sweets:
        bot_turn = sweets
    elif sweets % max_sweets == 0:
        bot_turn = max_sweets - 1
    else:
        bot_turn = sweets % max_sweets - 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f'bot взял {bot_turn} конфет, всего осталось {sweets}')
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)

bot.infinity_polling()