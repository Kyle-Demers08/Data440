# HW#2 - Archiving the web
### Kyle Demers
### Data 440, Fall 2022
### 10/19/2022

# Q1

Q1. Collect URIs from Tweets (2 points)
Extract 1000 unique links from tweets in Twitte

Main steps:

Write a Python program that collects English-language tweets that contain links. See Collecting Tweets.
Write a Python program that extracts the links shared in tweets. See Extracting Links from Tweets.
Resolve all URIs to their final target URI (i.e., the one that responds with a 200). See Resolve URIs to Final Target URI.
Save only unique final URIs (no repeats). See Save Only Unique URIs.
if after this step, you don't have 1000 unique URIs, go back and gather more until you are able to get at least 1000 unique URIs
Save this collection of 1000 unique links in a file and upload it to your repo in GitHub -- we'll use it again in HW3

## Answer

Python Script: [python Script](https://github.com/Kyle-Demers08/Data440/blob/main/HW2/process_errors.py)

Text file of URL's: [1000 Url's](https://github.com/Kyle-Demers08/Data440/blob/main/HW2/tweets_processed.txt)

## Discussion 

For the python script to get links I had to blacklist a lot of sites as they were video sites, sites not meant for archiving, or sites that caused errors. I also had to do some error handling for anything that broke code. From there I had to make sure the link wasn't already in my list containing all my links to prevent duplicates for problem 2. 

# Q2 Get TimeMaps for Each URI (2 points)

Obtain the TimeMaps for each of the unique URIs from Q1 using the ODU Memento Aggregator, MemGator.

You may use https://memgator.cs.odu.edu for limited testing, but do not request all of your 1000 TimeMaps from memgator.cs.odu.edu.

## Answer

python script: [get timemaps script](https://github.com/Kyle-Demers08/Data440/blob/ok/Get_TimeMaps.py)
timemaps jsonl: [timemaps](https://github.com/Kyle-Demers08/Data440/blob/ok/timemap.jsonl)


## Discussion

In the python script to get relevant information, I had to open up the text file of links and create a jsonl file to store the timemaps. I then had to slice the inde to get rid of white spaces. From there I was able to run memgator and obtain the TimeMaps. I had to do check if anything was returned to prevent my script from crashing. I could then read the json output of memgator to a dictionary and store and obtain the relevant information.
 

# Q3 Analyze Mementos Per URI-R. (2 points)

Use the TimeMaps you saved in Q2 to analyze how well the URIs you collected in Q1 are archived. Create a table showing how many URI-Rs have certain number of mementos. For example



## Answer


| **Mementos** | **URI-R's** |
|--------------|-------------|
|     0        |     756     |
|    1-9       |     171     |
|    10-19     |      15     |
|    20-29     |       6     |
|    30-39     |       7     |
|    40-49     |       4     |
|    50-59     |       2     |
|    60-69     |       4     |
|    70-79     |       2     |
|    80-89     |       1     |
|    90-99     |       2     |
|   100-200    |       6     |
|   200-500    |      11     |
|   500-1000   |       1     |
|  1000-10000  |       6     |
| 10000-100000 |       3     |
|   100000+    |       4     |

### Q: What URI-Rs had the most mementos? Did that surprise you?

### Answer: 

A website from Iowa State studying environmental data. This is definitely not what I guessed as it is a bit obscure, but it doesn't surprise me. I thought if I had a link to something like cnn, that would have the most, but I didn't have any of those links. The Website seems like it has been in use for a while tracking data. It also makes sense to have a lot of mementos as it is collecting data from the ever changing environment, and therefore the website is changing a lot.

## Discussion

In the python script for extracting TimeMaps, I created a list to append the amount of mementos for each URI-R. This made it easy as from here all I had to do was count how many URI-R's fit in each bin of mementos. While it is not standard to have variable bin widths, it was necessary to keep the number of bins under 20. 

# Q4 Analyze Datetimes of Mementos. (2 points)

For each of the URI-Rs from Q3 that had > 0 mementos, create a scatterplot with the age of each URI-R (today - earliest memento datetime) on the x-axis and number of mementos for that URI-R on the y-axis. Some Info Vis terminology: for this graph, the item is the URI-R and the attributes are the estimated age of the URI-R (channel is horizontal position) and the number of mementos for that URI-R (channel is vertical position).


## Answer

<img width="452" alt="image" src="https://user-images.githubusercontent.com/112887807/196829969-d248c697-86cf-4c60-b12e-9e368b665d75.png">

ipynb script for answering questions and creating graph: [Script](https://github.com/Kyle-Demers08/Data440/blob/main/HW2/plot.ipynb)

### Q: What can you say about the relationship between the age of a URI-R and the number of its mementos?
### Answer:
As the age of the URI-R increases, there tend to be more mementos. There is a concentration around new URI-R's and low mementos of course with a few outliers. When the age increases, there are very few URI-R's with few mementos, and they tend to have more mementos.

### Q: What URI-R had the oldest memento? Did that surprise you?
### Answer: 
The oldest memento is from a news source from new jersey, nj.com. This doesn't surprise me at all as I expected most of the older mementos to be from news sources.

### Q: How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?
### Answer:
137 of my URI-R's had an age of less than 1 week. 

## Discussion

For the graph I had to use log scale to be able to see the amount of URI-Rs as there were some extreme numbers over the 100,000 mark. It is cool to see the relationship truly develop and be visualized in the plot. 

# References

* Programiz, <https://www.programiz.com/python-programming/methods/list/index>
* Stack Overflow, <https://stackoverflow.com/questions/8258432/days-between-two-dates>
* Stack Overflow, <https://stackoverflow.com/questions/17594298/date-time-formats-in-python>
* geeks for geeks, <https://www.geeksforgeeks.org/append-to-json-file-using-python/>
* Stack Overflow, <https://stackoverflow.com/questions/41171791/how-to-suppress-or-capture-the-output-of-subprocess-run>
* Stack Overflow, <https://stackoverflow.com/questions/41265249/export-subprocess-output-result-in-dictionary-or-list>
* Geeks for Geeks, <https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/>
* Geeks for Geeks, <https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/>
* Python Tutorial, <https://www.pythontutorial.net/python-basics/python-read-text-file/>
