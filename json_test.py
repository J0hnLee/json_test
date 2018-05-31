import json
'''
event ={
  "array": [
    1,
    2,
    3
  ],
  "boolean": 'true',
  "null": 'null',
  "number": '123',
  "object": {
    "a": "b",
    "c": "d",
    "e": "f"
  },
  "string": "Hello World"
}


encodedjson = json.dumps(event)
print(encodedjson)


'''
import json
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
event ={
  "array": [
    1,
    2,
    3
  ],
  "boolean": 'true',
  "null": 'null',
  "number": '123',
  "object": {
    "a": "b",
    "c": "d",
    "e": "f"
  },
  "string": "Hello World"
}

json_str = json.dumps(event)
data=json.loads(json_str,object_hook=JSONObject)
print(data.string)