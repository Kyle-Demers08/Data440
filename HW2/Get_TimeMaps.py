import subprocess
import json
lines = open('tweets_processed.txt', 'r')
lines = lines.readlines()
print(lines)
last_post_date = [] #get date of last post
total_mems = [] #get total URI-Rs
last_post_info = []

with open("timemap.jsonl", "a+") as outfile: #create a place to store timemaps
    for line in lines:
        print(line[2:-2]) #print which url we are on
        url = line[2:-2] #index relevant url
        result = subprocess.run(['.\memgator-windows-386.exe', '--format=json', url], capture_output=True, text = True) #run memgator for each url
        x = result.stdout
        if len(x) > 0: #if memgator returns something
            mydict = json.loads(x) #read as a dictionary
            json.dump(mydict['mementos'],outfile) #store timemap in json
            json.dump('<br>',outfile)
            total_mems.append(len(mydict['mementos']['list'])) #-2 for first and last in the dict
            last_post_date.append(mydict['mementos']['first']['datetime'])
            last_post_info.append(mydict['mementos']['first'])
print(last_post_date)
print(total_mems)
print(last_post_info)

