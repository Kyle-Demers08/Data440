# Kyle Demers
## Homework 8 - Clustering
Due: Thursday, December 8, 2022 by 11:59pm Read through the entire assignment before starting. Do not wait until the last minute to start working on it.

### Assignment:
The goal of this assignment is to cluster Twitter accounts based on the content of their last 200 tweets.

### Q1: Find Popular Twitter Accounts
Generate a list of 100 popular accounts on Twitter. The accounts must be verified, have 10,000+ followers, and have 5000+ tweets. For example:

You may also generate this information manually by visiting individual account pages. You only need 100 popular accounts, so manual selection might be justified.

Because we're trying to cluster the accounts based on the text in their tweets, you should choose several sets of accounts that are similar (political, tech, sports, etc.) to see if they'll get clustered together later.

Save the list of accounts (screen_names), one per line, in a text file named accounts.txt and upload to your GitHub repo.

### A: 
How did you choose to collect the accounts?

### Response: 

I choose to manually collect my accounts. I was able to look at the following of most of the leaders of the groups and get a list from there.
There is also a see also page which allowed me to get other accounts if the following list ran dry.

### B: 
What topics/categories do the accounts belong to? You don't need to specify a grouping for each account, but what general topics/categories will you expect to be revealed by the clustering? Provide a this list before generating your clusters

### Response:

The first category is teams in English soccer. 
The next category I chose was politicians. I got politicians from both parties, it would be interesting to see if the algorithms can differentiate them although I doubt it will
The last category is general business. I want to see if this can be differentiated from the English soccer accounts which it likely will. I wonder if small subgroups will form in this category like tech or consulting.

Q2 - Create Account-Term Matrix (3 points)
Before we can run the clustering code from the PCI book, we have to build an account-term matrix (like the blog-term matrix in the Module 12 slides). Consider the Twitter accounts equivalent to blogs, and all account tweets, the words of the blog.

The PCI book provided code for creating the blog-term matrix given a list of blog feeds. I've provided similar code written by Dr. Michele Weigle's:

tweet_parser.py - This is similar to the feedparser library mentioned on pg. 31. It contains two functions used by generate_tweet_vector.py:

setup_api(filename) - set up and return a Twitter API object, filename is the file containing your API keys
parse(api, screen_name, num_tweets=100) - use Twarc2 to download about 100 tweets (excluding replies and retweets) from the timeline of the screen_name account and return a dictionary with the following structure:
{'screen_name': screen_name, 'tweets': [tweet1, tweet2, ...]}
generate_tweet_vector.py - This is similar to generatefeedvector.py described on pgs. 31-33 in PCI. It contains main code and two functions:

getwordcounts(api, screen_name) - calls parse() from tweet_parser.py and returns the screen_name and a dictionary of word counts appearing in that account's tweets, almost exactly like getwordcounts() in our examples
getwords(tweet) - takes a tweet and returns a filtered list of words, similar to getwords() in our examples, but with some added filtering:
removes URLs
removes screen names (starting with @)
splits words by non-alphabetic characters (and thus removes any numbers and symbols)
removes any words < 3 characters or > 15 characters
lowercases all words
generate_tweet_vector.py requires that you have accounts.txt (from Q1) and tweet_parser.py located in the same folder.

generate_tweet_vector.py will not work out-of-the-box.

First, on line 51, you'll need to insert the path to your Twarc config file.
Second, instead of creating an account-term matrix for every term in the tweets, I only want the 500 most popular terms that are not stopwords. You will need to write this code. To help with this, I've added a sumcounts dict that holds the words and frequency of those words over all accounts and a blank list popularlist where you should store the 500 most frequent non-stopword terms. On line 88, you'll see a section labeled # BEGIN YOUR CODE BLOCK. This is where you'll add your code.
Once complete, generate_tweet_vector.py will produce two files that you need to upload to your GitHub repo:

popular_terms.txt - the list (one per line) of the 500 most frequent terms in the tweets
tweet_term_matrix.txt - the generated account-term matrix
Once tweet_term_matrix.txt has been generated, you can use it in place of blogdata.txt in the example code to complete the remaining parts of this assignment.

A: Explain the general operation of generate_tweet_vector.py and how the tweets are converted to the account-term matrix.

B: Explain in detail the code that you added to filter for the 500 most frequent non-stopword terms.

C: Do the 500 most frequent terms make sense based on the accounts that you chose?

Q3 - Create Dendrogram (1 point)
Create an ASCII dendrogram and a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see Module 12, slides 21, 23). Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

A: How well did the hierarchical clustering do in grouping similar accounts together? Were there any particularly odd groupings?

Q4 - Cluster using k-Means (2 points)
Cluster the accounts using k-Means, using k=5,10,20 (see Module 12, slide 34). For each value of k, create a file that lists the accounts in each cluster and upload to your GitHub repo.

A: Give a brief explanation of how the k-Means algorithm operates on this data. What features is the algorithm considering?

B: How many iterations were required for each value of k?

C: Which k value created the most reasonable clusters? For that grouping, characterize the accounts that were clustered into each group.
