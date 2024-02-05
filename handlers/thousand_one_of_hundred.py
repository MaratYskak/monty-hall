import random
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from init import dp, bot



async def thousand_one_of_hundred(message: types.Message):
    msg = "сейчас выведу результат запусков игры одну тысячу раз, "
    msg += "где бот каждый раз менял свой выбор, когда ведущий ему это предлагал. "
    msg += "Это может занять какое-то время, подождите"
    await bot.send_message(message.from_user.id, msg)

    count_wins = 0

    for _ in range(1000):
        selected_number = random.randint(1, 100)
        selected_number2 = random.randint(1, 100)

        if selected_number != selected_number2:
            count_wins += 1

    msg2 = f"итого, применяя такую тактику, бот выиграл {count_wins} раз из 1000"
    await bot.send_message(message.from_user.id, msg2)
