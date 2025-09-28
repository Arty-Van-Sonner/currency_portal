import os
import telebot
from dotenv import load_dotenv, find_dotenv
from .models import CurrencyNameOption

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('TELEGRAMBOT_TOKEN'))

def start_telegrambot(*args, **kwargs):
    bot.polling()

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message) -> None:
    answer = get_instruction_str()
    bot.reply_to(message, answer, parse_mode='Markdown')

@bot.message_handler(commands = ['help'])
def help(message: telebot.types.Message): 
    text_for_processing = message.text.replace('/help', '').strip()
    currency = CurrencyNameOption.get_currency_by_name(text_for_processing)
    answer = ''
    if currency is None:
        answer = get_instruction_str()
    else:
        answer = currency.information
    bot.reply_to(message, answer, parse_mode = "Markdown")

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    answer = '*Available currencies:*' + сurrencies.list_currencies_for_output
    bot.reply_to(message, answer, parse_mode="Markdown")

@bot.message_handler(content_types = ['text'])
def text(message: telebot.types.Message):
    answer = ''
    was_exeptions = False
    try:
        currency_converter = classes.MyCurrencyConverter(message.text)
        answer = currency_converter.get_string_converted_amount()
    except gv.ErrorInStringFromUser as eisf:
        answer = f'{eisf} ({gv.ErrorInStringFromUser})'
        was_exeptions = True
        print()
        print('message_handler', eisf, gv.ErrorInStringFromUser, sep = '\n')
        print()
    except ValueError as ve:
        answer = f'{ve} ({ValueError})'
        was_exeptions = True
        print()
        print('message_handler', ex, ValueError, sep = '\n')
        print()
    except Exception as ex:
        answer = f'{ex} ({Exception})'
        was_exeptions = True
        print()
        print('message_handler', ex, Exception, sep = '\n')
        print()
    if was_exeptions:
        bot.reply_to(bot.reply_to(message, answer, parse_mode="Markdown"), get_instruction_str(), parse_mode="Markdown")
    else:
        bot.reply_to(message, answer, parse_mode="Markdown")

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.reply_to(message, 'Hello World!!!') 


def get_instruction_str() -> str:
        return '''*For using bot: enter a command to the bot in the following format:*
    •	_<currency name of source> <currency name of receiver> <the amount of currency being transferred>_
        `(Here the name of the currency should be in one word, but you can use '_' as space)`
    •	_<currency name of source> -> <currency name of receiver> (<the amount of currency being transferred>)_
    •	_(<the amount of currency being transferred>) <currency name of source> -> <currency name of receiver>_
        Show a list of available currencies: /values
        Show instructions: /help
        Show data of currency: /help <currency name>'''