import requests

url = 'https://{BASE_URL}/moderation/{YOUR_ORG_ID_HERE}/{YOUR_USER_ID_HERE}/url/filters'


params = {
  'filters': 'YOUR_FILTERS_HERE',  #provide your filters here
  'apikey': 'YOUR_APIKEY_HERE',  #provide your apikey here
  'mediaUrl': 'YOUR_MEDIA_URL_HERE',  #provide your mediaurl here
}

headers = {
  'Authorization': 'Bearer YOUR_TOKEN_HERE', 
}

response = requests.post(url, params=params, headers = headers)
print(response.text)
