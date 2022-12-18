import os
import requests

url = os.environ("DSA_SHEET")

content = requests.get(url)
json = content.json()
