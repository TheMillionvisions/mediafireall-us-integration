import requests

# Base URL for the API
BASE_URL = "BASE_URL_HERE"  # Provide the base URL here

# User ID for authentication
User_ID = "YOUR_USERID_HERE"  # Provide your user ID here

# Start date and time in the format 'yyyy-mm-dd hh:mm:ss'
Start_Date_Time = ''  # Provide the start date and time here

# End date and time in the format 'yyyy-mm-dd hh:mm:ss'
End_Date_Time = ''  # Provide the end date and time here


url = f'https://{BASE_URL}/mfw/model/config/{User_ID}/type'


# Parameters for the API request
params = {
    'complete': 'true',  # Provide 'true' or 'false' to filter completed items
    'descend': 'true',   # Provide 'true' or 'false' to sort results in descending order
    'end': End_Date_Time,  # Provide the end date and time
    'pageNumber': 10,  # Provide the page number you want to view
    'pageSize': 10,  # Provide the number of elements per page
    'start': Start_Date_Time,  # Provide the start date and time
    'safe' : 'true',  # Provide 'true' or 'false' to filter by safe or unsafe content
    'apikey': 'YOUR_APIKEY_HERE',  # Provide your API key here
}

headers = {
  'Authorization': 'Bearer YOUR_TOKEN_HERE',
}

response = requests.get(url, params=params, headers = headers)
print(response.text)
