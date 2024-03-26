# import requests


# teg = '8UQURPRQU'

# API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNlYzU5OWVmLWRmMDMtNDkyYi04NWJlLTE4NTkxNDFlNTVjNSIsImlhdCI6MTcxMTQ3MjUxMSwic3ViIjoiZGV2ZWxvcGVyLzA4NzVkMWMyLTdhNWEtOTFkYy05N2IzLTI2NWM4YTQ4MjIxMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc4LjIwNC4yNTUuMjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.nAorbPk0CWZdu4s7E4xOWAhJoDzxrYFnGK3bXM_Kz147s5rSH9Y4yqfeFAbIXo1dOfVqLQh4iV9oeIz82TNVyQ'
# def get_battles(teg):
#     data = requests.get(f'https://api.brawlstars.com/v1/players/{teg}/battelog/', headers={
#         'Accept': 'application/json',
#         'authorization': f'Bearer {API_KEY}'
#     })
    
#     return data

# print(get_battles(teg))

import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNlYzU5OWVmLWRmMDMtNDkyYi04NWJlLTE4NTkxNDFlNTVjNSIsImlhdCI6MTcxMTQ3MjUxMSwic3ViIjoiZGV2ZWxvcGVyLzA4NzVkMWMyLTdhNWEtOTFkYy05N2IzLTI2NWM4YTQ4MjIxMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc4LjIwNC4yNTUuMjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.nAorbPk0CWZdu4s7E4xOWAhJoDzxrYFnGK3bXM_Kz147s5rSH9Y4yqfeFAbIXo1dOfVqLQh4iV9oeIz82TNVyQ'

tag = '8UQURPRQU'

headers = {
    'authority': 'api.brawlstars.com',
    'accept': 'application/json',
    'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer ' + token,
    'referer': 'https://developer.brawlstars.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

response = requests.get(f'https://api.brawlstars.com/v1/players/{tag}/battlelog', headers=headers).json()
print(response)