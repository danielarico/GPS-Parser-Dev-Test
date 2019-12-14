import sys
from modules.functions import parserGPS

def main(json_route):
    try:
        with open(json_route, 'r') as json_data:
            json_payload = json_data.read()
    except FileNotFoundError as e:
        print("File not found:" + repr(e))
    except Exception as e:
        print("Unknown exception: " + repr(e))
    
    variables = parserGPS(json_payload)
    print(variables)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError as e:
        print(repr(e) + "\nExpecting json argument")
