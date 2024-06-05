import requests
import time


User_ID = "" #provide your userId here
Video_ID = "" #provide videoId here


url = 'https://apimediafirewall-us.millionvisions.ai/mfw/model/config/{User_ID}/{Video_ID}'
params = {
  'apikey': '', #provide your api key here
}

response_json = requests.get(url, params=params).json()

while True:
    if response_json.get("processStatus", {}).get("complete", False):
        print(response_json)
        break
    time.sleep(1)  # Wait for 1 second before checking again
