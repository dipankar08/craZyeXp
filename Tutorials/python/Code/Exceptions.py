######################################
# Topic: Explaing Exception Handaling in Pythobn
# Copywrite: TechnologyExpress@dipankar
# Author : Dipankar Dutta
#######################################

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        print 'Cool ! You Entered '+str(x) +'.'
    except:
        print 'OOPs ! you enter other than integer' 
    else:
        print 'Done! Exiting'
        break;

################################
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "The File Should be an Integer"
except Exception,e:
    print "Unexpected error:", e
else:
    f.close()
finally:
    print 'ThankYou'
########################################
class HostUnreacble(Exception):
     def __init__(self):
         self.value = 505
     def __str__(self):
        return 'Host is not rechable. ErrorCode:'+str(self.value)

try:
    raise HostUnreacble()
except HostUnreacble as e:
    print e

