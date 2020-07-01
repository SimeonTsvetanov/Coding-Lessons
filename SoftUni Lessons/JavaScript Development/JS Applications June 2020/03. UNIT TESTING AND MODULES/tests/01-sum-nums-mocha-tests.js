let expect = require('chai').expect;
let sum = require('../01. Sum of Numbers').sum;
// judge - https://judge.softuni.bg/Contests/Practice/Index/307#3

describe('sum(arr) - sum array of numbers', function () {
    it('should return 3 for [1, 2]', function () {
        let expectedSum = 3;
        let actualSum = sum([1, 2]);
        expect(actualSum).to.equal(actualSum);
    });

    it('should return 4 for [1, 1, 2]', function () {
        let expectedSum = 4;
        let actualSum = sum([1, 1, 2]);
        expect(actualSum).to.equal(actualSum);
    });

    it("should return 3 for [1.5, 2.5, -1]", function () {
        expect(sum([1.5, 2.5, -1])).to.be.equal(3);
    });

    it('should return 0 for []', function () {
        let expectedSum = 0;
        let actualSum = sum([]);
        expect(actualSum).to.equal(actualSum);
    });

    it('should return error if argument in array is string', function () {
        let actualSum = sum(['mask']);
        expect(actualSum).to.be.NaN;
    });
});