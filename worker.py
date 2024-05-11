import requests
import time

source = "https://maurder.com"

def run_worker_task():
    while True:
        response = requests.get(source + '/maurderPING')
        print(response)
        time.sleep(60)

if __name__ == "__main__":
    run_worker_task()