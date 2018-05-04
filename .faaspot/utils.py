# https://pypi.python.org/pypi/tmdbv3api

# Implement your function here.
# The function will get the event as the first parameter with query/body properties:
# The function should return a Dictionary
import os
import json
import urlparse


def _build_response(response, stringify=True):
    response = json.dumps(response) if stringify else response
    return {
        'statusCode': 200,
        'body': response,
        'headers': {"Content-Type": "application/json"}
    }


