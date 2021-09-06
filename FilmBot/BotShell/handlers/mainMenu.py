from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message
from ..utils.keyboards import start_kerboard


async def main_menu_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(0)), '🔥 Popular', '📂 My profile', '❤️ My favorites', '🎬 Movies', '🍿 TV Shows', '👨‍💻 Help', '📮 Request'], state='*')
    async def menu_keyboard(message: types.Message,  state: FSMContext):
        id_person = message['from']['id']
        if message.text == telegram_markup(await get_message(0)):
            await bot.send_message(chat_id=id_person, text='Select an action', reply_markup=await start_kerboard())
            