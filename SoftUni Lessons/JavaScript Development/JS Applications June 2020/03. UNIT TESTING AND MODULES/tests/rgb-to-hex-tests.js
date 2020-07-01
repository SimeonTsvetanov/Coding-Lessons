// Judge -> https://judge.softuni.bg/Contests/Practice/Index/307#5

let expect = require('chai').expect;
let rgbToHexColor = require('../03. RGB to Hex').rgbToHexColor;


describe('tests for rgb to hex', function () {
    describe('Valid tests, should return hex colors if valid input is given', function () {
        it("should return #FF9EAA for (255, 158, 170)", function () {
            expect(rgbToHexColor(255, 158, 170)).to.be.equal("#FF9EAA");
        });
        it("should return #0C0D0E for (12, 13, 14)", function () {
            expect(rgbToHexColor(12, 13, 14)).to.be.equal("#0C0D0E");
        });
        it("should return #000000 for (0, 0, 0)", function () {
            expect(rgbToHexColor(0, 0, 0)).to.be.equal("#000000");
        });
    });

    describe('Invalid tests, should return undefined if invalid value is given', function () {
        it("should return undefined if red is String", function () {
            expect(rgbToHexColor('255', 158, 170)).to.be.undefined;
        });
        it('should return undefined if red is below zero', function () {
            expect(rgbToHexColor(-255, 158, 170)).to.be.undefined;
        });
        it('should return undefined if red is bigger than 255', function () {
            expect(rgbToHexColor( 256, 158, 170)).to.be.undefined;
        });
        it('should return undefined if red is float', function () {
            expect(rgbToHexColor( 256.3, 158, 170)).to.be.undefined;
        });
        it('should return undefined if not enough params are given.', function () {
            expect(rgbToHexColor(158, 170)).to.be.undefined;
        });
    });
});