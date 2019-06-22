

# Parse unstructured data from WWW with requests and feedparser


# For parsing data we genrally using following steps
   # request
   # return respose object
   # Check returned  status
   # get information 
   # parse the feed


import requests

# Here we get the whole data of the page in the form of json response
response_json = requests.get('https://github.com/adivyas99/Statistics-for-Data-Science-using-Python')
# if http request response is 200 request is success and 400 request is not found
print(response_json.status_code)

# that give the html format
print(response_json.text)

# parse the response object in to json format
print(response_json.json)
# find out the header information json parsing
print(response_json.headers)
# check the json text encoding we use 
print(response_json.encoding)

# For downloading and parsing syndicated feeds 
# It supports RSS, ATOM, CDF and iTunes extensions
import feedparser

dt = feedparser.parse('http://www.reddit.com/r/python/.rss')

# For title of the feed--
print (dt['feed']['title'])
# To see different headers--
print (dt.headers)
# to see the paresed link--
print (dt.entries[0].link)


