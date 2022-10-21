import subprocess
import json
lines = open('tweets_processed.txt', 'r') #read in txt file
lines = lines.readlines()#get lines
print(lines)

for i,line in zip(range(len(lines)),lines):
    outfile = open('timemaps\\timemap_'+str(i)+'.jsonl','w')
    print(line[2:-2]) # print which url we are on to make sure it is running
    url = line[2:-2]  # index relevant url
    result = subprocess.run(['.\memgator-windows-386.exe', '--format=json', url], capture_output=True, text = True) #run memgator for each url
    x = result.stdout
    if len(x) > 0: #if memgator returns something
        mydict = json.loads(x) #read as a dictionary
        json.dump(mydict,outfile) #store timemap in jsonl file
        