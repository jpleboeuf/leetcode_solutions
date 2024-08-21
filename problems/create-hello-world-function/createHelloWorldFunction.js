/**
 * @return {Function}
 */
const createHelloWorld = () => (...args) => "Hello World";

const assert = require('node:assert').strict;

const f1 = createHelloWorld();
const args1 = [];
assert.equal(f1(args1), "Hello World");

const f2 = createHelloWorld();
const args2 = [{}, null, 42];
assert.equal(f2(args2), "Hello World");
