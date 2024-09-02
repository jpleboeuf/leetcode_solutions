/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
const filter = (arr, fn) => {
    const filteredArray = [];
    for (const [index, element] of arr.entries()) {
        fn(element, index) && filteredArray.push(element);
    }
    return filteredArray;
};

const assert = require('node:assert').strict;

const arr1 = [0, 10, 20, 30];
const greaterThan10 = (n) => n > 10;
const newArray1 = filter(arr1, greaterThan10);
assert.deepEqual(newArray1, [20, 30]);

const arr2 = [1, 2, 3];
const firstIndex = (n, i) => i === 0;
const newArray2 = filter(arr2, firstIndex);
assert.deepEqual(newArray2, [1]);

const arr3 = [-2, -1, 0, 1, 2];
const plusOne = (n) => n + 1;
const newArray3 = filter(arr3, plusOne);
assert.deepEqual(newArray3, [-2, 0, 1, 2]);
