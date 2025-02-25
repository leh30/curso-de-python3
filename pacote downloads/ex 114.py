import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.bing.com')
except:
    print('DEU ERRO!')
else:
    print('TUDO OK!')
    print(site.read())