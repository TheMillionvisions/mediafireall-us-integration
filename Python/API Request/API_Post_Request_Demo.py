import requests

url = 'https://apimediafirewall-us.millionvisions.ai/mfw/media/example@email.com/url/filters'

params = {
  'filters': '',
  'apikey': '',
  'mediaUrl': '',
}

headers = {
  'Authorization': 'Bearer token',
}

response = requests.post(url, params=params, headers = headers)
print(response.text)
