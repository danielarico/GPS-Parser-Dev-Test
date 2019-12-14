import json

with open('payload.json', 'r') as json_data:
  json_payload = json_data.read()

def parser(json_payload):
  data_str = extractData(json_payload)
  print(data_str)

  data = split(data_str)
  
  lat = decodeLat(data)
  lon = decodeLon(data)
  others = decodeOthers(data)
  adc = decodeAdc(data)

  print(lat)
  print(lon)
  print(others)
  print(adc)

  return 

#-----------------------------------------
# Auxiliar functions
#-----------------------------------------
def split(word): 
  return [char for char in word]

def listToString(to_string):
  lat_str = ""
  return (lat_str.join(to_string))

#-----------------------------------------
# Functions to extract bytes 
#-----------------------------------------
def extractData(json_payload):
  payload = json.loads(json_payload)
  data = payload["data"] # Data as string
  return (data)

def extractLat(data):
  lat = data[0:8]
  lat = listToString(lat)
  return lat

def extractLon(data):
  lon = data[8:16]
  lon = listToString(lon)
  return lon

def extractOthers(data):
  others = data[16:18]
  others = listToString(others)
  return others

def extractAdc(data):
  adc = data[18:24]
  adc = listToString(adc)
  return adc

#-----------------------------------------
# Functions to decode variables
#-----------------------------------------
def decodeLat(data):
  lat_str = extractLat(data)
  return lat_str

def decodeLon(data):
  lon_str = extractLon(data)
  return lon_str

def decodeOthers(data):
  others_str = extractOthers(data)
  return others_str

def decodeAdc(data):
  adc_str = extractAdc(data)
  return adc_str

#-----------------------------------------
# Function call
#-----------------------------------------
parser(json_payload)