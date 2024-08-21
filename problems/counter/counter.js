/**
 * @param {number} n
 * @return {Function} counter
 */
const createCounter = (n) => () => n++;

const assert = require('node:assert').strict;

const counter1 = createCounter(10);
assert.equal(counter1(), 10);
assert.equal(counter1(), 11);
assert.equal(counter1(), 12);

const counter2 = createCounter(-2);
assert.equal(counter2(), -2);
assert.equal(counter2(), -1);
assert.equal(counter2(), 0);
assert.equal(counter2(), 1);
assert.equal(counter2(), 2);
