import urllib
import re
import urllib2
import os

res = os.listdir(".")

stuff = urllib2.urlopen('http://pianosociety.com/all.html').read()  # stuff will contain the *entire* page
results = re.findall('(http.*mp3)',stuff)
counter = 1
leng = len(results)
for item in results:
    print(str(counter)+ "/"+str(leng))
    if(item.split('/')[4] in res):
        print("Already there")
    else:
        print item
        urllib.urlretrieve (item, item.split('/')[4])
    counter = counter + 1
