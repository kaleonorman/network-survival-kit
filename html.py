import urllib.request


response = urllib.request.urlopen('http://google.com')
html = response.read()
print (html);

