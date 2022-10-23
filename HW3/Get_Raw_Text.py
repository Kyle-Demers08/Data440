import requests
from boilerpy3 import extractors
lines = open('tweets_processed.txt','r') #file where urls are stored
lines = lines.readlines() #read line for line

for i,url in zip(range(len(lines)),lines): #zip together indecies and urls to iterate together
    url = requests.get(url, timeout=5).url #incase the url has changed in the past 2 weeks
    #url = url[2:] #get everything past the space
    outfile = open('Raw_text2\\rawtext_'+str(i)+'.txt','w') #write to a unique txt file
    try:
        url = requests.get(url) #get content
    except requests.exceptions.ConnectionError: #error handling
        outfile.write('') #0KB 
        continue
    except requests.exceptions.ChunkedEncodingError:
        outfile.write('') #0KB
        continue
    extractor = extractors.ArticleExtractor(raise_on_failure=False)
    content = extractor.get_content(url.text) #get text
    try:#error handling
        outfile.write(content)
    except UnicodeEncodeError:#just use a holder so we can keep links and content in the same place
        outfile.write('')#0 KB

