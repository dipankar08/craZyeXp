# Ch1 : Read file
import xml.etree.ElementTree as ET
>>> tree = ET.parse('etree.xml')
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x7f12ae09fa90>
>>> root = tree.getroot()
>>> root
<Element 'data' at 0x7f12ae042090>

#Ch2 REad String
>>> f = open('etree.xml')
>>> data = f.read()
>>> data
'<?xml version="1.0"?>\n<data>\n    <country name="Liechtenstein">\n        <rank>1</rank>\n        <year>2008</year>\n        <gdppc>141100</gdppc>\n        <neighbor name="Austria" direction="E"/>\n        <neighbor name="Switzerland" direction="W"/>\n    </country>\n    <country name="Singapore">\n        <rank>4</rank>\n        <year>2011</year>\n        <gdppc>59900</gdppc>\n        <neighbor name="Malaysia" direction="N"/>\n    </country>\n    <country name="Panama">\n        <rank>68</rank>\n        <year>2011</year>\n        <gdppc>13600</gdppc>\n        <neighbor name="Costa Rica" direction="W"/>\n        <neighbor name="Colombia" direction="E"/>\n    </country>\n</data>\n'
>>> root = ET.fromstring(data)
>>> root
<Element 'data' at 0x7f12ae0427d0>
>>> 

# Getting tag and attaribute 
>>> root.tag
'data'
>>> root.attrib
{}
>>> root[0]
<Element 'country' at 0x7f12ae042810>
>>> root[0].attrib
{'name': 'Liechtenstein'}
>>> root[0].attrib.get('name')
'Liechtenstein'
>>>
>>> root[0].items() # Rturn name value pair
[('name', 'Liechtenstein')]
>>> 
>>> root[0].keys()
['name']
>>> root[0].keys() == root[0].attrib.keys()
True
>>> 

#Get Child.
>>> root.getchildren()
[<Element 'country' at 0x7f12ae042810>, <Element 'country' at 0x7f12ae042990>, <Element 'country' at 0x7f12ae042ad0>]

>>> for c in root.getchildren():
...   print c.tag, c.attrib
... 
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
>>> 
#Access child by index.. That's great
>>> for c in root:
...   print c.tag, c.attrib
... 
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
>>> 
>>> root[0].tag
'country'
>>> root[0][0].tag
'rank'
>>> root[0][0].text
'1'
>>> 
# Findalla nd find text
>>> for i in root.findall('country') : # Find all country
...   print i.findtext('rank') # Find text of having tag rank of exha country
... 
1
4
68
>>> 
>>> for i in root.findall('neighbor') : # Not find in substructure
...   print i.attrib['name']
... 
>>> 
>>> root.find('country') # Return first occuranees
<Element 'country' at 0x7f12ae042810>
>>> root.find('country').attrib
{'name': 'Liechtenstein'}
>>>>>> root.find('countryt') # Not match return NULL
>>> 