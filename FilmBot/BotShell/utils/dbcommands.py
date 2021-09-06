from ..models.messageEditor import Message
from ..models.filmInfo import Films
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