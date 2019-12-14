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

  """
  print(lat)
  print(lon)
  print(others)
  print(adc)
  """
  return 

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
  print(others_str)
  others_bin = strToBin(others_str)
  print(others_bin)
  others = split(others_bin)
  return others_str

def decodeAdc(data):
  adc_str = extractAdc(data)
  return adc_str

#-----------------------------------------
# Auxiliar functions
#-----------------------------------------
def split(word): 
  return [char for char in word]

def listToString(to_string):
  lat_str = ""
  return (lat_str.join(to_string))

def strToBin(my_string):
  scale = 16
  num_of_bits = 8
  binary_str = bin(int(my_string, scale))[2:].zfill(num_of_bits)
  return binary_str

#-----------------------------------------
# Function call
#-----------------------------------------
parser(json_payload)