import requests
import time

BASE_URL = "BASE_URL_HERE" #provide the base url here
User_ID = "YOUR_USERID_HERE" #provide your userId here
Video_ID = "YOUR_VIDEOID_HERE" #provide videoId here


url = f'https://{BASE_URL}/mfw/model/config/{User_ID}/{Video_ID}'

params = {
  'apikey': 'YOUR_APIKEY_HERE', #provide your api key here
}

headers = {
  'Authorization': 'Bearer YOUR_TOKEN_HERE',
}

response_json = requests.get(url, params=params, headers = headers).json()

while True:
    if response_json.get("processStatus", {}).get("complete", False):
        print(response_json)
        break
    time.sleep(1)  # Wait for 1 second before checking again
