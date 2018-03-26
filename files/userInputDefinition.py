from inuptOptions import *
from functionMap import *

def userInput(str, **kwargs):
    exceptions = []
    throws = []
    strings = []
    for key, value in kwargs.items
        keyFunction = functionMap[key]
        exceptions.append(keyFunction(value)[0])
        throws.append(keyFunction(value)[1])
        strings.append(keyFunction(value)[2])
        
    try:
        response = input(str)
        for throwable in throws:
            throwable(response)
            
    except Exception as exception:
        while:
            try:
                
                break
            
            except Exception as exception:
                
    
    
