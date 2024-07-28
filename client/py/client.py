import requests

if __name__ == "__main__":
    server = "http://0.0.0.0:8080/hello"
    
    for i in range(1):
        resp = requests.get(server)
        print(resp.json())
