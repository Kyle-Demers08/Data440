# Homework 4 - Exploring Social Networks
# Kyle Demers
## 11/3/2022

Assignment
You will investigate the friendship paradox on Facebook and Twitter, which says "most people have fewer friends than their friends have, on average."

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

___

### Task 
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

### Q: Does the friendship paradox hold for this user and their friends on Facebook?

*note :* This user has 98 friends

The friendship paradox holds for this user. When looking at the average, of this users friends, they have more friends than this user does. This can be seen in both the graph and the results of the code written above.

### Discussion

The friendship paradox is interesting because the mean is almost always going to be skewed by a few of the "popular" people, or at least the ones who care a lot about their social media presence. This can be seen by the high standard deviation. That is a big part og how this theory works however. You are more likely to be friends with people who have a large amount of friends relative to a small amount of friends. That means that sampling bias occurs as poeple with a lot of friends will likely be sampled. 

---

## Q2. Friendship Paradox on Twitter 
Determine if the friendship paradox holds for your Twitter account. Since Twitter is a directed graph, use followers as the value you measure (i.e., "do your followers have more followers than you?").

If you have less than 50 followers on Twitter, then you can do the analysis for another Twitter account (e.g., my account is acnwala) and substitute the user you pick for you in the questions below.

### Q: What is the mean, standard deviation, and median of the number of followers that your followers have?

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

---

### Q: Does the friendship paradox hold for you and your followers on Twitter?

*Note :* the user has 461 followers

When looking at the mean of this users followers, they average 1429.94 which is more than the followers that this user has. However, when looking at the median, the friendship paradox does not hold. This is due to the upper bound of this users followers being magnitudes larger than the average and therefore skewing the mean upward. 

### Discussion

It is interesting to see the difference in average metrics. The higher end of the spectrum with the most followers has no significant impact on the median, while it plays a huge role in manipulating the mean. The friendship paradox seems like it would almost always hold true for most users. 

---

Link to ipynb where many calculations and graphs were done:
[link](https://github.com/Kyle-Demers08/Data440/blob/main/HW4/Untitled%20(2).ipynb)

Resources:
programiz, <https://www.programiz.com/python-programming/methods/list/sort>
github; using the twitter api, <https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/6b-labs-code-standard-python.md>
github; twitters user object model, <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user>

