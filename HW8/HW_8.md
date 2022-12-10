# Kyle Demers
## Homework 8 - Clustering
Due: Thursday, December 8, 2022 by 11:59pm Read through the entire assignment before starting. Do not wait until the last minute to start working on it.

### Assignment:
The goal of this assignment is to cluster Twitter accounts based on the content of their last 200 tweets.

### Q1: Find Popular Twitter Accounts
Generate a list of 100 popular accounts on Twitter. The accounts must be verified, have 10,000+ followers, and have 5000+ tweets. 

You may also generate this information manually by visiting individual account pages. You only need 100 popular accounts, so manual selection might be justified.

Because we're trying to cluster the accounts based on the text in their tweets, you should choose several sets of accounts that are similar (political, tech, sports, etc.) to see if they'll get clustered together later.

Save the list of accounts (screen_names), one per line, in a text file named accounts.txt and upload to your GitHub repo.

#### A: How did you choose to collect the accounts?

I choose to manually collect my accounts. I was able to look at the following of most of the leaders of the groups and get a list from there.
There is also a see also page which allowed me to get other accounts if the following list ran dry.

#### B: What topics/categories do the accounts belong to? Provide a this list before generating your clusters.

The first category is teams in English soccer. 
The next category I chose was politicians. I got politicians from both parties, it would be interesting to see if the algorithms can differentiate them although I doubt it will
The last category is general business. I want to see if this can be differentiated from the English soccer accounts which it likely will. I wonder if small subgroups will form in this category like tech or consulting.

### Discussion:

I think this combination of topics will be interesting. For soccer I grabbed teams from two different leagues. I wonder if the algorithm will be able to differentiate them using words like "Championship" or "Premier" and "League". I also wonder if Barclays the bank will be mixed with the soccer topics as they are the title sponsor of the epl. The mix of political candidates could be interesting either by senate and house or by party. I don't follow politics to well so it will be tough for me to tell. With business I wonder if the banks will split from other firms.
The accounts I pulled are [here](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/accounts.txt)

---

### Q2 - Create Account-Term Matrix (3 points)
Before we can run the clustering code from the PCI book, we have to build an account-term matrix (like the blog-term matrix in the Module 12 slides). Consider the Twitter accounts equivalent to blogs, and all account tweets, the words of the blog.

The PCI book provided code for creating the blog-term matrix given a list of blog feeds. I've provided similar code written by Dr. Michele Weigle's:

instead of creating an account-term matrix for every term in the tweets, I only want the 500 most popular terms that are not stopwords. You will need to write this code. To help with this, I've added a sumcounts dict that holds the words and frequency of those words over all accounts and a blank list popularlist where you should store the 500 most frequent non-stopword terms. On line 88, you'll see a section labeled # BEGIN YOUR CODE BLOCK. This is where you'll add your code.
Once complete, generate_tweet_vector.py will produce two files that you need to upload to your GitHub repo:

[popular_terms.txt](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/popular_terms.txt) - the list (one per line) of the 500 most frequent terms in the tweets
[tweet_term_matrix.txt](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/tweet_term_matrix.txt) - the generated account-term matrix
Once [tweet_term_matrix.txt](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/tweet_term_matrix.txt) has been generated, you can use it in place of blogdata.txt in the example code to complete the remaining parts of this assignment.

#### A: Explain the general operation of generate_tweet_vector.py and how the tweets are converted to the account-term matrix.

Generate_tweet_vector.py creates both the [term matrix](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/tweet_term_matrix.txt and the [popular terms](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/popular_terms.txt) files. It does this by grabbing the last 100 tweets from the accounts in accounts.txt and counting up each of the words. Those words get put into features of the term matrix and the counts are for each account. After going through each account, you would be able to see how many times in the past 100 tweets each account said each word. 

#### B: Explain in detail the code that you added to filter for the 500 most frequent non-stopword terms.

```python
newcounts = {} #this will hold the counts for non stopwords
for k in sumcounts:
    if k in wordlist:
        newcounts[k] = sumcounts[k] #gets word and counts if it is in the wordlist, puts it into a new dictionary
popularlist = nlargest(500, newcounts,key = newcounts.get)
```

My code looks to grab words that aren't stop words. We use wordlist as this is the list of words that aren't stopwords. If the word is in sumcount then the dictionary of newcounts appends the key(being the word) and its value attached to the words sumcounts. That means the newcounts dictionary has the key paired with it sum if the key is not a stopword. We then use nlargest to grab the 500 largest counts.

#### C: Do the 500 most frequent terms make sense based on the accounts that you chose?

The 500 most frequent terms make a lot of sense. The most frequent word is learn, likely because it used by business politics and sometimes sports. Then it is Biden which is of course a common political word. There are also words like global, inflation, worldcup, and win which all make sense and seem relevant to my topics. 

---

Q3 - Create Dendrogram (1 point)
Create an ASCII dendrogram and a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see Module 12, slides 21, 23). Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

<img width="278" alt="image" src="https://user-images.githubusercontent.com/112887807/206788661-b7cc7f84-2170-46f2-91f3-e4db1ff0b4fc.png">

[JPEG](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/clusters.jpg)

[ASCII](https://github.com/Kyle-Demers08/Data440/blob/main/HW8/ascii2.txt)

#### A: How well did the hierarchical clustering do in grouping similar accounts together? Were there any particularly odd groupings?

The clustering did a pretty good job at grouping things together. It did well at getting all the soccer teams together. Theres also a small subcategory of teams in the championship as opposed to the premier league although it didn't get them all. The business' are also connected with some banks being clustered into small subgroups. The politicians are all grouped together with a few seemingly small subgroups. 

#### Discussion

My ASCII diagram doesn't look like how I wanted it to. There isn't any indentation and without access to the code and seeing how it was made, it is hard to interpret.

---

#### Q4 - Cluster using k-Means (2 points)

Cluster the accounts using k-Means, using k=5,10,20 (see Module 12, slide 34). For each value of k, create a file that lists the accounts in each cluster and upload to your GitHub repo.

#### A: Give a brief explanation of how the k-Means algorithm operates on this data. What features is the algorithm considering?

The k-means algorithm takes clusters by the closest k data points. The closesness is determined by how alike the features values are which in this case is how often each words are said. Those that use similar words more often will likely be similar accounts and then be clustered together.

#### B: How many iterations were required for each value of k?

When K was 5 there were 4 iterations
When K was 10 there were 6 iterations
When K was 20 there were also 6 iterations

The number of iterations will not always be the same as no random state is specified. 

#### C: Which k value created the most reasonable clusters? For that grouping, characterize the accounts that were clustered into each group.

the k = 5 produced the best clusters. There was a group of clusters for soccer teams, 2 groups for business and 2 groups for politics. All of the soccer teams were correctly classified. Some of the more business focused politicians were mixed with the business accounts. As k went up, more clusters were made, and these clusters didn't have a clear reason as to why they were different from each other. With k = 5 the differentiation was clear.
