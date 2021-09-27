from django.db import models
#from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
from ..utils.text import clean_html_markup

class Message(models.Model):
    text = RichTextField(max_length=1024)
   # message_id = models.IntegerField(unique=True)
    msg_id = models.IntegerField(default=0, unique=True)

    def __str__(self):

        text = clean_html_markup(self.text)
        if len(text) > 30:
            return f'{text[:30]}...'
        else:
            return text

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
