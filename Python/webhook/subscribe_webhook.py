import requests

userID = "" #provide your userId here 
webhooks = [
        "https://example.com/webhook","https://example1.com/webhook"   #provide your webhook urls here 
        ]

url = "https://{BASE_URL}/notification/webhook"

body = {
    "userId" : userID,
    "webhooks" : webhooks
}

headers = {'Content-Type': 'application/json','Authorization':'Bearer token'}

params = {
  'apikey': '' #provide your apikey here
}

response = requests.post(url,params=params,json=body ,headers=headers)

if response.status_code == 201:
    print("Webhook request sent successfully. Please check the webhook message and click on the SubscribeUrl.")       
else:
    print("Failed to send POST request. Status code:", response.status_code)
    print("Response content:", response.content)

