import json

def parserGPS(json_payload):
    output = {}
    data, device = extractValues(json_payload)

    lat_hex = data[0:8]
    lon_hex = data[8:16]
    others_hex = data[16:24]

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
    k = payload.keys()

    if "data" in k and "device" in k:
        data = str(payload["data"])
        device = str(payload["device"])
        if len(data) != 24:
            raise ValueError("Error in json argument: \"data\" length incorrect")
        else:
            return data, device
    else:
        raise KeyError("Error in json argument: keys are not the expected")


#-----------------------------------------
# Functions to decode variables
#-----------------------------------------
def decodeLat(lat_hex):
    # Hex to float latitude conversion
    return lat_hex


def decodeLon(lon_hex):
    # Hex to float longitude conversion
    return lon_hex


def decodeOthers(others_hex):
    others = {}
    other_vars = others_hex[0:2]
    adc1 = others_hex[2:5]
    adc0 = others_hex[5:9]

    other_vars_bin = bin(int(other_vars, 16))[2:].zfill(8)
    others["periodicity"] = int(other_vars_bin[0])
    others["data_type"] = int(other_vars_bin[1:6], 2)
    others["low_battery"] = int(other_vars_bin[6])
    others["digital_input"] = int(other_vars_bin[7])
    others["temperatureNTC"] = (int(adc0, 16) - 2340) / 58.5

    return others