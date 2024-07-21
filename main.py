#!/usr/bin/env python 

# # import lib.utils as utils
# config= utils.getConfig()
# # print(config)

import yaml
import gob.utils as utils
import gob.Brain as Brain
import json

loops = 6
brains = []

with open("config/first.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
print(data)
config_brains = data[0]['brains']
for b in config_brains:
    # print( brain)
    utils.showBrain(b)
    brain = Brain.Brain(b)
    brains.append(brain)

print("BRAINS", brains)

message= "Bonjour, qui es-tu?"

for x in range(loops):
    id_b = x%len(brains)
    print(x, id_b, brains[id_b])
    print("\bMESSAGE IN ", message)
    response = brains[id_b].get().sendMessage(message)
    print(response)
    m = response.messages[1]['function_call']['arguments']
#   m = json.dumps(messages.__dict__) 
#   #m = json.loads(messages)#[0]['function_call']['arguments']['message']
#   mess = json.loads(m)
    message = json.loads(m)['message']
    print("MESSAGE OUT ", message)