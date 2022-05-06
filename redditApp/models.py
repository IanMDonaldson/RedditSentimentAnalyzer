from django.db import models
# type in reddit.com/ID36
# first is data>children>data>selftext = post content
# comments are data>children>body = comment content
# if replies it goes replies>data>children>data
# date is created_utc, a unix timestamp in UTC timezone
# Create your models here.
class Submission(models.Model):
    class Meta:
        db_table = 'Submission'
    commentID = models.CharField(primary_key=True, max_length=6)
    parentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    tickerID = models.ForeignKey('Ticker', on_delete=models.PROTECT)
    timeCreated = models.DateTimeField()
    postbody = models.TextField(max_length=2000)


    def __str__(self):
        return self.commentID+self.parentID+self.tickerID+self.postbody+self.timeCreated

class Ticker(models.Model):
    class Meta:
        db_table = 'Ticker'
    tickerID = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=6)
    companyName = models.CharField(max_length=155)

    def __str__(self):
        return self.tickerID+self.symbol+self.companyName

class Sentiment(models.Model):
    class Meta:
        db_table = 'Sentiment'
    sentimentID = models.AutoField(primary_key=True)
    commentID = models.ForeignKey('Submission', on_delete=models.CASCADE)
    tickerID = models.ForeignKey('Ticker', on_delete=models.DO_NOTHING)
    sentimentScore = models.DecimalField(decimal_places=4, max_digits=6);

    def __str__(self):
        return self.sentimentID+self.commentID+self.tickerID+self.sentimentScore
