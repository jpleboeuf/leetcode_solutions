/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
};

const assert = require('node:assert').strict;

const counter1 = createCounter(5);
assert.equal(counter1.increment(), 6);
assert.equal(counter1.reset(), 5);
assert.equal(counter1.decrement(), 4);

const counter2 = createCounter(0);
assert.equal(counter2.increment(), 1);
assert.equal(counter2.increment(), 2);
assert.equal(counter2.decrement(), 1);
assert.equal(counter2.reset(), 0);
assert.equal(counter2.reset(), 0);
