from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message
from ..utils.keyboards import start_kerboard


async def movies_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(8)), telegram_markup(await get_message(9)), telegram_markup(await get_message(10)), telegram_markup(await get_message(11))], state='*')
    async def movies_menu_keyboard(message: types.Message, state: FSMContext):
        # Trending
        if message.text == telegram_markup(await get_message(8)):
            id_person = message['from']['id']
            text = message.text

            # cursor.execute("SELECT name_film, year, rating, genres FROM films_list ORDER BY `all views` DESC LIMIT 6")
            # film_list= cursor.fetchall()
            films_last_s = np.load('all_history.npy')
            films_last_s = list(films_last_s)
            films_last_s = tuple(reversed(films_last_s))
            #  print(films_last_s)
            # films_last_s.reverse()
            #  page_inf = page_open(films_last_s, id_person)
            cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
            paper_count = cursor.fetchone()[0]
            page_inf = page_open1(films_last_s, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text='🔥 Today Trending!')

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await state.update_data(film_list=films_last_s, len_list=len(films_last_s), counter=0,
                                    id_mes=message.message_id)
            await state.update_data(anime='tranding1')
            await OrderDataUser.tranding1.set()
        # Recently added
        if message.text == telegram_markup(await get_message(9)):
            pass
        # Top rated
        if message.text == telegram_markup(await get_message(10)):
            pass
        # History
        if message.text == telegram_markup(await get_message(11)):
            pass

    @dp.message_handler(text=[telegram_markup(await get_message(12)), telegram_markup(await get_message(13))], state='*')
    async def movies_menu_keyboard_browse(message: types.Message, state: FSMContext):
        # Browse by Genre
        if message.text == telegram_markup(await get_message(12)):
            pass
        # Browse by Year
        if message.text == telegram_markup(await get_message(13)):
            pass
