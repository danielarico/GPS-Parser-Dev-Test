import json

with open('payload.json', 'r') as json_data:
  json_payload = json_data.read()

def parser(json_payload):
  data_str = extractData(json_payload)
  print(data_str)

  data = split(data_str)
  #print(data)
  #print(len(data))

  lat_str = extractLat(data)
  lon_str = extractLon(data)
  print(lat_str)
  print(lon_str)

  return 

def extractData(json_payload):
  payload = json.loads(json_payload)
  data = payload["data"] # Data as string
  return (data)

def split(word): 
  return [char for char in word]

def listToString(to_string):
  lat_str = ""
  return (lat_str.join(to_string))

def extractLat(data):
  lat = data[0:8]
  lat = listToString(lat)
  #falta convertir a numeros
  return lat

def extractLon(data):
  lon = data[8:16]
  lon = listToString(lon)
  #falta convertir a numeros
  return lon


parser(json_payload)