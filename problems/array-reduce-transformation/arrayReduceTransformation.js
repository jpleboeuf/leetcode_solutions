/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
const reduce = (nums, fn, init) => {
    let result = init;
    for (const num of nums) {
        result = fn(result, num)
    }
    return result;
};

const assert = require('node:assert').strict;

const nums1 = [1, 2, 3, 4];
const sum1 = (accum, curr) => accum + curr;
const init1 = 0;
const result1 = reduce(nums1, sum1, init1);
assert.deepEqual(result1, 10);

const nums2 = [1, 2, 3, 4];
const sum2 = (accum, curr) => accum + curr * curr;
const init2 = 100;
const result2 = reduce(nums2, sum2, init2);
assert.deepEqual(result2, 130);

const nums3 = [];
const sum3 = (accum, curr) => 0;
const init3 = 25;
const result3 = reduce(nums3, sum3, init3);
assert.deepEqual(result3, 25);
