import requests
import json

url = 'http://api.letgo.com/api/iplookup.json' 
# get the response from the API using GET Method.
response = (requests.get(url))
# convert JSON response into python dictionary
resp= json.loads(response.text); 

print((resp))     

latitude = resp["latitude"]
longitude = resp["longitude"]
print((latitude,longitude))   
# 41.2619, -95.8608

# POST request
newResponse = requests.post(f'http://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json', data=None) 

# convert JSON response into python dictionary
newResp = json.loads(newResponse.text)

# print(newResponse.status_code)
print(newResp)

print("Display Name: ",newResp["display_name"])
if("city" in add):
  print("City: ",newResp["address"]["city"])
else:
  print("No City in the Response")

