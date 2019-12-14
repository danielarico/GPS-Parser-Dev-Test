import json
from modules.functions import parserGPS

def main():
    with open(json_route, 'r') as json_data:
        json_payload = json_data.read()
    variables = parserGPS(json_payload)
    print("\nFinal dictionary:\n")
    print(variables)


if __name__ == "__main__":
    json_route = "data\payload.json"
    main()