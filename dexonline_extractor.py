from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import sys, os
hostname = str(sys.argv[1])
outgroup=open(hostname, 'wt')
url = urllib.request.urlopen("http://dexonline.ro/lista-cuvinte/"+hostname)
content = url.read()
soup = BeautifulSoup(content)
for a in soup.findAll("a",href=True):
    if re.findall('definitie', a['href']):
        print(a['href'], file=outgroup)

outgroup.flush()
os.fsync(outgroup)
outgroup.close()
