import requests

def client():
    token_h = "Token d4a927881060a986a4e5eec5f5c8d8f11751132f"

    header = {"Authorization": token_h}
    
    credentials = {
        "username": "rapmendes",
        "password": "dodobird1"
    }
    # response = requests.post(   
    #                             "http://127.0.0.1:8000/api/rest-auth/login/",
    #                             data=credentials
    #                         )

    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=header)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()