import json

def parserGPS(json_payload):
    output = {}
    data, device = extractValues(json_payload)
    print(data)

    lat = data[0:8]
    lon = data[8:16]
    oth = data[16:24]

    print(lat)
    print(lon)
    print(oth)

    output["latitude"] = decodeLat(lat)
    output["longitude"] = decodeLon(lon)
    others = decodeOthers(oth)
    output.update(others)
    print(output)
    return output


#-----------------------------------------
# Function to extract json values 
#-----------------------------------------
def extractValues(json_payload):
  payload = json.loads(json_payload)
  # Verificar si existen los keys
  data = payload["data"]
  device = payload["device"]
  return data, device


#-----------------------------------------
# Functions to decode variables
#-----------------------------------------
def decodeLat(lat_hex):
    lat = int(lat_hex, 16)
    return lat


def decodeLon(lon_hex):
    lon = int(lon_hex, 16)
    return lon


def decodeOthers(others_hex):
    others = {}
    print(others_hex)
    byte = others_hex[0:2]
    adc1 = others_hex[2:5]
    adc0 = others_hex[5:9]

    print(byte)
    print(adc1)
    print(adc0)

    
    return others


#-----------------------------------------
# Auxiliar functions
#-----------------------------------------
def listToString(to_string):
  lat_str = ""
  return (lat_str.join(to_string))
