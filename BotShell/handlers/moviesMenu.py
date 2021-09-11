from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, get_all_general_history, get_paper_count, get_trending_films
from ..utils.scroll_keyboard import page_open
from ..utils.keyboards import start_kerboard


async def movies_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(8)), telegram_markup(await get_message(9)), telegram_markup(await get_message(10)), telegram_markup(await get_message(11))], state='*')
    async def movies_menu_keyboard(message: types.Message, state: FSMContext):
        # Trending
        if message.text == telegram_markup(await get_message(8)):
            id_person = message['from']['id']
            text = message.text
            trending_films = await get_trending_films()
            print('len: '+str(len(trending_films)))
        #    all_general_history = await get_all_general_history()
            paper_count = await get_paper_count(id_person)

            page_inf = await page_open(trending_films, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text='🔥 Today Trending!')

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])

            await state.update_data(film_list=trending_films, len_list=len(trending_films), counter=0,
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
