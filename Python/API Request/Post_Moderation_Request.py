import requests

BASE_URL = "BASE_URL_HERE" #provide the base url here
User_ID = "YOUR_USERID_HERE" #provide your userId here
Org_ID = "YOUR_ORGID_HERE" #provide your orgId here

url = f'https://{BASE_URL}/moderation/{Org_ID}/{User_ID}/url/filters'


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
