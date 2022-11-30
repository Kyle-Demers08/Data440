from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from datetime import date
import random
import tweepy
import emoji

client = tweepy.Client(consumer_key='a0rC17C7DJb1DaPDnuCnTRI6e',
consumer_secret='BkJbd7weypuOaX2pEGDTYlKZfdYaebKUqQaBX5E0jp8CAbGe7u',
access_token='1567934049842348032-gxJnvXa9wf92thaSJnR8vS1HuPzVCt',
access_token_secret='hf4ajxQyZoVf8BQx5LiEHTDi44nyfHIQ0x0cZGmsghNCv')

date_format = "%m/%d/%Y"
christmas = datetime.strptime('12/25/2022', date_format) #this is christmas the year the script was written
todays_tweets = 0 #initialize a todays tweets variable
#initialize a bunch of good deeds to pick from
xmas_emoji = [':snowflake:', ':snowman:',':bell:']
deeds = ['Pay for someone’s groceries behind you in line.', 'Tell someone you love them.', 'Buy someone flowers.', 'Donate to charity.', 'Take lunch, cookies, or cupcakes to your local fire department and/or police department.',
         'Leave extra time in the parking meter or fill an expired or about to expire parking meter.', 'Leave a nice waiter or waitress a generous tip.', 'Do laundry for a friend.',
         'Put sticky notes with positive messages in public places.', 'Hand out gloves and mittens to the homeless, or leave them on park benches.', 'Sing an employee’s praises to a manager or on a comment card — a little recognition goes a long way.',
         'Help someone load their groceries.','Offer to return someone’s shopping cart to the store.','Let someone go ahead of you in the checkout line.','Leave a favorite book in a public place with a note that’s it’s free for the taking.'
         'Put a comment on someone’s webpage that you really like……let them know you enjoy it.', 'Write thank you notes to people who go all out to decorate their yard and house with lights. Thank them for lighting up the neighborhood.',
         'Volunteer to help someone wrap gifts.', 'Do yard work or shovel snow for a neighbor', 'Leave birdfood out for our flying friends! Maybe even make a bird feeder.', 'Clean someone elses space.', 'Spend quality time with someone.',
         'Donate some books.', 'Send someone a card.', 'Clean your room.', 'Compliment someone!', 'Donate some clothes.', 'Say something nice online.', 'Call your parents.', 'Double your tip.', 'Donate a toy.', 'Clean a road or park.', 'Make some cookies for others.',
         'Help a sibling to a chore or other job.', 'Leave a little treat in the mailbox for the mailman.', 'Donate blood.', 'Smile at someone.', 'Pick up litter.', 'Hold the door for someone.', 'Leave quarters on a snack/laundry machine.', 'Let someone ahead of you in line.']
def tweet():
    global christmas #change these variables in the global space
    global todays_tweets 
    todays_tweets += 1 
    today = datetime.today()
    diff = christmas - today
    diff = diff.days + 1 # add one since the difference is off
    if diff == 1:
        tweet = 'Its Christmas Eve! Todays the last day Santa will judge you for this year! A good deed for today would be: ' + random.choices(deeds) + emoji.emojize(random.choice(xmas_emoji))
    elif diff == 0:
        tweet = 'Merry Christmas! Enjoy today, you deserve it! Spend time with your loved ones.' + emoji.emojize("bell")
        if todays_tweets == 2:
            christmas.year + 1
            newdate = '12/25/' + str(christmas.year +1)
            christmas = datetime.strptime(newdate, date_format)
            tweet = 'I hope Santa delivered beyond everybodys hopes and dreams!' + emoji.emojize('snowman')
    else:
        if todays_tweets == 1: #need to seperate tweets to avoid duplicating tweets error
            tweet = "We're " + str(diff) + ' days away from Christmas! A good deed for today would be: ' + random.choice(deeds) + emoji.emojize(random.choice(xmas_emoji))
        else: 
            tweet = "We're still " + str(diff) + ' days away from Christmas! If you did not like this last deed or want another one you can do this: ' + random.choice(deeds) + emoji.emojize(random.choice(xmas_emoji))
    if todays_tweets == 2:
        todays_tweets = 0
    response = client.create_tweet(text=tweet)
    #print(response)
    print(tweet)
scheduler = BlockingScheduler()
scheduler.add_job(tweet, 'interval', hours=12)
scheduler.start()
#note this bot would eventually break if the same dead was selected the same tweet next year, I would do more error handling for that
#next steps would be to add more tweets