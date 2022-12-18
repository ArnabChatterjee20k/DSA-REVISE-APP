import os
import requests

url = os.environ.get("DSA_SHEET")

content = requests.get(url)
json = content.json()
