# 1 UPDATE VALUES IN DICTIONARIES AND LISTS

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 

print(x)
x[1][0]=15
print(x)


#Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students)
students[0]['last_name']='Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_directory)
sports_directory["soccer"][0]='Andres'
print(sports_directory)


# Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]

print(z)
z[0]['y']=30
print(z)


# 2 ITERATE THROUGH A LIST OF DICTIONARIES

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# FIRST ATTEMPT:    
def iterateDictionary(some_list):
    for index in some_list: 
        new_list=[]
        for item in index.items():
            for x in item:
                new_list.append(x)
        print(new_list[0]+" - "+new_list[1]+", "+new_list[2]+" - "+new_list[3])        

iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonelcopy

students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan', 'age':'3'},
        {'first_name' : 'John', 'last_name' : 'Rosales', 'age':'5'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age':'7'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age':'7'}
    ]
students3 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan', 'age':'3', 'favorite color': 'red'},
        {'first_name' : 'John', 'last_name' : 'Rosales', 'age':'5', 'favorite color': 'blue'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age':'7', 'favorite color': 'green'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age':'9', 'favorite color': 'yellow'}
    ]

# IMPROVED VERSION:    
def iterateDictionary(some_list):
    for index in some_list: 
        new_string=""
        for item in index.items():
            new_string=new_string+str(item[0])+" - "+str(item[1])+", "
        new_string=new_string[:-2]
        print(new_string)

iterateDictionary(students1) 
print("or")
iterateDictionary(students2) 
print("or")
iterateDictionary(students3) 


# 3 GET VALUES FROM A LIST OF DICTIONARIES

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan', 'age':'3'},
        {'first_name' : 'John', 'last_name' : 'Rosales', 'age':'5'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age':'7'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age':'7'}
    ]
students3 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan', 'age':'3', 'favorite color': 'red'},
        {'first_name' : 'John', 'last_name' : 'Rosales', 'age':'5', 'favorite color': 'blue'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age':'7', 'favorite color': 'green'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age':'9', 'favorite color': 'yellow'}
    ]

def iterateDictionary2(key_name,some_list):
    for index in some_list:
        print(index[key_name])
print("First names:")
iterateDictionary2('first_name',students1)
print("")
print("Last names:")
iterateDictionary2('last_name',students1)
print("")
print("Ages:")
iterateDictionary2('age',students3)
print("")
print("Favorite colors:")
iterateDictionary2('favorite color',students3)



# 4 ITERATE THROUGH A DICTIONARY WITH LIST VALUES

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for listt in some_dict:
        print(len(some_dict[listt]),listt.upper())
        for name in some_dict[listt]:
            print(name)
        print("")

printInfo(dojo)