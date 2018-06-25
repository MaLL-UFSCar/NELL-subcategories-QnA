# coding: utf-8
from subprocess import Popen, PIPE
import subprocess
import pandas as pd
import json


def getCategoriesList():
    process = subprocess.call(['java', '-jar', 'zenodotus.jar', '-gcl','-s','r.json'])
    
    result = pd.read_json('r.json')
    
    process = subprocess.call(["rm", "r.json"])
    
    return result


def getRelationsList():
    process = subprocess.call(['java', '-jar', 'zenodotus.jar', '-grl','-s','r.json'])
    
    result = pd.read_json('r.json')
    
    process = subprocess.call(["rm", "r.json"])
    
    return result


def getCategory(predicate):
    process = subprocess.call(['java', '-jar', 'zenodotus.jar', '-gc', str(predicate) ,'-s','r.json'])
    
    jsr = json.load(open('r.json'))
    
    try:
        category_name = str(jsr["category_name"])
        link = str(jsr["link"])
        category_prologue = str(jsr["category_prologue"])
        category_instances = pd.DataFrame(jsr["category_instances"])
        metadata = pd.DataFrame(jsr["metadata"])
        
        dic = {'category_name':category_name,'link':link,'category_prologue':category_prologue,
               'category_instances':category_instances,'metadata':metadata}
    except:
        dic = {'category_name':None,'link':None,'category_prologue':None,
               'category_instances':None,'metadata':None}
    
    process = subprocess.call(["rm", "r.json"])
    return dic

def isCategory(word):
    result = 'no'
    cat = getCategory(word)
    if(cat['category_name'] is not None): 
        result = 'yes'
    return result