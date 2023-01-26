#creating a dictionary
a={"name":"zara","age":7,"class":"first"}
print(a)

#getting all keys from the dictionary
print(a.keys()) #is list(a.keys()) to display as list

#getting all the values from the dictionary
print(a.values()) 

#getting all the items from the dictionary as a list of tuples
print(a.items()) 

b={
    'fruits':{'apple':'5kg','custard apple':'3kg'},
    'vegetables':{"cabbage":'1 pc','tomato':'5 kg'},
    'cereals':{'rice':'1kg','wheat':'2kg'}

}

from pprint import pp
pp(b)

#accessing a value from dict
print (a['name'])
print(a['class'])

#print(a[city]) #keyerror:city

#accessing a value from a dictionary using get()
print(a.get('name'))
print(a.get('class'))
print(a.get('city'))
print(a.get('city','not found')) #the default value cannot be specified
print(a.get('name','not found'))

#traversing a dictionery
#style1
for key in a:
    print(key,a[key])
    
#style2
for key,value in a.items():
    print(key,value)