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
        
        return category_name,link,category_prologue,category_instances,metadata
        
    except:
        return None,None,None,None,None
    
    
    process = subprocess.call(["rm", "r.json"])