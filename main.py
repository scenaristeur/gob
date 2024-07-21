#!/usr/bin/env python 

# # import lib.utils as utils
# config= utils.getConfig()
# # print(config)

import yaml
import gob.utils as utils
import gob.Brain as Brain

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