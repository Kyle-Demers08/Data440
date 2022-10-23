# HW#3 - Ranking Webpages
### Kyle Demers
### Data 440, Fall 2022
### 10/21/2022

--- 

# Q1. Data Collection 

Download the HTML content of the 1000 unique URIs you gathered in HW2 and strip out HTML tags (called "boilerplate") so that you are left with the main text content of each webpage.

**Removing HTML Boilerplate**

Now use a tool to remove (most) of the HTML markup from your 1000 HTML documents.

The Python boilerpy3 library will do a fair job at this task. You can use pip to install this Python package. The main boilerpy3 webpage has several examples of its usage.

Keep both files for each URI (i.e., raw HTML and processed), and upload both sets of files to your GitHub repo. Put the raw and processed files in separate folders.


## Answer:

Python script to get text: [Get text](https://github.com/Kyle-Demers08/Data440/blob/main/HW3/Get_Raw_Text.py)

The URI's I am using: [Text file of URI's](https://github.com/Kyle-Demers08/Data440/blob/main/HW2/tweets_processed.txt)

Raw text files: [Zip Folder Containing text for each url](https://github.com/Kyle-Demers08/Data440/blob/main/HW3/Raw_text.zip)

#### Q: How many of your 1000 URIs produced useful text? If that number was less than 1000, did that surprise you?

#### Answer:
of the 1016 urls, my code was able to process 994 of them. 350 of those 994 resulted in 0 KB meaning boilerpy3 couldn't extract any content as it produces no output. This means that 644 produced useful text. This is pretty suprising to me as I didn't think I would have that many textless files. Maybe there were links that led to just images that I wasn't able to filter out when I originally got the list or urls. 

## Discussion: 
For this I was able to use the URI's I gathered from HW#2. I did notice that since they were collected two weeks ago, some pages were likely deleted or moved as the text that was being returned from boilerpy was me getting Errors in the 400's. Some links also were raising errors for boilerpy so that information couldn't be written to a txt file leaving me with slightly under 1000 txt files.

---

# Q2. Rank with TF-IDF

Choose a query term (e.g., "coronavirus") that is not a stop word (e.g., "the"), or super-general (e.g., "web"), or in HTML markup (e.g., "http") that is found in at least 10 of your documents. If the term is present in more than 10 documents, choose any 10 English-language documents from different domains from the result set.

## Answer:

For this question I chose to run a query on the term "soccer". This should return many different topics from my initial searches as I looked for tweets containing "liverpool" and "soccer" and certain geographical locations. 

The query I ran was using the findstr command in windows powershell:

[Find Strings](https://github.com/Kyle-Demers08/Data440/blob/main/HW3/findstr.png)
Text Files containing the string "Soccer" and their Frequencies in parenthesis:
 - 691 (1)
 - 734 (3)
 - 735 (3)
 - 736 (8)
 - 737 (8)
 - 739 (4)
 - 741 (4)
 - 746 (1)
 - 751 (2)
 - 753 (6)
 - 754 (1)
 - 756 (1)
 - 762 (3)
 - 763 (7)
 - 768 (7)
 - 770 (1)
 - 772 (12)
 - 774 (3)
 - 775 (3)
 - 776 (1)
 - 777 (3)
 - 78 (8)
 - 79 (8)
 - 844 (3)
 - 86 (6)
 - 93 (8)
 - 985 (1)

The 10 I am picking from this list are the following: 985, 93, 86, 844, 78, 772, 735, 777, 754, 739

When searching soccer on google; 1,770,000,000 results were returned out of googles 35 billion corpus size

[Google Search](https://github.com/Kyle-Demers08/Data440/blob/main/HW3/soccer.png)
 
The IDF in this case is log<sub>2</sub>(35B/1.77B) which equals 4.303

To get the TF of the URI we need the wordcount so I used the cat powershell command to measure word count:

[Using Cat](https://github.com/Kyle-Demers08/Data440/blob/main/HW3/wordcount.png))


| TF-IDF |  TF  |  IDF  |   URI   |
|--------|------|-------|---------|
| 0.0585   |  0.0136  | 4.303 |   https://www.nj.com/highschoolsports/2022/10/who-are-the-top-sophomore-boys-soccer-players-in-the-state-let-us-know.html?utm_source=twitter&utm_medium=social&utm_campaign=hssportsnj_sf&utm_content=nj_twitter_hssportsnj |
|  0.0476 | 0.0111 | 4.303 | https://www.oregonlive.com/portland-thorns/2022/10/bill-oram-oregon-youth-soccer-prepares-effort-to-end-relationship-with-portland-timbers-and-thorns.html |
|  0.0342  | 0.0080 | 4.303 |   https://www.kait8.com/2022/10/10/a-state-soccers-win-streak-snapped-ulm/ |
|  0.0250  | 0.0058 | 4.303 |  https://newsworldpress.com/business/girlss-soccer-is-booming-in-england-however-the-large-cash-hasnt-caught-up-but-3.html |
|  0.0246  | 0.0057  | 4.303 |   https://newsworldpress.com/world-news/ladiess-soccer-is-booming-in-england-however-the-massive-cash-hasnt-caught-up-but.html |
|  0.0192  | 0.0045  | 4.303 |   https://www.dailymail.co.uk/health/article-11294523/Shocking-scenes-uncovered-inside-Britains-mental-health-service-crisis.html |
|  0.0151 | 0.0035  | 4.303 |     https://www.swimmingscience.net/is-chocolate-milk-an-adequate-recovery-aid-for-swimmers/?utm_source=ReviveOldPost&utm_medium=social&utm_campaign=ReviveOldPost |
|  0.0099 |  0.0023  | 4.303 |   https://ravallirepublic.com/sports/college/big-sky-conference/university-of-montana/montana-soccer-team-holds-off-northern-colorado/article_a6183f82-7072-577e-a841-d35440731d4e.html?utm_campaign=snd-autopilot&utm_medium=social&utm_source=twitter_RavalliRepublic |
|  0.0082  | 0.0019  | 4.303 |   https://www.ebay.com/itm/2018-NATIONAL-TREASURES-SOCCER-PELE-RIVALDO-DUAL-AUTO-GOLD-2-10-SSP-RARE-BRAZIL-/325367418451?mkcid=1&mkrid=711-53200-19255-0&toolid=20023&campid=5338914201&customid=100922&siteid=0&mkevt=1 |
|  0.0039  |  0.0009    |  4.303    |   https://newscharotar.com/streaming-in-canada-on-amazon-prime-video-apple-tv-crave-disney-and-netflix-oct-3-9/ |


## Discussion:

To calculate the TF I used the information out of the cat function to get the total wordcount in the text file and I used the findstr to get the specific word "soccer". I then divided the output of the findstr command by the cat command giving me Times Soccer appeared divided by total words. 
To calculate the IDF, I did a google search of the term "soccer". this resulted in 1.77 Billion results out of googles corpus size of 35 billion. I then did  log<sub>2</sub>(35B/1.77B) = 4.303. This number is constan regardless of the textfile so that number is the same throughout the table
Since I was using a one word query, to get the TF-IDF, all I needed to do was multiply the one TF and the one IDF. 

---
 
# References

* Boilerpy3, <https://pypi.org/project/boilerpy3/>
* W3schools, <https://www.w3schools.com/python/python_try_except.asp>
* geeks for geeks, <https://www.geeksforgeeks.org/python-append-to-a-file/?id=discuss>
* Stack Overflow, <https://stackoverflow.com/questions/59685819/count-the-number-of-characters-words-and-lines-in-powershell>
* Window Tools, <http://winteltools.com/findstr/>

