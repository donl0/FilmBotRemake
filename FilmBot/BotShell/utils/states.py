from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
#from main import dp

class OrderDataUser(StatesGroup):
    waiting_for_Genres = State()
    waiting_for_Years = State()
    waiting_for_Years_mix = State()
    sanding_films = State()
    after_question = State()
    comment_v = State()
    sanding_films2 = State()
    sanding_films_Years = State()
    Subscribed1 = State()
    my_prof_st = State()

    top_all = State()
    to_del_tr = State()
    to_add_tr = State()
    popular1 = State()
    history1 = State()

    tranding1 = State()
    resently1 = State()
    top1 = State()

    top_m =State()
    top_24 = State()
    box_state = State()
    waiting_fot_help = State()

    waiting_for_filter = State()

    from_main_menu= State()

    to_movie = State()

    to_start_menu = State()

    request_list = State()

    search_page1 = State()
    search_page2 = State()
    search_page3 = State()
    Search_filter1 = State()
    by_name1 = State()
    search_stars = State()
    search_director = State()
    search_by_all = State()
    send_or_no= State()
    adv_ph_c_wait2=State()
    favorite_st =State()