from handlers.explain import explain
from handlers.one_of_hundred import one_of_hundred
from handlers.one_of_three import one_of_three
from handlers.start import send_welcome
from handlers.thousand_one_of_hundred import thousand_one_of_hundred
from handlers.thousand_one_of_three import thousand_one_of_three
from init import dp, bot 
from aiogram.filters.command import Command
from aiogram import F




def register_handlers():
    dp.message.register(send_welcome, Command('start'))

    dp.message.register(one_of_three, F.text == "поиграть 'один из трёх'")
    dp.message.register(one_of_hundred, F.text == "поиграть 'один из ста'")
    dp.message.register(explain, F.text == "объяснение 'парадокса'")
    dp.message.register(thousand_one_of_three, F.text == "запустить 1000 игр 'один из трёх'")
    dp.message.register(thousand_one_of_hundred, F.text == "запустить 1000 игр 'один из ста'")