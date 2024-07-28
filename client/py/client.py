import os
import logging
import requests
import time

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    server = os.environ.get("SERVER")
    port = int(os.environ.get("PORT", 8080))
    count = int(os.environ.get("NUM_REQUESTS", 1))
    url = f"http://{server}:{port}/hello"

    for i in range(count):
        resp = requests.get(url)
        logging.info(resp.json())

    time.sleep(86400 * 7)