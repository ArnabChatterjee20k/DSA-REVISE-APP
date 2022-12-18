import os
import requests

url = os.getenv("DSA_SHEET")

content = requests.get(url)
json = content.json()