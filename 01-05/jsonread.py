import json
with open('/home/zaidi/GitHub-Projects/praxis-academy/01-05/iso3166_full.json') as jsonfile:
    parsed = json.load(jsonfile)
print (json.dumps(parsed, indent=2, sort_keys=True))