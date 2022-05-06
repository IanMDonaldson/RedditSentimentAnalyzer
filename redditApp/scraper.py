from psaw import PushshiftAPI
import datetime as datetime
import mysql.connector

# need to get ticker names and company names from DB
# then for each of the ticker + company name
#   could either
#   1. search with psaw for each of the ticker name+company name
#   maybe use psaw to search
# submissions = list of 1000 submissions
#
#
#

api = PushshiftAPI()
startTime = int(datetime.datetime(2022,2,20).timestamp())

submissions = list(api.search_submissions( after=startTime,
                    subreddit='wallstreetbets',
                    filter=['title','id','created_utc']
                    ))
print(submissions[-1].timeCreated)
for submission in submissions:
    print(submission.title)

    # words = submission.title.split()
    # cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))
    #
    # if len(cashtags) > 0:
    #     print(cashtags)
    #     print(submission.title)
