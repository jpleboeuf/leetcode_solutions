/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
const map = (arr, fn) => {
    const mapped_array = [];
    for (const [index, element] of arr.entries()) {
        mapped_array.push(fn(element, index));
    }
    return mapped_array;
};

const assert = require('node:assert').strict;

const arr1 = [1, 2, 3];
const plusone = (n) => n + 1;
const newArray1 = map(arr1, plusone);
assert.deepEqual(newArray1, [2, 3, 4]);

const arr2 = [1, 2, 3];
const plusI = (n, i) => n + i;
const newArray2 = map(arr2, plusI);
assert.deepEqual(newArray2, [1, 3, 5]);

const arr3 = [10, 20, 30];
const constant = () => 42;
const newArray3 = map(arr3, constant);
assert.deepEqual(newArray3, [42, 42, 42]);
