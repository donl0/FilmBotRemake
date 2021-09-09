from ..models.messageEditor import Message
from ..models.filmInfo import Films, Genres
from ..models.star import Stars
from ..models.director import Directors
from ..models.admindb import Admins
#from .. import models
from asgiref.sync import sync_to_async

@sync_to_async
def get_all_info():
    x = Films.objects.filter()
    #print(x)
   # print(x[0])
   # print(x[0].video_cotent)
    print(x[0])
    return x[0]


@sync_to_async
def get_message(msg_id):
    text = Message.objects.filter(msg_id=msg_id)
    return text[0].text


@sync_to_async
def genre_create(genres):
    print(genres)
    print(genres[0])
    print(genres[1])
    for genre in genres:
        Genres.objects.get_or_create(genre_name=genre)


@sync_to_async
def stars_create(stars):
    for star in stars:
        Stars.objects.get_or_create(name=star)


@sync_to_async
def directors_create(director):
    Directors.objects.get_or_create(name=director)


@sync_to_async
def film_create(info, genres, stars, director):
#def film_create(info):
    film = Films.objects.get_or_create(**info)
   # film = Films.objects.create(**info)
    #film_name
    #film = Films.objects.get_or_create(film_name=info['film_name'])
   # film = Films.objects.get_or_create(film_name='1')
    print(film)
  #  print(film[0])
    for genre in genres:
        #film[0].objects.update(genres=Genres.objects.filter(genre_name=genre))
        #film2 = Films.objects.filter(film_name=film[0].film_name)
       # for film_ in film2:
     #       film_.genres.add(Genres.objects.get(genre_name=genre))
        film[0].genres.add(Genres.objects.get(genre_name=genre))
    for star in stars:
        film[0].stars.add(Stars.objects.get(name=star))

    film[0].director.add(Directors.objects.get(name=director))

       # film[0].genres.add(genres=Genres.objects.filter(genre_name=genre))


@sync_to_async
def get_admin():
    admins = Admins.objects.filter()
    mass_admins = []
    for admin in admins:
        mass_admins.append(admin.admin_id)
    print(mass_admins)
   # admins = list(admins)
   # print(admins)
    return mass_admins
