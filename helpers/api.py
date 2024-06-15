import requests
import json
import os
import re

from dotenv import load_dotenv
load_dotenv()
brawl_stars_api_key = os.getenv('BRAWL_API_KEY')
brawl_api = os.getenv('BRAWL_API_ENDPOINT')
 
def GetBrawlEvents():

    try:
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": f'Bearer {brawl_stars_api_key}'}
        response = requests.get(brawl_api, headers = headers).json()

        res = []
        for data in response:
            res.append((data['event']['mode'], data['event']['map']))

        return res
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'I am unable to fetch Brawl Stars Events at the moment!'
