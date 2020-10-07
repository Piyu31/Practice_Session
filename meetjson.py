import json

x =  '{ "name":"John Smith", "age":27, "city":"America"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#convert pythob to json
x = {
  "name": "Eragon",
  "age": 3098,
  "city": "Valley"
}
y = json.dumps(x)
print(y)


print(json.dumps({"name": "Arthur", "age": 28}))
print(json.dumps(["white angel", "red devil"]))
print(json.dumps(("God", "Satan")))
print(json.dumps("howdieee"))
print(json.dumps(67))
print(json.dumps(98.56))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))