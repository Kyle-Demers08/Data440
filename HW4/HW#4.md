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

[acnwala friend csv](https://github.com/Kyle-Demers08/Data440/blob/main/HW4/acnwala_friends_friends_count.csv)

### Q: What is the mean, standard deviation, and median of the number of friends that the user's friends have?

### Answer:

```python
print('the mean followers of your friends followers: ' + str("{:.2f}".format(np.mean(df['counts']))))
```

The mean followers of anwala is 542.67

```python
print('the standard deviation of your friends followers: ' + str("{:.2f}".format(np.std(df['counts']))))
```
The standard deviation of anwala's followers is 536.67


```python
print('the median of your friends followers: ' + str("{:.2f}".format(np.median(df['counts']))))``` 
```

the median of anwala's followers is 396

---

Create a graph of the number of friends (y-axis) and the friends themselves (x-axis), sorted by number of friends. The friends don't need to be labeled on the x-axis: 1, 2, 3,..., n should be sufficient. Include the user in the graph in the appropriate sorted position (count the number of their friends) and label as U.

```python
fig, ax = plt.subplots(figsize = (9,6 ))
ax.scatter(x,df['counts'], alpha=0.5, edgecolors="k") #plot with .5 transparency
# label axes
ax.set_ylabel("Followers")
ax.set_xlabel('Person (sorted high to low)')
#remove weird tick marks
ax.set_yticks([],minor = True)
#plot user point
plt.plot(88.5, 98, marker = 'o', c = 'red')
#label 
plt.annotate('U',[88,170])
plt.show()
```
<img width="450" alt="image" src="https://user-images.githubusercontent.com/112887807/199545161-5b7d26bc-88c7-47c4-8a0e-40570b06bf9d.png">

Q: Does the friendship paradox hold for this user and their friends on Facebook?

*note* : This user has 98 friends

The friendship paradox holds for this user. When looking at the average, of this users friends, they have more friends than this user does. This can be seen in both the graph and the results of the code written above.

Q2. Friendship Paradox on Twitter (4 points)
Determine if the friendship paradox holds for your Twitter account. Since Twitter is a directed graph, use followers as the value you measure (i.e., "do your followers have more followers than you?").

If you have less than 50 followers on Twitter, then you can do the analysis for another Twitter account (e.g., my account is acnwala) and substitute the user you pick for you in the questions below.

Q: What is the mean, standard deviation, and median of the number of followers that your followers have?

Since I do not have a twitter account, I am using user acnwala.

In order to find this information, I used the following python script to get the data of his twitter followers and append the relevant information to a list. From there I could simply copy and paste that list back into my jupyter notebook and use the data there.

[getting followers python script](https://github.com/Kyle-Demers08/Data440/blob/main/HW4/Get_followers.py)

```python
print('the mean followers of your friends followers: ' + str("{:.2f}".format(np.mean(follower_counts))))
```

the mean followers of your friends followers: 1429.94

```python
print('the standard deviation of your friends followers: ' + str("{:.2f}".format(np.std(follower_counts))))
```

the standard deviation of your friends followers: 4722.65

```python
print('the median of your friends followers: ' + str("{:.2f}".format(np.median(follower_counts))))
```

the median of your friends followers: 256.00

Q: Does the friendship paradox hold for you and your followers on Twitter?

You may use Twarc2 in Python to access the Twitter API to find a user's followers. The code to access the Twitter API should be similar to get_tweets.py, you may use that to start.

Other helpful references:

Labs for the Standard Product Track in Python - look at the section headings to find the appropriate part to read
Twitter's User object model - explains the data structure returned from the Twitter API
process-tweets.py - shows examples of accessing different parts of the data structure returned from the Twitter API
Submission
Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the hw4 folder). Your repo should include your report, images, code, and data you developed to answer the questions. Include "Ready to grade @anwala" in your final commit message.
