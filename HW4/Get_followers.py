# get_tweets.py
# Credit: MCW

# More examples at
# https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/6b-labs-code-standard-python.md

from http import client
import sys
import json
from twarc import Twarc2, expansions
from configparser import ConfigParser

# CHANGE THIS TO YOUR TWARC CONFIG
TWARC_CONFIG_FILE = "C:\\Users\\kyled\\AppData\\Roaming\\twarc\\config"
OUTPUT_FILE = "followers.jsonl"   # line-oriented JSON

# read Twitter API keys from twarc config file, setup twarc2 object
config = ConfigParser(interpolation=None)
with open(TWARC_CONFIG_FILE) as twarc_config:
     config.read_string("[TWARC]\n" + twarc_config.read())
bearer_token = config['TWARC']['bearer_token'].strip('\'')
client = Twarc2(bearer_token=bearer_token)
followers_count = []
followers = client.followers(user="acnwala")
followers
for page in followers:
    result = expansions.flatten(page)
    print(result)
    for user in result:
        followers_count.append(json.dumps(user['public_metrics']['followers_count']))
print(followers_count)
