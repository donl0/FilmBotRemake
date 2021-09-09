from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message
from ..utils.keyboards import start_kerboard, movie_keyboard_kerboard


async def main_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(0)), await get_message(1), await get_message(2), await get_message(3), await get_message(4), await get_message(5), await get_message(6), await get_message(7)], state='*')
    async def menu_keyboard(message: types.Message,  state: FSMContext):
        id_person = message['from']['id']
        # 🔍 Search
        if message.text == telegram_markup(await get_message(0)):
            #await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=await start_kerboard())
            pass
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
            await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=movie_keyboard_kerboard)
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
            