#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/5 16:19
import requests
from bs4 import BeautifulSoup as bs


def getSoup(url):
    response = requests.get(url)
    response.raise_for_status()
    res = response.content
    soup = bs(res, 'html.parser')
    return soup