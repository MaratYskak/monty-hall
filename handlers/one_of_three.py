import random
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from init import dp, bot



async def one_of_three(message: types.Message, state: FSMContext):
    # Список чисел для выбора
    numbers = [1, 2, 3]

    # Случайный выбор одного числа из списка
    selected_number = random.choice(numbers)

    selected_number = str(selected_number)

    mapa = {
        '1': 'wrong',
        '2': 'wrong',
        '3': 'wrong',
    }

    mapa[selected_number] = 'right'

    await state.update_data(mapa=mapa)

    msg = "чтобы вы убедились, что я не жульничаю, "
    msg += "я сразу тут напишу, какой номер выигрышный: \n\n"
    msg += f" || {selected_number} || \n\n"
    msg += "не нужно смотреть его сейчас\\. Можете посмотреть после игры"


    await bot.send_message(message.from_user.id, msg, parse_mode='MarkdownV2')

    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="1",
        callback_data=f"choice 1")
    )
    builder.add(InlineKeyboardButton(
        text="2",
        callback_data=f"choice 2")
    )
    builder.add(InlineKeyboardButton(
        text="3",
        callback_data=f"choice 3")
    )
    builder.adjust(3)

    msg2 = "а сейчас выберите один вариант"
    await bot.send_message(message.from_user.id, msg2, reply_markup=builder.as_markup())


@dp.callback_query(F.data.startswith("choice"))
async def choice(callback: CallbackQuery, state: FSMContext):
    _, choice = callback.data.split(" ")

    data = await state.get_data()

    mapa = data['mapa']
    

    lose_num = ''
    change_num = ''

    for k, v in mapa.items():
        if v != 'right' and k != choice:
            lose_num = k
    for k, v in mapa.items():
        if k != lose_num and k != choice:
            change_num = k

    if mapa[choice] == 'right':
        mapa['won'] = 'won'
    else:
        mapa['won'] = 'nope'

    await bot.send_message(callback.from_user.id, f"вы выбрали {choice}")
    await bot.send_message(callback.from_user.id, f"из оставшихся двух я открою вам один проигрышный номер - это {lose_num}")

    builder = InlineKeyboardBuilder()
    if mapa['won'] == 'won':
        builder.add(InlineKeyboardButton(
            text="оставить выбор прежним",
            callback_data=f"finish same won {choice}")
        )
        builder.add(InlineKeyboardButton(
            text="поменять",
            callback_data=f"finish changed lost {change_num}")
        )
    else:
        builder.add(InlineKeyboardButton(
            text="оставить выбор прежним",
            callback_data=f"finish same lost {choice}")
        )
        builder.add(InlineKeyboardButton(
            text="поменять",
            callback_data=f"finish changed won {change_num}")
        )
    await bot.send_message(callback.from_user.id, f"теперь хотите ли оставить выбор прежним или хотите поменять?", reply_markup=builder.as_markup())


@dp.callback_query(F.data.startswith("finish"))
async def finish(callback: CallbackQuery):
    _, changed_or_same, itog, choice = callback.data.split(" ")

    if changed_or_same == 'same':
        msg = f"вы оставили выбор прежним - {choice}. "
        msg += f"Ваш шанс угадать при этом остался прежним - 1/3"
        await bot.send_message(callback.from_user.id, msg)

    if changed_or_same == 'changed':
        msg = f"вы поменяли выбор на {choice}. "
        msg += f"Ваш шанс угадать при этом возрос - 2/3"
        await bot.send_message(callback.from_user.id, msg)

    if itog == 'lost':
        msg = 'в итоге вы проиграли, бывает'
        await bot.send_message(callback.from_user.id, msg)
    if itog == 'won':
        msg = 'в итоге вы выиграли'
        await bot.send_message(callback.from_user.id, msg)