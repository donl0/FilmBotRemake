from aiogram import Bot, Dispatcher
from aiogram import types

from ..utils.dbcommands import get_message, films_top_24, get_paper_count, films_top_mouth, films_top_rating
from ..utils.scroll_keyboard import page_open
from ..utils.text import telegram_markup
from ..utils.states import OrderDataUser, FSMContext, State


async def top_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(70)), telegram_markup(await get_message(71)), telegram_markup(await get_message(72))], state='*')
    async def top_films_handler(message: types.Message, state: FSMContext):
        text = message.text
        id_person = message['from']['id']

        if text == telegram_markup(await get_message(70)):

            film_list = await films_top_24()
            film_list = tuple(reversed(film_list))
            #   print(film_list)
            # page_inf = page_open(film_list, id_person)
            paper_count = await get_paper_count(id_person)
            page_inf = await page_open(film_list, paper_count, id_person)
            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, id_mes=message.message_id)
            await state.update_data(anime='top_all')
            await OrderDataUser.top_all.set()
        elif text == 'Top of the month':
            film_list = await films_top_mouth()
            film_list = tuple(reversed(film_list))
           # film_list = tuple(reversed(film_list))
            # print(film_list)
            # page_inf = page_open(film_list, id_person)
            paper_count = await get_paper_count(id_person)
            page_inf = await page_open(film_list, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, id_mes=message.message_id)
            await state.update_data(anime='top_all')
            await OrderDataUser.top_all.set()

        elif text == 'Top IMDb':
            film_list = await films_top_rating()
            film_list = tuple(reversed(film_list))
            #  print(film_list)
            # page_inf = page_open(film_list, id_person)
            paper_count = await get_paper_count(id_person)
            page_inf = await page_open(film_list, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, id_mes=message.message_id)
            await state.update_data(anime='Top IMDb')
            await OrderDataUser.top_all.set()

