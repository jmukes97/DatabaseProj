from dbDataStructures import *
from databaseInit import *
from inventoryFunctions import *
from orderingFunctions import *
import code

# import only system from os 
from os import system, name 
  
# define our clear function 
def cls(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

code.interact(local = locals())