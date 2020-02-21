#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#  /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\  
# <   -  Brandhunt Product Update Scraper Module  -   >
#  \|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/

# --- IMPORT SECTION --- #

import os
import requests
import json
import importlib.util

ext_py_mod_url = os.environ['MORPH_GET_SCRIPT_URL']

r = requests.get(ext_py_mod_url)
jsonpy = json.loads(r.content)
filecont = jsonpy[0]['file_cont']
filecont = json.loads(filecont)

with open('prod_update_copy.py','w') as newfile:
    for cont in filecont:
        newfile.write(cont)

#spec = importlib.util.spec_from_loader('helper', loader=None)
#helper = importlib.util.module_from_spec(spec)
#for cont in filecont:
#    exec(cont, helper.__dict__)

#print(type(helper)) # prints "<class 'module'>"
#helper.a # prints "5"
