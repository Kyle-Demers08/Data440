import subprocess
import json
#print(subprocess.Popen('C:\\Users\\kyled\\Downloads')
result = subprocess.run(['.\memgator-windows-386.exe', '--format=json', 'https://alexandernwala.com/'], capture_output=True, text = True)
x = result.stdout
mydict = json.loads(x)
print(mydict['mementos']['first'])
