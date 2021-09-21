from ..utils.film_show import film_create
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, get_all_general_history, get_paper_count, get_trending_films, \
    get_all_films, get_user_history, get_search_way
from ..utils.scroll_keyboard import page_open
from ..utils.keyboards import start_kerboard, top_keyboard1, Genre_keyboard, years_keyboard, main_m_keyboard, \
    search_keyboard, again_keyboard, just_back_k
from ..utils.tools import do_with_3_10_8_film_info


async def backs_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text='⬅ Back', state=OrderDataUser.request_list)
    async def rquest_mak(message: types.Message):
        id_person = message['from']['id']
        text = message.text
        await bot.send_message(chat_id=id_person, text='You are back to the main menu', reply_markup=start_kerboard)
        await OrderDataUser.to_start_menu.set()


    @dp.message_handler(text='⬅  Back', state=OrderDataUser.comment_v)
    async def comm_back(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        id_person = message['from']['id']
        print('SRABOTAL')
        # await state.update_data(film_name=mess)
        film_info = film_create(user_data['film_name'], id_person)
        film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10], film_info[8])
        film_info[3] = film_info_remake['film_info3']
        film_info[8] = film_info_remake['film_info8']
        film_info[10] = film_info_remake['film_info10']
        #  print('-----film_info-------')
        #  print(film_info)
        #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])

        # film_info[3]=film_info[3].replace(", "," #")

        await bot.send_message(chat_id=id_person, text=film_info[0] + '(' + str(film_info[1]) + ')',
                               reply_markup=await main_m_keyboard(user_data['film_name'], id_person))

        await bot.send_video(chat_id=id_person, video=film_info[4],
                             caption='*' + film_info[0] + '(' + str(film_info[1]) + ')*' + '\n\n_Genre: ' + str(
                                 film_info[3]) + '_\n' + str(film_info[8]) + '\nIMDb: *' + str(
                                 film_info[2]) + '*' + '\n_Dirctor: ' + film_info[9] + '\nActors: ' + film_info[
                                         10] + '_', reply_markup=film_info[7],
                             parse_mode="Markdown")  # as_html=True#parse_mode=ParseMode.MARKDOWN

        try:
            if user_data['anime'] == 1:
                await OrderDataUser.to_start_menu.set()
            elif user_data['anime'] == 'tranding1':
                await OrderDataUser.tranding1.set()
            elif user_data['anime'] == 'popular1':
                await OrderDataUser.popular1.set()
            elif user_data['anime'] == 'sanding_films':
                await OrderDataUser.sanding_films.set()
            elif user_data['anime'] == 'resently1':
                await OrderDataUser.resently1.set()
            elif user_data['anime'] == 'top_all':
                await OrderDataUser.top_all.set()
            elif user_data['anime'] == 'Top IMDb':
                await OrderDataUser.top_all.set()
        except:
            print("user_data['anime'] not exist")


    @dp.message_handler(text='⬅  Back', state='*')
    async def genres_adding(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        user_data = await state.get_data()
        try:
            film_inf = user_data['film_name']
            film_info = await film_create(film_inf, id_person)
            #  print('-----film_info-------')
            #  print(film_info)
            #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])
            film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10], film_info[8])
            film_info[3] = film_info_remake['film_info3']
            film_info[8] = film_info_remake['film_info8']
            film_info[10] = film_info_remake['film_info10']
            await bot.send_message(chat_id=id_person, text=film_info[0] + '(' + str(film_info[1]) + ')',
                                   reply_markup=await main_m_keyboard(film_inf, id_person))

            await bot.send_video(chat_id=id_person, video=film_info[4],
                                 caption='*' + film_info[0] + '(' + str(film_info[1]) + ')*' + '\n\n_Genre: ' + str(
                                     film_info[3]) + '_\n' + str(film_info[8]) + '\nIMDb: *' + str(
                                     film_info[2]) + '*' + '\n_Dirctor: ' + film_info[9] + '\nActors: ' + film_info[
                                             10] + '_', reply_markup=film_info[7],
                                 parse_mode="Markdown")  # as_html=True#parse_mode=ParseMode.MARKDOWN
        except:
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=start_kerboard)
            # await state.finish()
            await OrderDataUser.to_start_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.from_main_menu)
        async def genres_adding(message: types.Message):
            # await bot.answer(text='🏠 You are back to main menu', reply_markup=start_kerboard)
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=start_kerboard)
            # await state.finish()
            await OrderDataUser.to_start_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.waiting_for_filter)
        async def genres_adding(message: types.Message):

            # await bot.answer(text='🏠 You are back to main menu', reply_markup=start_kerboard)
            await bot.send_message(chat_id=message['from']['id'], text='Select an action', reply_markup=movie_keyboard)
            await OrderDataUser.from_main_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.waiting_for_Genres)
        async def genres_adding(message: types.Message):
            id_person = message['from']['id']
            await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=movie_keyboard)
            await OrderDataUser.from_main_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.sanding_films)
        async def genres_adding(message: types.Message, state: FSMContext):
            user_data = await state.get_data()
            id_person = message['from']['id']
            # await state.update_data(genre=1, year=1)
            await state.update_data(genre=101, year=101)
            # print('это')
            try:
                x = user_data['genre'] + str(1)
                await bot.send_message(chat_id=id_person, text='Pick a genre', reply_markup=Genre_keyboard)
                await OrderDataUser.waiting_for_Genres.set()
            except:
                await bot.send_message(chat_id=id_person, text='Select one year', reply_markup=years_keyboard)
                await OrderDataUser.waiting_for_Years.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.waiting_for_Years)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            # print('это2')
            await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=movie_keyboard)
            await OrderDataUser.from_main_menu.set()
            # print('это2')

        # await OrderDataUser.waiting_fot_help.set()
        @dp.message_handler(text='⬅ Back', state=OrderDataUser.waiting_fot_help)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            await bot.send_message(chat_id=id_person, text='You are back to the main menu', reply_markup=start_kerboard)
            await OrderDataUser.to_start_menu.set()

        #        await OrderDataUser.after_question.set()
        @dp.message_handler(text='⬅ Back', state=OrderDataUser.after_question)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            await bot.send_message(chat_id=id_person, text='Select a section', reply_markup=info_keyb)
            await OrderDataUser.waiting_fot_help.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.box_state)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            await bot.send_message(chat_id=id_person, text='Select section', reply_markup=start_kerboard)
            await OrderDataUser.to_start_menu.set()

        @dp.message_handler(text='⬅ Back',
                            state=[OrderDataUser.resently1, OrderDataUser.popular1, OrderDataUser.history1,
                                   OrderDataUser.my_prof_st, OrderDataUser.tranding1])
        async def genres_adding(message: types.Message):
            # await bot.answer(text='🏠 You are back to main menu', reply_markup=start_kerboard)
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=start_kerboard)
            # await state.finish()
            await OrderDataUser.to_start_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.top_all)
        async def genres_adding(message: types.Message):

            await bot.send_message(chat_id=message['from']['id'], text='Select an action', reply_markup=movie_keyboard)
            await OrderDataUser.from_main_menu.set()

        @dp.message_handler(text='⬅ Back', state=[OrderDataUser.search_page1, OrderDataUser.search_stars,
                                                  OrderDataUser.search_director, OrderDataUser.search_by_all])
        async def genres_adding(message: types.Message):
            id_person = message['from']['id']

            search_way = await get_search_way(id_person)

            await bot.send_message(chat_id=message['from']['id'],
                                   text='🔍 What movie are you looking for?\nSearch: ' + search_way,
                                   reply_markup=search_keyboard)
            await OrderDataUser.search_page1.set()

        @dp.message_handler(text='⬅️ Back', state='*')
        async def genres_adding(message: types.Message, state: FSMContext):
            user_data = await state.get_data()
            id_person = message['from']['id']
            user_data = await state.get_data()
            mass_anime = ['by all', 'by director', 'by actor', 'by name']
            await state.update_data(film_name=4)
            #  print('назад')
            try:

                if user_data['anime'] in mass_anime:
                    paper_count = await get_paper_count(id_person)
                    page_inf = await page_open(user_data['film_list'], paper_count, id_person)
                    await state.update_data(film_list=user_data['film_list'], len_list=len(user_data['film_list']),
                                            counter=0, id_mes=message.message_id)
                    await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=again_keyboard)
                    await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                else:
                    paper_count = await get_paper_count(id_person)
                    page_inf = await page_open(user_data['film_list'], paper_count, id_person)
                    await state.update_data(film_list=user_data['film_list'], len_list=len(user_data['film_list']),
                                            counter=0, id_mes=message.message_id)
                    await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=just_back_k)
                    await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            except:
                await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                       reply_markup=start_kerboard)
                # await state.finish()
                await OrderDataUser.to_start_menu.set()



