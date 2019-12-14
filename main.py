import json
from modules.functions import parserGPS

def main():
    try:
        with open(json_route, 'r') as json_data:
            json_payload = json_data.read()
    except FileNotFoundError as error:
        print("File not found:" + repr(error))
    except Exception as error:
        print("Unknown exception: " + repr(error))
    
    variables = parserGPS(json_payload)
    print(variables)


if __name__ == "__main__":
    json_route = "data\payload.json"
    main()