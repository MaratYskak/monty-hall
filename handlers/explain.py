from aiogram import types

from init import dp, bot



async def explain(message: types.Message):
    msg = """
    “Парадокс Монти Холла” - это вероятностная головоломка, основанная на американской телевизионной игре “Let’s Make a Deal”. Ведущий игры, Монти Холл, предлагает участнику выбрать одну из трех дверей. За одной из дверей находится автомобиль, а за двумя другими - козы.

Вот как это работает:

Вы выбираете одну из трех дверей (например, дверь №1). Монти, который знает, что находится за каждой дверью, открывает одну из оставшихся дверей, за которой находится коза (например, дверь №3). Теперь у вас есть выбор: остаться с вашим первоначальным выбором (дверь №1) или переключиться на другую закрытую дверь (дверь №2).

Интуитивно кажется, что вероятность выигрыша равна 50/50, независимо от того, смените вы свой выбор или нет. Однако математический анализ показывает, что ваш шанс выиграть удваивается, если вы меняете свой выбор.

Вот почему:

Вероятность того, что автомобиль находится за дверью, которую вы изначально выбрали, составляет 1/3. Следовательно, вероятность того, что автомобиль находится где-то за оставшимися двумя дверями, составляет 2/3. Когда Монти открывает одну из оставшихся дверей, показывая козу, это не меняет вероятность того, что автомобиль находится за вашей изначально выбранной дверью (1/3). Однако теперь мы знаем, что автомобиль точно находится за одной из двух дверей: вашей изначально выбранной дверью или закрытой дверью. Таким образом, вероятность того, что автомобиль находится за закрытой дверью, составляет 2/3. Поэтому, если вы смените свой выбор, ваш шанс выиграть увеличится до 2/3.

Еще более понятное объяснение:
Изначально 100 коробок, из которых 99 пустые и 1 с призом. Вы выбираете одну коробку, и с вероятностью 99% вы выберете пустую. Затем, из оставшихся 99 коробок ведущий открывает и показывает вам 98 пустых, а одну оставляет закрытой, и предлагает вам изменить изначальный выбор (который был проигрышным 99%).
"""

    await bot.send_message(message.from_user.id, msg)