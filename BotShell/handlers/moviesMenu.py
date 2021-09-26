from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, get_all_general_history, get_paper_count, get_trending_films, \
    get_all_films, get_user_history, get_all_last_search
from ..utils.scroll_keyboard import page_open
from ..utils.keyboards import start_kerboard, top_keyboard1, Genre_keyboard, years_keyboard
from ..utils.tools import get_only_names2, get_only_names


async def movies_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(8)), telegram_markup(await get_message(9)), telegram_markup(await get_message(10)), telegram_markup(await get_message(11))], state='*')
    async def movies_menu_keyboard(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        # Trending
        if message.text == telegram_markup(await get_message(8)):
            id_person = message['from']['id']
            text = message.text

            # cursor.execute("SELECT name_film, year, rating, genres FROM films_list ORDER BY `all views` DESC LIMIT 6")
            # film_list= cursor.fetchall()

            films_last_s = tuple(reversed(await get_only_names(await get_all_general_history())))
            #  print(films_last_s)
            # films_last_s.reverse()
            #  page_inf = page_open(films_last_s, id_person)
            paper_count = await get_paper_count(id_person)
            page_inf = await page_open(films_last_s, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text='🔥 Today Trending!')

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=films_last_s, len_list=len(films_last_s), counter=0,
                                    id_mes=message.message_id)
            await state.update_data(anime='tranding1')
            await OrderDataUser.tranding1.set()
        # Recently added
        if message.text == telegram_markup(await get_message(9)):
          #  cursor.execute("SELECT name_film, year, rating, genres FROM films_list")
            film_list = await get_all_films()
            ##print(film_list)
            film_list = tuple(reversed(film_list))
            # print(film_list)
            # film_list=list(film_list[0]).reverse()
            # print(film_list)
            # page_inf = page_open(film_list, id_person)
            paper_count = await get_paper_count(id_person)

            page_inf = await page_open(film_list, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, id_mes=message.message_id)
            await state.update_data(anime='resently1')
            await OrderDataUser.resently1.set()
        # Top rated
        if message.text == telegram_markup(await get_message(10)):
            await bot.send_message(chat_id=id_person, text='Select section', reply_markup=await top_keyboard1())
            await OrderDataUser.top_all.set()
        # History
        if message.text == telegram_markup(await get_message(11)):
            film_list = await get_user_history(id_person)
            if len(film_list) == 0:
                text = 'Your history is empty('
                await bot.send_message(chat_id=id_person, text=text)
            else:
                paper_count = await get_paper_count(id_person)

                page_inf = await page_open(film_list, paper_count, id_person)
                text = page_inf[0]
                await bot.send_message(chat_id=id_person, text=text, reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, id_mes=message.message_id)
                await state.update_data(anime='hostory1')
                await OrderDataUser.history1.set()

    @dp.message_handler(text=[telegram_markup(await get_message(12)), telegram_markup(await get_message(13))], state='*')
    async def movies_menu_keyboard_browse(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        # Browse by Genre
        if message.text == telegram_markup(await get_message(12)):
            await bot.send_message(chat_id=id_person, text='Pick a genre', reply_markup=Genre_keyboard)
            await OrderDataUser.waiting_for_Genres.set()
        # Browse by Year
        if message.text == telegram_markup(await get_message(13)):
            await bot.send_message(chat_id=id_person, text='Select one year', reply_markup=years_keyboard)
            await OrderDataUser.waiting_for_Years.set()
