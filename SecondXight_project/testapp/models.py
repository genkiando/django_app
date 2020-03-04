from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# class Document(models.Model):
#     # description = models.IntegerField(max_length=255,blank=True)
#     csv_file = models.FileField(upload_to='file/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)


