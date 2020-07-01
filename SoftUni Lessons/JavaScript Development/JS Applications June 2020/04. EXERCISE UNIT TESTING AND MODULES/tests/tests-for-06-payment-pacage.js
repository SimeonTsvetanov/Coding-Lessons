// Test in Judge -> https://judge.softuni.bg/Contests/Practice/Index/974#1

let expect = require('chai').expect;
let PaymentPackage = require('../06. Payment Package').PaymentPackage;

describe("tests for PaymentPackage", function () {
    describe("test constructor", function () {
        it("should create an instance for ('mask, 69')", function name() {
            let newPayment = new PaymentPackage("mask", 69);
            expect(newPayment instanceof PaymentPackage).to.be.true;
        });

        it("should have correct values for ('mask', 60.5)", function name() {
            let p = new PaymentPackage('mask', 60.5);
            expect(p.name).to.be.equal("mask");
            expect(p.value).to.be.closeTo(60.5, 0.01);
            expect(p.VAT).to.be.closeTo(20, 0.01);
            expect(p.active).to.be.true;
            expect(p._active).to.be.true;
            expect(p.VAT).to.be.greaterThan(1);
            expect(p._VAT).to.be.greaterThan(1);
            expect(p.value).to.be.greaterThan(50);
            expect(p._value).to.be.greaterThan(50);
        });
        it("should throw error when initialised with incorrect values", function () {
            let p = null;
            expect(() => p = new PaymentPackage(123, 123)).to.throw(Error);
            expect(() => p = new PaymentPackage("correct", "asd")).to.throw(Error);
        })
    });

    describe("toString", function () {
        it("should return correct value for ('asdasd', 500)", function () {
            let p = new PaymentPackage("asdasd", 500);
            let expectedText = [
                `Package: ${p.name}` + '',
                `- Value (excl. VAT): ${p.value}`,
                `- Value (VAT ${p.VAT}%): ${p.value * (1 + p.VAT / 100)}`
            ].join("\n");
            let actualText = p.toString();

            expect(actualText).to.be.equal(expectedText);
        });

        it("should return correct value for ('0', 0) inactive", function () {
            let p = new PaymentPackage("0", 0);
            p.active = false;
            p.active = true;
            p.active = false;
            let expectedText = [
                `Package: ${p.name}` + ' (inactive)',
                `- Value (excl. VAT): ${p.value}`,
                `- Value (VAT ${p.VAT}%): ${p.value * (1 + p.VAT / 100)}`
            ].join("\n");
            let actualText = p.toString();

            expect(actualText).to.be.equal(expectedText);
        });
    })
});
