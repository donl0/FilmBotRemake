from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types

async def search_keyboard_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(state=OrderDataUser.search_page1, content_types=types.ContentTypes.TEXT)
    async def search_keyboard(message: types.Message, state: FSMContext):
        text = message.text
        id_person = message['from']['id']
        if text == '🕵️‍♂️ What others search':
            a = np.load('last_search.npy')
            string = ''
            for i in a:
                string += '- ' + str(i) + '\n'
                # await bot.send_message(chat_id=id_person, text=i[0])

            await bot.send_message(chat_id=id_person, text=string)
        elif text == '⚙️ Search filter':
            #   print('FF0')
            cursor.execute(f"SELECT `search way` FROM user_info WHERE id_tele='{id_person}'")
            search_way = cursor.fetchone()[0]

            cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
            paper_count = cursor.fetchone()[0]

            search_keyboard1 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            item_back = InlineKeyboardButton(text='⬅ Back')
            item_search1 = InlineKeyboardButton(text='🗒 Search: ' + search_way)
            item_filter_search2 = InlineKeyboardButton(text='🔢 Movies per page: ' + str(paper_count))

            search_keyboard1.insert(item_back).add(item_search1, item_filter_search2)
            await bot.send_message(chat_id=id_person,
                                   text='⚠️Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=search_keyboard1)
            await OrderDataUser.Search_filter1.set()
        elif text == '⬅ Back':
            # await bot.answer(text='🏠 You are back to main menu', reply_markup=start_kerboard)
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=start_kerboard)
            # await state.finish()
            await OrderDataUser.to_start_menu.set()
        else:
            cursor.execute(f"SELECT `search way` FROM user_info WHERE id_tele='{id_person}'")
            search_way = cursor.fetchone()[0]
            if search_way == 'by name':  # instr
                cursor.execute(f"SELECT name_film, year, rating, genres  FROM films_list WHERE instr(name_film, '{text}')")
                film_info = cursor.fetchall()

                cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
                paper_count = cursor.fetchone()[0]

                page_inf = page_open1(film_info, paper_count, id_person)
                if not film_info == '':
                    x = True
                    #  np.save('last_search', a)

                    # a=film_info[0][0]
                    # print(page_inf)
                    try:
                        films_last_s = np.load('last_search.npy')
                        films_last_s = list(films_last_s)
                        a = film_info[0][0]
                        if film_info[0][0] in films_last_s:
                            a = film_info[1][0]
                            if film_info[1][0] in films_last_s:
                                x = False

                        if len(films_last_s) < 10 and x == True:
                            films_last_s.append(a)
                            random.shuffle(films_last_s)

                            np.save('last_search', films_last_s)
                        elif x == True:
                            rand_num = random.randint(1, 10)
                            del films_last_s[rand_num]
                            films_last_s.append(a)
                            random.shuffle(films_last_s)

                            np.save('last_search', films_last_s)
                    except:
                        pass
                try:
                    await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                    # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                    await state.update_data(film_list=film_info, len_list=len(film_info), counter=0,
                                            id_mes=message.message_id)
                    await state.update_data(anime='by name')
                    await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                    await OrderDataUser.by_name1.set()  # by_name1
                except:
                    await bot.send_message(chat_id=id_person,
                                           text='Sorry we don’t have movie\nWe recommend that you use 📮 Request page, to submitt your movie request. ')
            elif search_way == 'by actor':  # instr
                cursor.execute(f"SELECT name_film, year, rating, genres  FROM films_list WHERE instr(Stars, '{text}')")
                film_info = cursor.fetchall()

                cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
                paper_count = cursor.fetchone()[0]

                page_inf = page_open1(film_info, paper_count, id_person)
                try:
                    await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                    # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                    await state.update_data(film_list=film_info, len_list=len(film_info), counter=0,
                                            id_mes=message.message_id)
                    await state.update_data(anime='by actor')

                    await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                    await OrderDataUser.search_stars.set()
                except:
                    await bot.send_message(chat_id=id_person,
                                           text='Sorry we don’t have movie\nWe recommend that you use 📮 Request page, to submitt your movie request. ')

            elif search_way == 'by director':
                cursor.execute(f"SELECT name_film, year, rating, genres  FROM films_list WHERE instr(Director, '{text}')")
                film_info = cursor.fetchall()

                cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
                paper_count = cursor.fetchone()[0]

                page_inf = page_open1(film_info, paper_count, id_person)
                await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_info, len_list=len(film_info), counter=0, id_mes=message.message_id)
                await state.update_data(anime='by director')
                await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                await OrderDataUser.search_director.set()
                # by all
            elif search_way == 'by all':
                cursor.execute(
                    f"SELECT name_film, year, rating, genres  FROM films_list WHERE instr(Director, '{text}') OR instr(Stars, '{text}') OR instr(name_film, '{text}')")
                film_info = cursor.fetchall()

                cursor.execute(f"SELECT `paper count` FROM user_info WHERE id_tele='{id_person}'")
                paper_count = cursor.fetchone()[0]

                page_inf = page_open1(film_info, paper_count, id_person)
                await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_info, len_list=len(film_info), counter=0, id_mes=message.message_id)
                await state.update_data(anime='by all')
                await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                await OrderDataUser.search_by_all.set()