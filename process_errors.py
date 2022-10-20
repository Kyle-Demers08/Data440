import sys
import json
import requests
from datetime import datetime

# read in lines of JSON from stdin
lines = sys.stdin.readlines()  # read in all the lines

# For tweet object format, see
# https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
# and look at the file that was created by collect-tweets.py
counter = 0
for line in lines:
    tweet_data = json.loads(line)  # each line is JSON

    # collect links 
    links = []
    if 'urls' in tweet_data['entities']:
        for link in tweet_data['entities']['urls']:
            if 'twitter.com' in link['expanded_url']:
                break
            elif 'youtu.be' in link['expanded_url']:
                break
            elif 'youtube' in link['expanded_url']:
                break
            elif 'twitch.tv' in link['expanded_url']:
                break
            elif 'netflix.com' in link['expanded_url']:
                break
            elif 'soundcloud.com' in link['expanded_url']:
                break
            elif 'musik' in link['expanded_url']:
                break
            else:
                try: # try to get the final link
                    url = requests.get(link['expanded_url'], timeout=5).url
                except requests.exceptions.ReadTimeout: #look for exception
                    break
                except requests.exceptions.ConnectionError:
                    break
                if url in links: #make sure its not already been used
                    break
                else:
                    links.append(url) #append
                    break


    # print information about the tweet
    for link in links:
        print("  " + str(link))
    counter += len(links)
print('the amount of links collected is ' + str(counter))
print ()
                