// HashMap in JS is Map

// to init
let firstHashMap = new Map();

//declaring and init
let secondHashMap = new Map([
    [1, 'first'],
    [2, 'second'],
    [5, 'fifth']
]);

console.log("firstHashMap : ", firstHashMap);
console.log("secondHashmap : ", secondHashMap);

/*
Useful Methods and Properties:
hashmap.size() returns the # of elements in the hashmap
hashmap.get(<key>) returns the value of the element of the given key
hashmap.has(<key>) checks to see if the hashmap contains the key that is passed as an argument
hashmap.set(<key>, <value>) accepts 2 arguments and creates a new element to the hashmap
hashmap.delete(<key>) deletes the key/value pair that matches the key that is passed in as an argument
hashmap.clear() clears all elements from the hashmap
*/

console.log(secondHashMap.size);