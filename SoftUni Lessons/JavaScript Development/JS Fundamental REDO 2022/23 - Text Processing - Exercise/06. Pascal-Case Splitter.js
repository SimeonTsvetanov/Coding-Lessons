function pascalCaseSplitter (text) {
    // MasK
    let result = text.replace(/([A-Z])/g, ' $1')
        .replace(/^./, function(str){ return str.toUpperCase(); })
    result = result.split(' ').filter(function (e) {return e !== '';});
    console.log(result.join(', '));
}

pascalCaseSplitter('HoldTheDoor');