from .dbcommands import get_all_by_film_name, get_admin
from keyboards import InlineKeyboardMarkup,InlineKeyboardButton
#from db_cursor import cursor, conn
#from config import admin_id
def film_create(film_name, id_person):
  admin_id = await get_admin()
  #keyb for filn 👍👎🏿🧡▶️💬
#   print('-------------------')
#   print(film_name)
  #print(film_name[0][0])
  film_name=film_name.replace("'", "''")
  film_inf = await get_all_by_film_name(film_name)
  cursor.execute(f"SELECT * from `films_list` WHERE name_film='{film_name}'")
  comm = cursor.fetchone()

  cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
  comm_list = cursor.fetchone()[0]
  mass_i=[9,10,12]
  list2=list(comm)
  for i in mass_i:
    if list2[i]>1000:
      
      print(list2[i])
      list2[i]=list2[i]/1000
      
      list2[i]=round(list2[i],1)
      list2[i]=str(list2[i])
      if list2[i][-1]=='0':
        list2[i]=list2[i][:-2]
      #list2[i]=int(list2[i])

      print(comm[i], list2[i])
    #  comm_int=comm[i]
      list_int=list2[i]
      list_int+='K'
      comm=list(comm)
      comm[i]=list_int
  if not film_name in comm_list:
  # print('----------COMM------')
  # print(comm)
    next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    item_film_like = InlineKeyboardButton(text='😍 '+str(comm[9]), callback_data='like video')
    item_film_dislike = InlineKeyboardButton(text='🤬 '+str(comm[10]), callback_data='dislike video')
    item_comm = InlineKeyboardButton(text='💬 ' +str(comm[12]), callback_data='comment video')
    item_fav = InlineKeyboardButton(text='🧡 Favourite', callback_data='add favourite')
    item_watch_f = InlineKeyboardButton(text='▶️ Watch now', callback_data='start watching')
    item_searc_an = InlineKeyboardButton(text='🔍 Search another', switch_inline_query_current_chat='')
    #next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_fav, item_watch_f).row(item_searc_an)
    if id_person in admin_id:
      item_add_tr = InlineKeyboardButton(text='Add to popular', callback_data='Add_to_tranding')
      item_del_tr = InlineKeyboardButton(text='Remove from popular', callback_data='Del_from_tranding')
      item_delete_film = InlineKeyboardButton(text='Delete movie', callback_data='totally delete')
      item_hide_film = InlineKeyboardButton(text='Hide movie', callback_data='totally hide')
      next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_watch_f, item_searc_an).add(item_add_tr, item_del_tr).row(item_hide_film, item_delete_film)
    else:
      next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_watch_f, item_searc_an)
  #  print('----------COMM------')
    #print(comm)
  # print(comm[0], comm[1], comm[2], comm[3], comm[5], comm[11], comm[12])
    return [comm[0], comm[1], comm[2], comm[3], comm[5], comm[11], comm[12], next_step_keyboard, comm[4], comm[16], comm[17]]
  else:
    next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    item_film_like = InlineKeyboardButton(text='😍 '+str(comm[9]), callback_data='like video')
    item_film_dislike = InlineKeyboardButton(text='🤬 '+str(comm[10]), callback_data='dislike video')
    item_comm = InlineKeyboardButton(text='💬 ' +str(comm[12]), callback_data='comment video')
    item_fav = InlineKeyboardButton(text='🚫 Remove', callback_data='del favourite')
    item_watch_f = InlineKeyboardButton(text='▶️ Watch now', callback_data='start watching')
    item_searc_an = InlineKeyboardButton(text='🔍 Search another', switch_inline_query_current_chat='')
    #next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_fav, item_watch_f).row(item_searc_an)
    if id_person in admin_id:
      item_add_tr = InlineKeyboardButton(text='Add to popular', callback_data='Add_to_tranding')
      item_del_tr = InlineKeyboardButton(text='Remove from popular', callback_data='Del_from_tranding')
      item_delete_film = InlineKeyboardButton(text='Delete movie', callback_data='totally delete')
      item_hide_film = InlineKeyboardButton(text='Hide movie', callback_data='totally hide')
      next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_watch_f, item_searc_an).add(item_add_tr, item_del_tr).row(item_hide_film, item_delete_film)
    else:
      next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_watch_f, item_searc_an)
  #  print('----------COMM------')
    #print(comm)
  # print(comm[0], comm[1], comm[2], comm[3], comm[5], comm[11], comm[12])
    return [comm[0], comm[1], comm[2], comm[3], comm[5], comm[11], comm[12], next_step_keyboard, comm[4], comm[16], comm[17]]