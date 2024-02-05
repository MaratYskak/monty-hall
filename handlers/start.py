from aiogram import types

from init import dp, bot



async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text="объяснение 'парадокса'")],
        [types.KeyboardButton(text="поиграть 'один из трёх'")],
        [types.KeyboardButton(text="поиграть 'один из ста'")],
        [types.KeyboardButton(text="запустить 1000 игр 'один из трёх'")],
        [types.KeyboardButton(text="запустить 1000 игр 'один из ста'")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)

    msg = "эти две игры 'один из трёх' и 'один из 100' "
    msg += "наглядно показывают принцип 'парадокса' Монти Холла, "
    msg += "(который парадоксом не является, но почему-то его так называют)"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard)