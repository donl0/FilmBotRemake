from ..utils.dbcommands import year_genre_filter, get_films_by_genres, get_paper_count, get_films_by_year
from ..utils.keyboards import just_back_yrarf_keybard, Genre_keyboard, years_keyboard, just_back_ganre_keybard, \
    start_kerboard, movie_keyboard
from ..utils.scroll_keyboard import page_open, next_page_info1, previous_page_info1
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types


async def genres_year_logic_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=['Anime', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Fantasy',
              'Drama', 'Family', 'Family', 'Game Show', 'Horror', 'Music', 'Mystery', 'News', 'Reality-TV', 'Romance',
              'Sci-Fi', 'Sport', 'Superhero', 'Talk_Show', 'Thriller', 'War', 'Western'], state='*')
    async def genres_adding(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        text = message.text
        user_data = await state.get_data()
        # print('user_data: '+str(user_data))
        try:
            if user_data['year'] == 101:
                x = 4
                print('1' + x)
            #   print('x'+user_data['year'])
            film_list = await year_genre_filter(user_data['year'], text)

            x = 4
            print('годы')
            #   print('sdelal')
            x = 1
        #  print('x=1 1 ')
        except:
            print('жанры')
            film_list = await get_films_by_genres(text)
           # sql = cursor.execute(f"SELECT * FROM films_list WHERE (instr(genres, '{text}'));")
            x = 2
        # print('x=2')

        # sql=cursor.execute(f"SELECT * FROM films_list WHERE (instr(genres, '{text}'));")

      #  film_list = cursor.fetchall()
        film_list = tuple(reversed(film_list))
        # print(film_list)
        # page_inf = page_open(film_list, id_person)
        paper_count = await get_paper_count(id_person)
        page_inf = await page_open(film_list, paper_count, id_person)

        if x == 1:
            #  print('x=1 1 ')
            await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=just_back_yrarf_keybard)

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            #  await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_ganre_keybard)
            await OrderDataUser.sanding_films_Years.set()
        elif x == 2:
            # print('x=2 2')
            await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=just_back_yrarf_keybard)

            await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
            # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
            await OrderDataUser.sanding_films.set()

        '''
        if len(film_list)<5:
            len_list=len(film_list)
        else:
            len_list=5
        keyboard_film_list= InlineKeyboardMarkup(row_width=3)
        for i in range(len_list):
            film=film_list[i]
            item_f = InlineKeyboardButton(text=film[0]+'('+str(film[1])+')| HMDb '+str(film[2])+'/10', callback_data='find film')
            keyboard_film_list.row(item_f)
    
        item_page = InlineKeyboardButton(text='Page: 1', callback_data='11111')
        item_next_page = InlineKeyboardButton(text='Next page⏭', callback_data='next_page')
        keyboard_film_list.add(item_page, item_next_page)
        '''
        # await bot.send_message(chat_id =id_person, text=page_inf[0], reply_markup=page_inf[1])
        # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)

        await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, genre=text,
                                id_mes=message.message_id)
        await state.update_data(anime='sanding_films')
        # await OrderDataUser.sanding_films.set()

    @dp.message_handler(state=OrderDataUser.sanding_films_Years, text='Choose genre')
    async def Years_filter11(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        # user_data = await state.get_data()
        await bot.send_message(chat_id=id_person, text='Select genre of the movie, you want to find. ',
                               reply_markup=Genre_keyboard)

    @dp.message_handler(state=OrderDataUser.sanding_films_Years,text=['Anime', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
                                  'Documentary', 'Fantasy', 'Drama', 'Family', 'Family', 'Game Show', 'Horror', 'Music',
                                  'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Superhero',
                                  'Talk_Show', 'Thriller', 'War', 'Western'])
    async def Years_filter112(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            user_data = await state.get_data()
            await state.update_data(genre=message.text)
        # await OrderDataUser.waiting_for_Years.set()
        # await OrderDataUser.sanding_films.set()
    @dp.message_handler(state=[OrderDataUser.sanding_films], text='Choose year')
    async def Years_filter11(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        # user_data = await state.get_data()
        await bot.send_message(chat_id=id_person, text='Select a year of movies you want to find.',
                               reply_markup=years_keyboard)

    @dp.message_handler(
        text=[2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005,
              2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988,
              1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971,
              1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954,
              1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937,
              1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922],
        state=OrderDataUser.sanding_films)
    async def Years_filter1(message: types.Message, state: FSMContext):

        id_person = message['from']['id']
        text = message.text
        user_data = await state.get_data()
        # sql=cursor.execute(f"SELECT * FROM films_list WHERE year='{text}' AND (instr(genres, '{user_data['genre']}'));")
        # try:
        #  if
        #    sql=cursor.execute(f"SELECT * FROM films_list WHERE year='{text}' AND (instr(genres, '{user_data['genre']}'));")
        # except:
        #    print('сделал хуйню')
        #   sql=cursor.execute(f"SELECT * FROM films_list WHERE year='{text}' AND (instr(genres, ''));")
        # genre
        #  print(user_data['genre'])

        film_list = await year_genre_filter(text, user_data['genre'])
        film_list = tuple(reversed(film_list))
        # page_inf = page_open(film_list, id_person)

        paper_count = await get_paper_count(id_person)
        page_inf = await page_open(film_list, paper_count, id_person)

        await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
        await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=just_back_yrarf_keybard)

        # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)

        try:
            if user_data['genre'] == 101:
                x = 4
                print('1' + x)

            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, genre=user_data['genre'],
                                    year=text, id_mes=message.message_id)
        except:
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, genre='', year=text,
                                    id_mes=message.message_id)
        await OrderDataUser.sanding_films.set()

    @dp.message_handler(
        text=[2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005,
              2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988,
              1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971,
              1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954,
              1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937,
              1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922],
        state=[OrderDataUser.waiting_for_Years, OrderDataUser.sanding_films_Years, OrderDataUser.sanding_films])
    async def Years_filter1(message: types.Message, state: FSMContext):

        id_person = message['from']['id']
        text = message.text
        user_data = await state.get_data()
        # sql=cursor.execute(f"SELECT * FROM films_list WHERE year='{text}' AND (instr(genres, '{user_data['genre']}'));")
        try:
            if user_data['genre'] == 101:
                x = 4
                print('1' + x)
                # print('1'+x)
            film_list = await year_genre_filter(user_data['year'], text)
        except:
            film_list = await get_films_by_year(text)
        # genre


        film_list = tuple(reversed(film_list))
        # page_inf = page_open(film_list, id_person)
        paper_count = await get_paper_count(id_person)
        page_inf = await page_open(film_list, paper_count, id_person)

        await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
        await bot.send_message(chat_id=id_person, text='List of movies.', reply_markup=just_back_ganre_keybard)

        # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_ganre_keybard)

        try:
            if user_data['genre'] == 101:
                x = 4
                print('1' + x)

            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, genre=user_data['genre'],
                                    year=text, id_mes=message.message_id)
        except:
            await state.update_data(film_list=film_list, len_list=len(film_list), counter=0, genre='', year=text,
                                    id_mes=message.message_id)
        await OrderDataUser.sanding_films_Years.set()
    # waiting_for_Years

    @dp.callback_query_handler(state=OrderDataUser.sanding_films, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        #   print(call.inline_message_id)
        #  print(call.message.message_id)
        user_data = await state.get_data()
        # print(user_data)

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)

        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

        await OrderDataUser.sanding_films.set()

    @dp.callback_query_handler(state=OrderDataUser.sanding_films, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        # print('PREVIOUS')
        # print(call.inline_message_id)
        # print(call.message.message_id)
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

        await OrderDataUser.sanding_films.set()

    @dp.callback_query_handler(
        state=[OrderDataUser.sanding_films, OrderDataUser.waiting_for_Years, OrderDataUser.sanding_films_Years],
        text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        # print(call.inline_message_id)
        # print(call.message.message_id)
        user_data = await state.get_data()
        # print(user_data)

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

        await OrderDataUser.sanding_films_Years.set()

    @dp.callback_query_handler(state=OrderDataUser.sanding_films_Years, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        print('PREVIOUS')
        #  print(call.inline_message_id)
        # print(call.message.message_id)
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])


    @dp.callback_query_handler(state=OrderDataUser.sanding_films_Years, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        print('PREVIOUS')
        #  print(call.inline_message_id)
        # print(call.message.message_id)
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])


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
            print('1=')
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=await start_kerboard())
            # await state.finish()
            await OrderDataUser.to_start_menu.set()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.waiting_for_Years)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            await bot.send_message(chat_id=message['from']['id'], text='Select an action',
                                   reply_markup=movie_keyboard)
            await OrderDataUser.from_main_menu.set()

            await state.finish()

        @dp.message_handler(text='⬅ Back', state=OrderDataUser.sanding_films_Years)
        async def genres_adding(message: types.Message, state: FSMContext):
            id_person = message['from']['id']
            user_data = await state.get_data()
            id_person = message['from']['id']
            # await state.update_data(genre=1, year=1)
            await state.update_data(genre=101, year=101)
            await bot.send_message(chat_id=id_person, text='Select one year', reply_markup=years_keyboard)
            await OrderDataUser.waiting_for_Years.set()
            print('это?')