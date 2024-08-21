/**
 * @param {string} val
 * @return {Object}
 */
const expect = (val) => ({
  toBe: (otherVal) => val === otherVal ? true : (function(){throw "Not Equal"}()),
  notToBe: (otherVal) => val !== otherVal ? true : (function(){throw "Equal"}()),
});

const assert = require('node:assert').strict;

assert.equal(expect(5).toBe(5), true);
assert.throws(() => expect(5).notToBe(5), /^Equal$/);

assert.throws(() => expect(5).toBe(null), /^Not Equal$/);
assert.equal(expect(5).notToBe(null), true);
