import requests

url = 'https://{BASE_URL}/oauth/token'

body = {
  "userId": "YOUR_USERID_HERE" ,  #provide your userId here
  "apikey": 'YOUR_APIKEY_HERE' #provide your api key here
}

response = requests.post(url)
print(response.text)
