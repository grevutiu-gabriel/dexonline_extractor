from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import sys, os
hostname = str(sys.argv[1])
outgroup=open(hostname, 'wt')
url="http://dexonline.ro/lista-cuvinte/"+hostname
url = urllib.parse.urlsplit(url)
url = list(url)
url[2] = urllib.parse.quote(url[2])
url = urllib.parse.urlunsplit(url)
url = urllib.request.urlopen(url)
content = url.read()
soup = BeautifulSoup(content)
for a in soup.findAll("a",href=True):
    if re.findall('definitie', a['href']):
        print(a['href'].rsplit('/',1)[1], file=outgroup)

outgroup.flush()
os.fsync(outgroup)
outgroup.close()
