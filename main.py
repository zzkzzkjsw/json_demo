import json
data={
    "description":"I am a dict",
    "array":["1",2,3]
}

'''
1. json.dumps(dict) returns a str
'''
jsonstr=json.dumps(data)
print(type(jsonstr),jsonstr)
with open("data.json","w") as f:
    f.write(jsonstr)


# =====================================================================
with open("data.json","r") as f:
    jsonstr=f.read()

'''
2. json.loads(str) returns a dict
'''
data2=json.loads(jsonstr)
print(type(data2),data2)


# =====================================================================



