import json
import requests

if __name__ == "__main__":
    print("sending post request. Adding Kyle to webserver...")
    response = requests.post(f"http://localhost:8888/data", data=json.dumps({
        "username": "kylejn27",
        'user_data': { 'name': 'kyle', 'dob': '06/27/1993' }
    }))  
    print("kyle has been added.")
    print()

    print("getting Kyle from the webserver")
    response = requests.get(f"http://localhost:8888/data/kylejn27").json()
    print(response)

  