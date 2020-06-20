// Write a function which receives a class and
// attaches to it a property species and a function toSpeciesString().
// When called, the function returns a string with format:
// "I am a <species>. <toString()>"
// The function toString() is called from the current instance (call using this).

// Stupid Description... to whomever wrote this problem... You need new JOB!

function extendProrotype(classToExtend) {
    classToExtend.prototype.species = 'Human';
    classToExtend.prototype.toSpeciesString = function() {
        return `I am a ${this.species}. ${this.toString()}`
    };
}
