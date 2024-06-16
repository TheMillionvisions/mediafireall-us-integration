import requests

url = 'https://{BASE_URL}/moderation/{YOUR_ORG_ID_HERE}/{YOUR_USER_ID_HERE}/url/filters'


params = {
  'filters': 'YOUR_FILTERS_HERE',
  'apikey': 'YOUR_APIKEY_HERE',
  'mediaUrl': 'YOUR_MEDIA_URL_HERE',
}

headers = {
  'Authorization': 'Bearer YOUR_TOKEN_HERE',
}

response = requests.post(url, params=params, headers = headers)
print(response.text)
