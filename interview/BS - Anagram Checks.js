function solve(s0,s1){
    // if s0, s1 not in the same length , return false
    // s0 = "listen"
    // s1 = "silent"

    if (s0.length !== s1.length) return false;

    // store 2 string into map
    let mep1 = new Map();
    let mep2 = new Map();
    
    for (let i = 0 ; i < s0.length ; i++) {
        if (!mep1.has(s0[i])) mep1.set(s0[i], 1);
        if (!mep2.has(s1[i])) mep2.set(s1[i], 1);
        if (mep1.has(s0[i])) {
            let val = mep1.get(s0[i]);
            val += 1;
            mep1.set(s0[i], val);
        }
        if (mep2.has(s1[i])) {
            let val = mep2.get(s1[i]);
            val += 1;
            mep2.set(s1[i], val);
        }
    }

    for (let [key, val] of mep1) {
        if (!mep2.has(key)) return false;
        let testVal = mep2.get(key);
        // check if testval is undefined return false
        // check if testVal is not the same value as val then return false
        if (testVal === undefined || testVal !== val) return false;
    }

    return true;
    
}

const res = solve("hah", "aah");
console.log(res);

