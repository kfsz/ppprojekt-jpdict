from django.db import models

# Create your models here.

class Word (models.Model):
    word = models.CharField(max_length = 80, default = '')
    reading = models.CharField(max_length = 80, default = '')
    alterword = models.CharField(max_length = 80, default = '')
    alterreading = models.CharField(max_length = 140, default = '')
    common = models.BooleanField(default = 'False')
    #included_kanji // for when kanjis will appear here
    #also jlpt/other tags/maybe links // better generate them
    #misc field from JMDict
    def __str__(self):
        return self.word

class WordTL (models.Model):
    word = models.ForeignKey(Word, max_length = 80, related_name = 'meanings',  on_delete = models.CASCADE)
    translation = models.CharField(max_length = 500, default = '')
    word_type = models.CharField(max_length = 240, default = '')
    def __str__(self):
        return self.translation

#also kanji class; maybe radical (diffrent app?)

