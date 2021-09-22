from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, test1, get_search_way
from ..utils.keyboards import start_kerboard, movie_keyboard_kerboard, top_keyboard, search_keyboard


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
            pass
        # 📂 My profile
        if message.text == telegram_markup(await get_message(2)):
            pass
        # ❤️ My favorites
        if message.text == telegram_markup(await get_message(3)):
            pass
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
            pass
            