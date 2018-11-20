import json
import yaml

sample = {
  "foo": "bar",
  "baz": [
    "qux",
    "quxx"
  ],
  "corge": None,
  "grault": 1,
  "garply": True,
  "waldo": "false",
  "fred": "undefined",
  "emptyArray": [],
  "emptyObject": {},
  "emptyString": ""
}

json_obj = json.dumps(sample)
print ('json_obj =', json_obj)

ff = open('data.yml', 'wb')
yaml.dump(sample, ff, default_flow_style=False)

ydump = yaml.dump(sample, default_flow_style=False)
print ('ydump=',ydump)