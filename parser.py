import json

with open('payload.json', 'r') as json_data:
  json_payload = json_data.read()

def parser(json_payload):
  data_str = extractData(json_payload)
  print(data_str)

  data = split(data_str)
  #print(data)
  #print(len(data))

  lat = extractLat(data)
  #lon = extract_lon(data)

  return 

def extractData(json_payload):
  payload = json.loads(json_payload)
  data = payload["data"] # Data as string
  return (data)

def split(word): 
  return [char for char in word]

def extractLat(data):
  lat = data[0:8]
  lat = listToString(lat)
  print(lat)
  #falta convertir a numeros
  return lat

def listToString(to_string):
  lat_str = ""
  return (lat_str.join(to_string))


parser(json_payload)