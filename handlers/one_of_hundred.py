import random
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from init import dp, bot

class Main(StatesGroup):
    start = State()




async def one_of_hundred(message: types.Message, state: FSMContext):
    selected_number = random.randint(1, 100)

    selected_number = str(selected_number)

    await state.update_data(the_num=selected_number)

    msg = "чтобы вы убедились, что я не жульничаю, "
    msg += "я сразу тут напишу, какой номер выигрышный: \n\n"
    msg += f" || {selected_number} || \n\n"
    msg += "не нужно смотреть его сейчас\\. Можете посмотреть после игры"


    await bot.send_message(message.from_user.id, msg, parse_mode='MarkdownV2')

    msg2 = "теперь напишите ваш вариант (число от 1 до 100)"
    await bot.send_message(message.from_user.id, msg2)
    await state.set_state(Main.start)


@dp.message(StateFilter(Main.start))
async def start(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, f"вы выбрали {message.text}, и с вероятностью 99% вы ошиблись 😁")
    await bot.send_message(message.from_user.id, f"теперь уберём из оставшихся вариантов 98 неправильных")

    data = await state.get_data()
    the_num = data['the_num']
    won = ''
    if the_num == message.text:
        won = 'won'
    else:
        won = 'nope'

    # Заданные числа, которые нужно исключить из выбора
    excluded_numbers = [int(message.text)]

    # Генерация списка чисел от 1 до 100 без исключенных чисел
    available_numbers = [number for number in range(1, 101) if number not in excluded_numbers]

    # Случайный выбор одного числа из доступных чисел
    selected_number_except_excluded = random.choice(available_numbers)

    selected_number_except_excluded
    await bot.send_message(message.from_user.id, f"я оставил еще один вариант неизвестным - {selected_number_except_excluded}")

    builder = InlineKeyboardBuilder()
    if won == 'won':
        builder.add(InlineKeyboardButton(
            text="оставить свой выбор прежним",
            callback_data=f"hundFinish same won {message.text}")
        )
        builder.add(InlineKeyboardButton(
            text="поменять выбор",
            callback_data=f"hundFinish changed lost {selected_number_except_excluded}")
        )
    else:
        builder.add(InlineKeyboardButton(
            text="оставить свой выбор прежним",
            callback_data=f"hundFinish same lost {message.text}")
        )
        builder.add(InlineKeyboardButton(
            text="поменять выбор",
            callback_data=f"hundFinish changed won {selected_number_except_excluded}")
        )

    builder.adjust(1)
    await bot.send_message(message.from_user.id, f"хотите выбрать его или хотите оставить свой выбор прежним?", reply_markup=builder.as_markup())
    await state.clear()


@dp.callback_query(F.data.startswith("hundFinish"))
async def hundFinish(callback: CallbackQuery):
    _, changed_or_same, itog, choice = callback.data.split(" ")

    if changed_or_same == 'same':
        msg = f"вы оставили выбор прежним - {choice}. "
        msg += f"Ваш шанс угадать при этом остался прежним - 1/100"
        await bot.send_message(callback.from_user.id, msg)

    if changed_or_same == 'changed':
        msg = f"вы поменяли выбор на {choice}. "
        msg += f"Ваш шанс угадать при этом возрос - 99%"
        await bot.send_message(callback.from_user.id, msg)

    if itog == 'lost':
        msg = 'в итоге вы проиграли, бывает'
        await bot.send_message(callback.from_user.id, msg)
    if itog == 'won':
        msg = 'в итоге вы выиграли'
        await bot.send_message(callback.from_user.id, msg)
