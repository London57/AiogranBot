import brawlstats
from pprint import pprint

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNlYzU5OWVmLWRmMDMtNDkyYi04NWJlLTE4NTkxNDFlNTVjNSIsImlhdCI6MTcxMTQ3MjUxMSwic3ViIjoiZGV2ZWxvcGVyLzA4NzVkMWMyLTdhNWEtOTFkYy05N2IzLTI2NWM4YTQ4MjIxMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc4LjIwNC4yNTUuMjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.nAorbPk0CWZdu4s7E4xOWAhJoDzxrYFnGK3bXM_Kz147s5rSH9Y4yqfeFAbIXo1dOfVqLQh4iV9oeIz82TNVyQ'

client = brawlstats.Client(token)

tag = '8UQURPRQU'

player = client.get_profile(tag)

print(player.__dict__)