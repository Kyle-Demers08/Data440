# Homework 4 - Exploring Social Networks
# Kyle Demers
## 11/1/2022
Due: Thursday, November 3, 2022 by 11:59pm

Assignment
You will investigate the friendship paradox on Facebook and Twitter, which says "most people have fewer friends than their friends have, on average."

(Report (2 points)

## Q1. Friendship Paradox on Facebook (4 points)
Determine if the friendship paradox holds for a user's Facebook account. (This used to be more interesting when you could more easily download your friend's friends list from Facebook. Facebook now requires each friend to approve this operation, effectively making it impossible.)

acnwala_friends_friends_count.csv (provided on Piazza) contains a user's friends' names and number of friends they each have.

(acnwala friend csv)[https://github.com/Kyle-Demers08/Data440/blob/main/HW4/acnwala_friends_friends_count.csv]

Q: What is the mean, standard deviation, and median of the number of friends that the user's friends have?

Create a graph of the number of friends (y-axis) and the friends themselves (x-axis), sorted by number of friends. The friends don't need to be labeled on the x-axis: 1, 2, 3,..., n should be sufficient. Include the user in the graph in the appropriate sorted position (count the number of their friends) and label as U.

Q: Does the friendship paradox hold for this user and their friends on Facebook?

Q2. Friendship Paradox on Twitter (4 points)
Determine if the friendship paradox holds for your Twitter account. Since Twitter is a directed graph, use followers as the value you measure (i.e., "do your followers have more followers than you?").

If you have less than 50 followers on Twitter, then you can do the analysis for another Twitter account (e.g., my account is acnwala) and substitute the user you pick for you in the questions below.

Q: What is the mean, standard deviation, and median of the number of followers that your followers have?

Q: Does the friendship paradox hold for you and your followers on Twitter?

You may use Twarc2 in Python to access the Twitter API to find a user's followers. The code to access the Twitter API should be similar to get_tweets.py, you may use that to start.

Other helpful references:

Labs for the Standard Product Track in Python - look at the section headings to find the appropriate part to read
Twitter's User object model - explains the data structure returned from the Twitter API
process-tweets.py - shows examples of accessing different parts of the data structure returned from the Twitter API
Submission
Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the hw4 folder). Your repo should include your report, images, code, and data you developed to answer the questions. Include "Ready to grade @anwala" in your final commit message.
