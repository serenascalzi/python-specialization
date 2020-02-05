# chapter 12
# networked programs

# socket program
import socket

url = input('Enter URL: ')
try:
    url.startswith('http') == True
    start = url.find('/')
    mid = url.find('/', start + 1)
    end = url.find('/', mid + 1)
    host = url[mid + 1 : end]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    count = 0
    while True:
        data = mysock.recv(3000)
        if len(data) < 1:
            break
        count = count + len(data)
        print(data.decode(), end = '')
    print('Characters:', count)
except:
    print('Please enter a full & valid URL!')
    exit()

mysock.close()

# urllib program
import urllib.request

url = input('Enter URL: ')
try:
    url.startswith('http') == True
    fhand = urllib.request.urlopen(url)
    count = 0
    for line in fhand:
        count = count + len(line)
        print(line.decode().strip())
    print('Characters:', count)
except:
    print('Please enter a full & valid URL!')
    exit()

# urllinks program
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
tags = soup('p')
for tag in tags:
    count = count + 1
print('Paragraphs:', count)

# graded external tool #1
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = '')

mysock.close()

# graded external tool #2
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
sum = 0
for span in spans:
    strings = str(span)
    numbers = re.findall('([0-9]+)', strings)
    if len(numbers) > 0:
        for number in numbers:
            num = int(number)
            sum = sum + num
print(sum)

# graded external tool #3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = input('Enter Count - ')
position = input('Enter Position - ')

ct = int(count)
pos = int(position)

counter = 0

while counter <= ct:
    print(url)

    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    alllinks = list()
    links = soup('a')
    for link in links:
        strings = str(link)
        urls = re.findall('"(http[s]?://.*?)"', strings)
        if len(urls) > 0:
            for u in urls:
                alllinks.append(u)
    url = alllinks[pos - 1]
    counter = counter + 1

# advanced
# Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
