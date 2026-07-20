import requests
import time
website = input("Enter a website (include https://):")
try:
    start = time.time()
    response = requests.get(website)
    end = time.time()
    response_time = end - start
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Time: {response_time:.2f} seconds")
    if response.status_code == 200:
        print("Website is ONLINE")
    else:
        print("Website returned an unexpected status.")
except requests.exceptions.RequestsException:
    print("Websites is OFFLINE or unreachable.")