import requests
import json

url = 'http://api.letgo.com/api/iplookup.json' 

# get the response from the API using GET Method.
response = (requests.get(url))

# convert JSON response into python dictionary
resp= json.loads(response.text); 

# (28.6504, 77.2372)
# print((resp)) 

latitude = resp["latitude"]
longitude = resp["longitude"]
# print((latitude,longitude)) 

# POST request
newUrl = 'http://nominatim.openstreetmap.org/reverse?lat={}&lon={}&format=json'.format(latitude,longitude);

newResponse = requests.post(newUrl, data=None) 

# convert JSON response into python dictionary
newResp = json.loads(newResponse.text)

# print(newResponse.status_code)
# print(newResp)

print("Display Name: ",newResp["display_name"])
add= newResp["address"];

# for some latitude and longitude city is not there int the response like (lat  = #41.2619,long= -95.8608) so need to handle the case   

if("city" in add):
  print("City: ",newResp["address"]["city"])
else:
  print("No City in the Response")

