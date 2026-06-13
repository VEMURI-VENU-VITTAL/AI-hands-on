import json
import re


def extractJson(response):
    matches = re.findall(r'\{.*?\}', response)
    if len(matches)==0: return {}
    return json.loads(matches[0])