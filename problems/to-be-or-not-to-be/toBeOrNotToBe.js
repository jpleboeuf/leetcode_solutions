/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    
};

const assert = require('node:assert').strict;

assert.equal(expect(5).toBe(5), true);
assert.throws(() => expect(5).notToBe(5), /^Equal$/);

assert.throws(() => expect(5).toBe(null), /^Not Equal$/);
assert.equal(expect(5).notToBe(null), true);
