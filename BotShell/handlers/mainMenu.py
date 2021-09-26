from ..utils.scroll_keyboard import page_open
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, test1, get_search_way, get_trending_films, get_paper_count, \
    get_favourite_user
from ..utils.keyboards import start_kerboard, movie_keyboard_kerboard, top_keyboard, search_keyboard, my_prof_keyboard, \
    box_keyboard1
from ..utils.tools import get_only_names


async def main_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(0)), telegram_markup(await get_message(1)), telegram_markup(await get_message(2)), telegram_markup(await get_message(3)), telegram_markup(await get_message(4)), telegram_markup(await get_message(5)), telegram_markup(await get_message(6)), telegram_markup(await get_message(7))], state='*')
    async def menu_keyboard(message: types.Message,  state: FSMContext):
        id_person = message['from']['id']
        # 🔍 Search
        if message.text == telegram_markup(await get_message(0)):
            search_way = await get_search_way(id_person)

            await bot.send_message(chat_id=message['from']['id'],
                                   text='🔍 What movie are you looking for?\nSearch: ' + search_way,
                                   reply_markup=search_keyboard)
            await OrderDataUser.search_page1.set()
        # 🔥 Popular
        if message.text == telegram_markup(await get_message(1)):
            text = message.text
            trending_films = await get_trending_films()
            print('len: ' + str(len(trending_films)))
            #    all_general_history = await get_all_general_history()
            paper_count = await get_paper_count(id_person)

            page_inf = await page_open(trending_films, paper_count, id_person)

            await bot.send_message(chat_id=id_person, text='🔥 Today Trending!')

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])

            await state.update_data(film_list=trending_films, len_list=len(trending_films), counter=0,
                                    id_mes=message.message_id)
            await state.update_data(anime='tranding1')
            await OrderDataUser.tranding1.set()
        # 📂 My profile
        if message.text == telegram_markup(await get_message(2)):
            user_name = message['from']['username']
            user_name = user_name.replace("_", " ")
            await bot.send_message(chat_id=id_person,
                                   text=f'👋 Hello *{user_name}*!\nWelcome to you personal profile. ',
                                   reply_markup=my_prof_keyboard, parse_mode="Markdown")
            await OrderDataUser.my_prof_st.set()
        # ❤️ My favorites
        if message.text == telegram_markup(await get_message(3)):
            comm_list = await get_only_names(await get_favourite_user(id_person))
            # film_list=comm_list
            # print(comm_list)
            if len(comm_list) == 0:
                await bot.send_message(chat_id=id_person, text='Your favourite list is empty😓')
            else:
                paper_count = await get_paper_count(id_person)
                film_list = tuple(reversed(comm_list))
                # print(film_list)
                page_inf = await page_open(film_list, paper_count, id_person)
                await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_list, len_list=len(film_list), counter=0,
                                        id_mes=message.message_id)
                await state.update_data(anime='tranding1')

                await OrderDataUser.favorite_st.set()
        # 🎬 Movies
        if message.text == telegram_markup(await get_message(4)):
            print('popal')
            await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=await movie_keyboard_kerboard())
            #await bot.send_message(chat_id=id_person, text='Select an action',
             #                      reply_markup=await top_keyboard13())
            await OrderDataUser.from_main_menu.set()
        # 🍿 TV Shows
        if message.text == telegram_markup(await get_message(5)):
            pass
        # 👨‍💻 Help
        if message.text == telegram_markup(await get_message(6)):
            pass
        # 📮 Request
        if message.text == telegram_markup(await get_message(7)):
            await bot.send_message(chat_id=id_person,
                                   text=telegram_markup(await get_message(92)), reply_markup=await box_keyboard1())
            await OrderDataUser.box_state.set()
            