import json

def read(value: str): 
  with open("config.json", "r") as file: 
    data = json.load(file)

  return data[value]
