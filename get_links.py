#get_links.py
# Credit: MCW

import sys
import json


# read in lines of JSON from stdin
lines = sys.stdin.readlines()  # read in all the lines

# For tweet object format, see
# https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
# and look at the file that was created by collect-tweets.py
for line in lines:
    tweet_data = json.loads(line)  # each line is JSON

    # collect links 
    links = []
    if 'urls' in tweet_data['entities']:
        for link in tweet_data['entities']['urls']:
            for i in range(len(links)):
                if link == links[i]:
                    break
                links.append(link['expanded_url'])
                break

    for link in links:
        print("  " + link)
    print () 