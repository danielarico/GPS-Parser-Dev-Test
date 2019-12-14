import json

def parserGPS(json_payload):
    output = {}
    data, device = extractValues(json_payload)
    print("Data: " + data)

    lat_hex = data[0:8]
    lon_hex = data[8:16]
    others_hex = data[16:24]

    print("part1: " + lat_hex)
    print("part2: " + lon_hex)
    print("part3: " + others_hex)

    output["device"] = device
    output["latitude"] = decodeLat(lat_hex)
    output["longitude"] = decodeLon(lon_hex)
    others = decodeOthers(others_hex)

    output.update(others)
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
    other_vars = others_hex[0:2]
    adc1 = others_hex[2:5]
    adc0 = others_hex[5:9]
    
    print("other vars: " + other_vars)
    print("adc1: " + adc1)
    print("adc0: " + adc0)

    other_vars_bin = bin(int(other_vars, 16))[2:].zfill(8)
    others["periodicity"] = int(other_vars_bin[0])
    others["data_type"] = int(other_vars_bin[1:6], 2)
    others["low_battery"] = int(other_vars_bin[6])
    others["digital_input"] = int(other_vars_bin[7])
    others["temperatureNTC"] = (int(adc0, 16) - 2340) / 58.5

    print("other_vars_bin: " + other_vars_bin)
    print("\nOthers dictionary:\n")
    print(others)
    return others