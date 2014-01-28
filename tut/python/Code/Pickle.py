######################################
# Topic: Explaing Pickle Module in python
# Copywrite: TechnologyExpress@dipankar
# Author : Dipankar Dutta
#######################################


import pickle

student = {'name': 'Python',
         'roll': ('class roll', 10),
         'subjects': ['python','djnago']
           }
colors = ['red', 'green', 'yellow']

output = open('data.pkl', 'wb')
# Pickle our data
pickle.dump(student, output)
pickle.dump(colors, output)
output.close()

#####################################
import pickle

inputfile= open('data.pkl', 'rb')

student = pickle.load(inputfile)
print student 
colors = pickle.load(inputfile)
print colors

inputfile.close()

#####################################3
count = 100
a = pickle.dumps(count)
print type(a) #what is type of a
b = pickle.loads(a)
print b
#######################################

import json

student = {'name': 'Python',
         'roll': ('class roll', 10),
         'subjects': ['python','djnago']
           }
colors = ['red', 'green', 'yellow']

output = open('data.json', 'w')
#Pickle our data
json.dump(student, output)
json.dump(colors, output)
output.close()
####################################
import json

inputfile= open('data.json',  'r')

#student = json.load(inputfile)
#print student 
#colors = json.load(inputfile)
#print colors

inputfile.close()
###################################

