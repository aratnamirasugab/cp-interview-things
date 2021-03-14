#hashtable using dictionary
#declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#accessing the dics with the key
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
print "dict['Class']: ", dict['Class']

#we can change/ update the value of each key
dict['Age'] = 23
print(dict['Age'])

# delete
# we can remove one or clear entire hashtable
# with using del || dict.clear()

# length
# we can meausre the length of hashtable using len(dict)
print(len(dict))



# Hash Table is a data structure which organizes data using hash functions in order to support quick insertion and search.

# There are two different kinds of hash tables: hash set and hash map.

# The hash set is one of the implementations of a set data structure to store no repeated values.
# The hash map is one of the implementations of a map data structure to store (key, value) pairs.
# It is easy to use a hash table with the help of standard template libraries. Most common languages such as Java, C++ and Python support both hash set and hash map.

# By choosing a proper hash function, the hash table can achieve wonderful performance in both insertion and search.
