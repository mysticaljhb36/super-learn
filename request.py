# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:55:03 2020

@author: DELL
"""

import requests

url = "http://127.0.0.1:5000/"
r = request.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())