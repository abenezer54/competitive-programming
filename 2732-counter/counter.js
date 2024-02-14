/**
 * @param {number} n
 * @return {Function} counter
 */
 
var createCounter = function(n) {
    let count = 0;
    return function() {
        count += 1;
        console.log(count);
        return n + count - 1;
        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */