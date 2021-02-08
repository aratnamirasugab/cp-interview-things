/**
 Hashtables are often coveted in algorithm optimization for their O(1) constant time lookup. While JavaScript doesn’t have a native Hashtable class, 
 it does have native Objects and Hashmaps(Map) that offer similar functionality when it comes to organizing key/value pairs.
 
 Hashtable vs Hashmap:
 Hashtables and hashmaps are data structures that store data in an array-like format, using key/value pairs, where the (hashed) key corresponds to the index in the array. 
 One of the primary benefits that a hashtable has over a hashmap is the native ability to handle synchronous updates. This means that a hashtable can be shared by multiple 
 threads without introducing desynching errors.
 
 Hashmaps offer the same key/value functionality and come native in JavaScript (ES6) in the form of the Map() object (not to be confused with Array.prototype.map()). 
 While hashmaps are limited to single-threaded code, they do have some benefits, for instance the allowance of null values which allows for greater flexibility.
 
 JavaScript Objects: Similar but Different
 You might be thinking, “but JavaScript objects already keep track of key/value pairs.” While you can use JS objects to serve the same function of a hashmap, 
 a hashmap does offer some benefits. For instance, hashmaps offer greater flexibility. The key in a hashmap can be any datatype, this includes arrays and objects. 
 Meanwhile, objects can only use integers, strings, and symbols as their keys.
 
 Hashmaps are organized as linked lists, so the order of its elements is maintained, which allows the hashmap to be iterable. Also, unlike key/value pairs stored in an Object, 
 the number of items in a hashmap can be determined by the size property.
 
 Note: One of the primary pitfalls to be aware of when it comes to hashmaps in JavaScript, is that they cannot be directly translated to JSON.
 
 */
