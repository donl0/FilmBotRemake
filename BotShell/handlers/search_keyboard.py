from ..utils.dbcommands import get_all_last_search, get_search_way, get_paper_count, get_all_by_contain_film, \
    add_to_all_last_search, get_all_by_star, get_all_by_director_film, get_all_by_all_preference_search, \
    update_paper_count, update_search_way
from ..utils.keyboards import start_kerboard, again_keyboard, search_keyboard1, search_keyboard2, search_keyboard_str
from ..utils.scroll_keyboard import page_open
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import re

from ..utils.tools import get_only_names2, get_only_names


async def search_keyboard_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(state=OrderDataUser.search_page1, content_types=types.ContentTypes.TEXT)
    async def search_keyboard_(message: types.Message, state: FSMContext):
        text = message.text
        id_person = message['from']['id']
        if text == '🕵️‍♂️ What others search':
            last_search = await get_all_last_search()
            last_search = tuple(reversed(last_search))
            last_search = await get_only_names(last_search)
            string = ''
            if len(last_search) == 0:
                string += 'Search history is empty'
            else:
                for i in range(6):
                    try:
                        string += '- ' + str(last_search[i].film_name) + '\n'
                    except:
                        break
                # await bot.send_message(chat_id=id_person, text=i[0])

            await bot.send_message(chat_id=id_person, text=string)
        elif text == '⚙️ Search filter':
            search_way = await get_search_way(id_person)

            paper_count = await get_paper_count(id_person)

            search_keyboard = search_keyboard1(search_way, paper_count)
            await bot.send_message(chat_id=id_person,
                                   text='⚠️Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=search_keyboard)

            await OrderDataUser.Search_filter1.set()
        elif text == '⬅ Back':
            # await bot.answer(text='🏠 You are back to main menu', reply_markup=start_kerboard)
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',reply_markup=await start_kerboard())            # await state.finish()
            await OrderDataUser.to_start_menu.set()
        else:
            search_way = await get_search_way(id_person)
            print(search_way)
            if search_way == 'by name':  # instr
                film_info = await get_all_by_contain_film(text)

                paper_count = await get_paper_count(id_person)

                page_inf = await page_open(film_info, paper_count, id_person)
                if len(film_info) != 0:
                    x = True
                    await add_to_all_last_search(film_info[0].film_name)
                    #await add_to_all_last_search()
                    #  np.save('last_search', a)

                    # a=film_info[0][0]
                    # print(page_inf)


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
                film_info = await get_all_by_star(text)

                paper_count = await get_paper_count(id_person)

                page_inf = await page_open(film_info, paper_count, id_person)
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
                film_info = await get_all_by_director_film(text)

                paper_count = await get_paper_count(id_person)

                page_inf = await page_open(film_info, paper_count, id_person)
                await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_info, len_list=len(film_info), counter=0, id_mes=message.message_id)
                await state.update_data(anime='by director')
                await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                await OrderDataUser.search_director.set()
                # by all
            elif search_way == 'by all':
                film_info = await get_all_by_all_preference_search(text)

                paper_count = await get_paper_count(id_person)

                page_inf = await page_open(film_info, paper_count, id_person)
                await bot.send_message(chat_id=id_person, text=page_inf[0], reply_markup=page_inf[1])
                # await bot.send_message(chat_id =id_person, text='----------------------------------------------', reply_markup=just_back_yrarf_keybard)
                await state.update_data(film_list=film_info, len_list=len(film_info), counter=0, id_mes=message.message_id)
                await state.update_data(anime='by all')
                await bot.send_message(chat_id=id_person, text='🔍 Search ', reply_markup=again_keyboard)
                await OrderDataUser.search_by_all.set()
        #await OrderDataUser.Search_filter1.set()


    @dp.message_handler(state=OrderDataUser.Search_filter1, content_types=types.ContentTypes.TEXT)
    async def start_getter(message: types.Message, state: FSMContext):
        text = message.text
        id_person = message['from']['id']
        if text.startswith('🔢 Movies per page:'):
            phoneNum = re.compile(r':([\s\S]+)')
            Fn = phoneNum.search(text)
            num = Fn.group(1)
            mass = [3, 5, 8, 12, 15]
            search_keyboard = search_keyboard2(num, mass)
            await bot.send_message(chat_id=id_person, text='🔢 Movies per page:', reply_markup=search_keyboard)
            # оставить этот же
            await OrderDataUser.Search_filter1.set()
        elif text in ['3', '5', '8', '12', '15']:
            await update_paper_count(text, id_person)
            search_way = await get_search_way(id_person)
          #  search_keyboard = search_keyboard1(search_way, paper_count)
            movie_keyboard = search_keyboard1(search_way, text)
            await bot.send_message(chat_id=id_person,
                                   text='⚠️ Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=movie_keyboard)
            # оставить этот же
            await OrderDataUser.Search_filter1.set()
        elif text.startswith('✅'):
            text = text[1:]
            await update_paper_count(text, id_person)

            search_way = await get_search_way(id_person)

            movie_keyboard = search_keyboard1(search_way, text)

            await bot.send_message(chat_id=id_person,
                                   text='⚠️ Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=movie_keyboard)
            # оставить этот же
            await OrderDataUser.Search_filter1.set()
        elif text.startswith('🗒 Search:'):
            phoneNum = re.compile(r': ([\s\S]+)')
            Fn = phoneNum.search(text)
            num = Fn.group(1)

            mass = ['by name', 'by actor', 'by director', 'by all']
            # item_back = InlineKeyboardButton(text='⬅ Back')
            # search_keyboard_all.insert(item_back)
            search_keyboard_all = search_keyboard_str(num, mass)

            await bot.send_message(chat_id=id_person,
                                   text='⚠️ Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=search_keyboard_all)
            # оставляем это
            # await OrderDataUser.search_page1.set()
            await OrderDataUser.search_page2.set()  # типа тюда вниз
        elif text == '⬅ Back':
            search_way = await get_search_way(id_person)
            paper_count = await get_paper_count(id_person)

            movie_keyboard = search_keyboard1(search_way, paper_count)


            await bot.send_message(chat_id=message['from']['id'],
                                   text='🔍 What movie are you looking for?\nSearch: ' + search_way,
                                   reply_markup=movie_keyboard)
            await OrderDataUser.search_page1.set()

    @dp.message_handler(state='*', text=['⤴️ Back', '🔁 Again'])
    async def start_getter(message: types.Message, state: FSMContext):
        text = message.text
        id_person = message['from']['id']
        if text == '⤴️ Back':
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu',
                                   reply_markup=start_kerboard)
            # await state.finish()
            await OrderDataUser.to_start_menu.set()
        elif text == '🔁 Again':
            search_way = await get_search_way(id_person)
            paper_count = await get_paper_count(id_person)

            search_keyboard = search_keyboard1(search_way, paper_count)

            await bot.send_message(chat_id=message['from']['id'],
                                   text='🔍 What movie are you looking for?\nSearch: ' + search_way,
                                   reply_markup=search_keyboard)
            await OrderDataUser.search_page1.set()

    @dp.message_handler(state='*',
                        text=['✅ by name', '✅ by actor', '✅ by director', '✅ by all', 'by name', 'by actor',
                              'by director', 'by all'])
    async def start_getter(message: types.Message):
        text = message.text
        id_person = message['from']['id']
        mass = ['by name', 'by actor', 'by director', 'by all']
        paper_count = await get_paper_count(id_person)

        if text in mass:
            # text=text[1:]
            await update_search_way(text, id_person)
            search_keyboard = search_keyboard1(text, paper_count)
            await bot.send_message(chat_id=id_person,
                                   text='⚠️Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=search_keyboard)

            # await bot.send_message(chat_id=message['from']['id'], text='🔍 What movie are you looking for?\nSearch: '+search_way, reply_markup=search_keyboard)
            await OrderDataUser.Search_filter1.set()
        if text.startswith('✅'):
            text = text[1:]
            await update_search_way(text, id_person)
            movie_keyboard1 = search_keyboard1(text, paper_count)
            await bot.send_message(chat_id=id_person,
                                   text='⚠️ Please note. Search filter automatically remembers your previously saved settings.',
                                   reply_markup=movie_keyboard1)
        await OrderDataUser.Search_filter1.set()