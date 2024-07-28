import os
import requests
import time

if __name__ == "__main__":
    server = os.environ.get("SERVER")
    port = int(os.environ.get("PORT", 8080))
    count = int(os.environ.get("NUM_REQUESTS", 1))
    url = f"http://{server}:{port}/hello"
    print(url)
    
    for i in range(count):
        print("--------  ", url)
        resp = requests.get(url)
        print(resp.json())

    time.sleep(86400 * 7)